from setuptools import setup

requires = [
    'click==6.6',
    'numpy==1.11.1',
    'pandas==0.18.1'
]

tests_require = []

classifiers = [
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 2.7',
    'Environment :: Console',
    'Development Status :: 4 - Beta',
    'Topic :: Scientific/Engineering',
    'Intended Audience :: Science/Research'
]

setup(
    name='prms-python',
    description='''
PRMS-Python provides a Python interface to PRMS data files and for running
PRMS simulations. This module tries to improve the management of PRMS
simulation data while also providing useful "pythonic" tools to do
scenario-based PRMS simulations. By "scenario-based" modeling we mean, for
example, parameter sensitivity analysis, where each "scenario" is an
iterative perturbation of one or many parameters. Another example
"scenario-based" modeling exercise would be climate scenario modeling: what
will happen to modeled outputs if the input meteorological data were to change?
    ''',
    license='BSD3',
    version='0.1',
    classifiers=classifiers,
    py_modules=['prms_python'],
    install_requires=requires,
    tests_require=tests_require,
    package_data={'prms_python': ['models/lbcd/*']},
    include_package_data=True,
    entry_points='''
        [console_scripts]
        prmspy=prms_python.scripts.prmspy:prmspy
    '''
)
