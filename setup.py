from setuptools import find_packages, setup

setup(
    name = 'brainfunc',
    packages = find_packages(include=['brainfunc']),
    version = '0.1.0',
    description = 'Extension of the brainf*ck language that supports the use of functions.'
    author = 'Skander Krid',
    author_email = 'kridskander@gmail.com'
    license = 'MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)