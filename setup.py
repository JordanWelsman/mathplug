# Module imports
import sys
import os
from setuptools import setup

# Terminal formatting
class color:
    DEFAULT =       '\033[39m'
    BLACK =         '\033[30m'
    RED =           '\033[31m'
    GREEN =         '\033[32m'
    YELLOW =        '\033[33m'
    BLUE =          '\033[34m'
    MAGENTA =       '\033[35m'
    CYAN =          '\033[36m'
    LIGHTGRAY =     '\033[37m'
    DARKGRAY =      '\033[90m'
    LIGHTRED =      '\033[91m'
    LIGHTGREEN =    '\033[92m'
    LIGHTYELLOW =   '\033[93m'
    LIGHTBLUE =     '\033[94m'
    LIGHTMAGENTA =  '\033[95m'
    LIGHTCYAN =     '\033[96m'
    WHITE =         '\033[97m'


# Python 3 assertion
assert sys.version_info.major >= 3, f"{color.LIGHTRED}Python version must be 3 or higher."

# Arguments
args = sys.argv
num_args = len(args)
program_name = args[0]
version = "0.0.1"
run_pytest_after_setup = False

def run_program():
    if (num_args > 1): # if arguments are passed
        arg = args[1]
        match arg:
            case '-v' | '--version': # display version number
                print(f"Running {color.DARKGRAY}mathplug{color.DEFAULT} version {color.GREEN}v{version}{color.DEFAULT}.")
            case 'bdist_wheel': # create package files
                with open("README.md", "r") as fh:
                    long_description = fh.read()

                setup(
                    name = 'mathplug',
                    version = '0.0.2',
                    description = 'A lightweight Python package which supplies simple math functions.',
                    long_description = long_description,
                    long_description_content_type = 'text/markdown',
                    author = 'Jordan Welsman',
                    author_email = 'jordan.welsman@outlook.com',
                    url = 'https://github.com/JordanWelsman/mathplug/',
                    py_modules = ["__init__", "mathplug", "test_mathplug"],
                    classifiers = ["Development Status :: 2 - Pre-Alpha", "Intended Audience :: Other Audience", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", "Programming Language :: Python :: 3.9", "Topic :: Scientific/Engineering :: Mathematics"],
                    package_dir = {'': 'mathplug'},
                    extras_require = {
                        "dev": [
                            "pytest >= 7.1",
                        ],
                    },
                )
                if run_pytest_after_setup:
                    os.system("pytest")
            case other: # incorrect
                print(f"{color.RED}ERROR: {color.LIGHTRED}argument not recognized:{color.DEFAULT} {other}")
    else:
        print(f"If no arguments are required, use {color.GREEN}<python | python3> <setup.py> <bdist_wheel> {color.DEFAULT} to run setup.")

# Run the program
run_program()
