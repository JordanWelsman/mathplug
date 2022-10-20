from setuptools import setup

setup(
    name = 'mathplug',
    version = '0.0.1',
    description = 'A lightweight Python package which supplies simple math functions.',
    long_description = 'mathplug is a lightweight Python package which supplies simple math functions. It was primarily designed as an excuse to learn how to publish a Python package. Secondarily, this will give me an opportunity to learn some of the more complicated mathematical equations since I somehow skipped that part. In the future, you\'ll be able to install and import this software into your notebook or Python file and use it to add some numbers together. How exciting!',
    author = 'Jordan Welsman',
    author_email = 'jordan.welsman@outlook.com',
    url = 'https://github.com/JordanWelsman/mathplug/',
    py_modules = ["__init__", "add", "divide", "hello_world", "multiply", "subtract"],
    classifiers = ["Development Status :: 2 - Pre-Alpha", "Intended Audience :: Other Audience", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", "Programming Language :: Python :: 3.9", "Topic :: Scientific/Engineering :: Mathematics"],
    package_dir = {'': 'mathplug'}
)