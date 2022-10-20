from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'mathplug',
    version = '0.0.1',
    description = 'A lightweight Python package which supplies simple math functions.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Jordan Welsman',
    author_email = 'jordan.welsman@outlook.com',
    url = 'https://github.com/JordanWelsman/mathplug/',
    py_modules = ["__init__", "add", "divide", "hello_world", "multiply", "subtract"],
    classifiers = ["Development Status :: 2 - Pre-Alpha", "Intended Audience :: Other Audience", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", "Programming Language :: Python :: 3.9", "Topic :: Scientific/Engineering :: Mathematics"],
    package_dir = {'': 'mathplug'},
    extras_require = {
        "dev": [
            "pytest >= 7.1",
        ],
    },
)