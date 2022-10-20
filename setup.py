from setuptools import setup

setup(
    name = 'mathplug',
    version = '0.0.1',
    description = 'A lightweight Python package which supplies simple math functions.',
    long_description = 'mathplug is a lightweight Python package which supplies simple math functions. It was primarily designed as an excuse to learn how to publish a Python package. Secondarily, this will give me an opportunity to learn some of the more complicated mathematical equations since I somehow skipped that part. In the future, you\'ll be able to install and import this software into your notebook or Python file and use it to add some numbers together. How exciting!',
    py_modules = ["add", "divide", "hello_world", "multiply", "subtract"],
    package_dir = {'': 'mathplug'}
)