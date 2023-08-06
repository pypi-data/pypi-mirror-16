"""Tree-based minimization algorithms."""

import copy
import inspect
import numbers
import numpy as np

from collections import Iterable

from sklearn.base import clone
from sklearn.base import is_regressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.utils import check_random_state

from .acquisition import _gaussian_acquisition
from .callbacks import check_callback
from .callbacks import VerboseCallback
from .learning import ExtraTreesRegressor
from .learning import GradientBoostingQuantileRegressor
from .learning import RandomForestRegressor
from .space import Space
from .utils import create_result


def _tree_minimize(func, dimensions, base_estimator, n_calls,
                   n_points, n_random_starts, specs, x0=None, y0=None,
                   random_state=None, acq="EI", xi=0.01, kappa=1.96,
                   verbose=False, callback=None):

    rng = check_random_state(random_state)
    space = Space(dimensions)

    # Initialize with provided points (x0 and y0) and/or random points
    if x0 is None:
        x0 = []
    elif not isinstance(x0[0], list):
        x0 = [x0]

    if not isinstance(x0, list):
        raise ValueError("`x0` should be a list, but got %s" % type(x0))

    n_init_func_calls = len(x0) if y0 is None else 0
    n_total_init_calls = n_random_starts + n_init_func_calls

    if n_calls <= 0:
        raise ValueError("Expected `n_calls` > 0, got %d" % n_calls)

    if n_random_starts < 0:
        raise ValueError(
            "Expected `n_random_starts` >= 0, got %d" % n_random_starts)

    if n_random_starts == 0 and not x0:
        raise ValueError("Either set `n_random_starts` > 0, or provide `x0`")

    if n_calls < n_total_init_calls:
        raise ValueError(
            "Expected `n_calls` >= %d, got %d" % (n_total_init_calls, n_calls))

    callbacks = check_callback(callback)
    if verbose:
        callbacks.append(VerboseCallback(
            n_init=n_init_func_calls, n_random=n_random_starts,
            n_total=n_calls))

    if y0 is None and x0:
        y0 = []
        for i, x in enumerate(x0):
            y0.append(func(x))

            if callbacks:
                curr_res = create_result(x0[:i + 1], y0, space, rng, specs)
                for c in callbacks:
                    c(curr_res)
    elif x0:
        if isinstance(y0, Iterable):
            y0 = list(y0)
        elif isinstance(y0, numbers.Number):
            y0 = [y0]
        else:
            raise ValueError(
                "`y0` should be an iterable or a scalar, got %s" % type(y0))
        if len(x0) != len(y0):
            raise ValueError("`x0` and `y0` should have the same length")
        if not all(map(np.isscalar, y0)):
            raise ValueError("`y0` elements should be scalars")
    else:
        y0 = []

    # Random function evaluations.
    X_rand = space.rvs(n_samples=n_random_starts, random_state=rng)
    Xi = x0 + X_rand
    yi = y0

    for i, x in enumerate(X_rand):
        yi.append(func(x))

        if callbacks:
            curr_res = create_result(
                x0 + X_rand[:i + 1], yi, space, rng, specs)
            for c in callbacks:
                c(curr_res)

    if np.ndim(yi) != 1:
        raise ValueError("`func` should return a scalar")

    # Tree-based optimization loop
    models = []
    n_model_iter = n_calls - n_total_init_calls
    for i in range(n_model_iter):
        rgr = clone(base_estimator)
        rgr.fit(space.transform(Xi), yi)
        models.append(rgr)

        # `rgr` predicts constants for each leaf which means that the EI
        # has zero gradient over large distances. As a result we can not
        # use gradient based optimizers like BFGS, so using random sampling
        # for the moment.
        X = space.transform(space.rvs(n_samples=n_points,
                                      random_state=rng))
        values = _gaussian_acquisition(
            X=X, model=rgr, y_opt=np.min(yi), method=acq,
            xi=xi, kappa=kappa)
        next_x = X[np.argmin(values)]
        next_x = space.inverse_transform(next_x.reshape((1, -1)))[0]

        yi.append(func(next_x))
        Xi.append(next_x)

        if callbacks:
            curr_res = create_result(Xi, yi, space, rng, specs)
            for c in callbacks:
                c(curr_res)

    return create_result(Xi, yi, space, rng, specs, models)


def gbrt_minimize(func, dimensions, base_estimator=None, n_calls=100,
                  n_points=1000, n_random_starts=10, x0=None, y0=None,
                  n_jobs=1, random_state=None, acq="EI", xi=0.01, kappa=1.96,
                  verbose=False, callback=None):
    """Sequential optimization using gradient boosted trees.

    Gradient boosted regression trees are used to model the (very)
    expensive to evaluate function `func`. The model is improved
    by sequentially evaluating the expensive function at the next
    best point. Thereby finding the minimum of `func` with as
    few evaluations as possible.

    The total number of evaluations, `n_calls`, are performed like the
    following. If `x0` is provided but not `y0`, then the elements of `x0`
    are first evaluated, followed by `n_random_starts` evaluations.
    Finally, `n_calls - len(x0) - n_random_starts` evaluations are
    made guided by the surrogate model. If `x0` and `y0` are both
    provided then `n_random_starts` evaluations are first made then
    `n_calls - n_random_starts` subsequent evaluations are made
    guided by the surrogate model.

    Parameters
    ----------
    * `func` [callable]:
        Function to minimize. Should take a array of parameters and
        return the function values.

    * `dimensions` [list, shape=(n_dims,)]:
        List of search space dimensions.
        Each search dimension can be defined either as

        - a `(upper_bound, lower_bound)` tuple (for `Real` or `Integer`
          dimensions),
        - a `(upper_bound, lower_bound, "prior")` tuple (for `Real`
          dimensions),
        - as a list of categories (for `Categorical` dimensions), or
        - an instance of a `Dimension` object (`Real`, `Integer` or
          `Categorical`).

    * `base_estimator` [`GradientBoostingQuantileRegressor`]:
        The regressor to use as surrogate model

    * `n_calls` [int, default=100]:
        Number of calls to `func`.

    * `n_random_starts` [int, default=10]:
        Number of evaluations of `func` with random initialization points
        before approximating the `func` with `base_estimator`.

    * `n_points` [int, default=1000]:
        Number of points to sample when minimizing the acquisition function.

    * `x0` [list, list of lists or `None`]:
        Initial input points.

        - If it is a list of lists, use it as a list of input points.
        - If it is a list, use it as a single initial input point.
        - If it is `None`, no initial input points are used.

    * `y0` [list, scalar or `None`]:
        Evaluation of initial input points.

        - If it is a lists, then it corresponds to evaluations of the function
          at each element of `x0` : the i-th element of `y0` corresponds
          to the function evaluated at the i-th element of `x0`.
        - If it is a scalar, then it corresponds to the evaluation of the
          function at `x0`.
        - If it is None and `x0` is provided, then the function is evaluated
          at each element of `x0`.

    * `n_jobs` [int, default=1]:
        The number of jobs to run in parallel for `fit`.
        If -1, then the number of jobs is set to the number of cores.

    * `random_state` [int, RandomState instance, or None (default)]:
        Set random state to something other than None for reproducible
        results.

    * `acq` [string, default=`"LCB"`]:
        Function to minimize over the forest posterior. Can be either

        - `"LCB"` for lower confidence bound,
        - `"EI"` for expected improvement,
        - `"PI"` for probability of improvement.

    * `xi` [float, default=0.01]:
        Controls how much improvement one wants over the previous best
        values. Used when the acquisition is either `"EI"` or `"PI"`.

    * `kappa` [float, default=1.96]:
        Controls how much of the variance in the predicted values should be
        taken into account. If set to be very high, then we are favouring
        exploration over exploitation and vice versa.
        Used when the acquisition is `"LCB"`.

    * `verbose` [boolean, default=False]:
        Control the verbosity. It is advised to set the verbosity to True
        for long optimization runs.

    * `callback` [callable, list of callables, optional]
        If callable then `callback(res)` is called after each call to `func`.
        If list of callables, then each callable in the list is called.

    Returns
    -------
    * `res` [`OptimizeResult`, scipy object]:
        The optimization result returned as a OptimizeResult object.
        Important attributes are:

        - `x` [list]: location of the minimum.
        - `fun` [float]: function value at the minimum.
        - `models`: surrogate models used for each iteration.
        - `x_iters` [list of lists]: location of function evaluation for each
           iteration.
        - `func_vals` [array]: function value for each iteration.
        - `space` [Space]: the optimization space.
        - `specs` [dict]`: the call specifications.
        - `rng` [RandomState instance]: State of the random state
           at the end of minimization.

        For more details related to the OptimizeResult object, refer
        http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html
    """
    # Save call args
    specs = {"args": copy.copy(inspect.currentframe().f_locals),
             "function": inspect.currentframe().f_code.co_name}

    # Check params
    rng = check_random_state(random_state)

    # Default estimator
    if base_estimator is None:
        gbrt = GradientBoostingRegressor(n_estimators=30, loss='quantile')
        base_estimator = GradientBoostingQuantileRegressor(base_estimator=gbrt,
                                                           n_jobs=n_jobs,
                                                           random_state=rng)

    return _tree_minimize(func, dimensions, base_estimator,
                          n_calls=n_calls,
                          n_points=n_points, n_random_starts=n_random_starts,
                          x0=x0, y0=y0, random_state=random_state, xi=xi,
                          kappa=kappa, acq=acq, specs=specs, callback=callback)

    return res


def forest_minimize(func, dimensions, base_estimator='et', n_calls=100,
                    n_points=1000, n_random_starts=10, x0=None, y0=None,
                    n_jobs=1, random_state=None, acq="EI", xi=0.01, kappa=1.96,
                    verbose=False, callback=None):
    """Sequential optimisation using decision trees.

    A tree based regression model is used to model the expensive to evaluate
    function `func`. The model is improved by sequentially evaluating
    the expensive function at the next best point. Thereby finding the
    minimum of `func` with as few evaluations as possible.

    The total number of evaluations, `n_calls`, are performed like the
    following. If `x0` is provided but not `y0`, then the elements of `x0`
    are first evaluated, followed by `n_random_starts` evaluations.
    Finally, `n_calls - len(x0) - n_random_starts` evaluations are
    made guided by the surrogate model. If `x0` and `y0` are both
    provided then `n_random_starts` evaluations are first made then
    `n_calls - n_random_starts` subsequent evaluations are made
    guided by the surrogate model.

    Parameters
    ----------
    * `func` [callable]:
        Function to minimize. Should take a array of parameters and
        return the function values.

    * `dimensions` [list, shape=(n_dims,)]:
        List of search space dimensions.
        Each search dimension can be defined either as

        - a `(upper_bound, lower_bound)` tuple (for `Real` or `Integer`
          dimensions),
        - a `(upper_bound, lower_bound, "prior")` tuple (for `Real`
          dimensions),
        - as a list of categories (for `Categorical` dimensions), or
        - an instance of a `Dimension` object (`Real`, `Integer` or
          `Categorical`).

    * `base_estimator` [string or `Regressor`, default=`"et"`]:
        The regressor to use as surrogate model. Can be either

        - `"rf"` for random forest regressor
        - `"et"` for extra trees regressor
        - instance of regressor with support for `return_std` in its predict
          method

        The predefined models are initilized with good defaults. If you
        want to adjust the model parameters pass your own instance of
        a regressor which returns the mean and standard deviation when
        making predictions.

    * `n_calls` [int, default=100]:
        Number of calls to `func`.

    * `n_random_starts` [int, default=10]:
        Number of evaluations of `func` with random initialization points
        before approximating the `func` with `base_estimator`.

    * `n_points` [int, default=1000]:
        Number of points to sample when minimizing the acquisition function.

    * `x0` [list, list of lists or `None`]:
        Initial input points.

        - If it is a list of lists, use it as a list of input points.
        - If it is a list, use it as a single initial input point.
        - If it is `None`, no initial input points are used.

    * `y0` [list, scalar or `None`]:
        Evaluation of initial input points.

        - If it is a list, then it corresponds to evaluations of the function
          at each element of `x0` : the i-th element of `y0` corresponds
          to the function evaluated at the i-th element of `x0`.
        - If it is a scalar, then it corresponds to the evaluation of the
          function at `x0`.
        - If it is None and `x0` is provided, then the function is evaluated
          at each element of `x0`.

    * `n_jobs` [int, default=1]:
        The number of jobs to run in parallel for `fit` and `predict`.
        If -1, then the number of jobs is set to the number of cores.

    * `random_state` [int, RandomState instance, or None (default)]:
        Set random state to something other than None for reproducible
        results.

    * `acq` [string, default=`"LCB"`]:
        Function to minimize over the forest posterior. Can be either

        - `"LCB"` for lower confidence bound,
        - `"EI"` for expected improvement,
        - `"PI"` for probability of improvement.

    * `xi` [float, default=0.01]:
        Controls how much improvement one wants over the previous best
        values. Used when the acquisition is either `"EI"` or `"PI"`.

    * `kappa` [float, default=1.96]:
        Controls how much of the variance in the predicted values should be
        taken into account. If set to be very high, then we are favouring
        exploration over exploitation and vice versa.
        Used when the acquisition is `"LCB"`.

    * `verbose` [boolean, default=False]:
        Control the verbosity. It is advised to set the verbosity to True
        for long optimization runs.

    * `callback` [callable, optional]
        If provided, then `callback(res)` is called after call to func.

    Returns
    -------
    * `res` [`OptimizeResult`, scipy object]:
        The optimization result returned as a OptimizeResult object.
        Important attributes are:

        - `x` [list]: location of the minimum.
        - `fun` [float]: function value at the minimum.
        - `models`: surrogate models used for each iteration.
        - `x_iters` [list of lists]: location of function evaluation for each
           iteration.
        - `func_vals` [array]: function value for each iteration.
        - `space` [Space]: the optimization space.
        - `specs` [dict]`: the call specifications.

        For more details related to the OptimizeResult object, refer
        http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html
    """
    # Save call args + rng
    specs = {"args": copy.copy(inspect.currentframe().f_locals),
             "function": inspect.currentframe().f_code.co_name}

    # Check params
    rng = check_random_state(random_state)

    # Default estimator
    if isinstance(base_estimator, str):
        if base_estimator not in ("rf", "et"):
            raise ValueError(
                "Valid values for the base_estimator parameter"
                " are: 'rf' or 'et', not '%s'" % base_estimator)

        if base_estimator == "rf":
            base_estimator = RandomForestRegressor(n_estimators=100,
                                                   min_samples_leaf=3,
                                                   n_jobs=n_jobs,
                                                   random_state=rng)

        elif base_estimator == "et":
            base_estimator = ExtraTreesRegressor(n_estimators=100,
                                                 min_samples_leaf=3,
                                                 n_jobs=n_jobs,
                                                 random_state=rng)

    else:
        if not is_regressor(base_estimator):
            raise ValueError("The base_estimator parameter has to either"
                             " be a string or a regressor instance."
                             " '%s' is neither." % base_estimator)

    return _tree_minimize(func, dimensions, base_estimator,
                          n_calls=n_calls,
                          n_points=n_points, n_random_starts=n_random_starts,
                          specs=specs, x0=x0, y0=y0, random_state=random_state,
                          acq=acq, xi=xi, kappa=kappa, verbose=verbose,
                          callback=callback)
