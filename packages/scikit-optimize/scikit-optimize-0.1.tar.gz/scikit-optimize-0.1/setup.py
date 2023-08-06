try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='scikit-optimize',
      version='0.1',
      description='Sequential model-based optimization toolbox.',
      long_description=('Scikit-Optimize, or skopt, is a simple and efficient'
                        ' library for sequential model-based optimization,'
                        ' accessible to everybody and reusable in various'
                        ' contexts.'),
      url='https://scikit-optimize.github.io/',
      license='BSD',
      author='The scikit-optimize contributors',
      packages=['skopt', 'skopt.learning'],
      install_requires=["numpy", "scipy", "scikit-learn>=0.18dev", "cython",
                        "matplotlib"]
      )
