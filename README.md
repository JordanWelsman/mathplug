```ascii
 __   __  _______  _______  __   __  _______  ___      __   __  _______ 
|  |_|  ||   _   ||       ||  | |  ||       ||   |    |  | |  ||       |
|       ||  |_|  ||_     _||  |_|  ||    _  ||   |    |  | |  ||    ___|
|       ||       |  |   |  |       ||   |_| ||   |    |  |_|  ||   | __ 
|       ||       |  |   |  |       ||    ___||   |___ |       ||   ||  |
| ||_|| ||   _   |  |   |  |   _   ||   |    |       ||       ||   |_| |
|_|   |_||__| |__|  |___|  |__| |__||___|    |_______||_______||_______|
```

![PyPI](https://img.shields.io/pypi/v/mathplug)
![GitHub](https://img.shields.io/github/license/JordanWelsman/mathplug)
![GitHub last commit](https://img.shields.io/github/last-commit/JordanWelsman/mathplug)
![GitHub pull requests](https://img.shields.io/github/issues-pr/JordanWelsman/mathplug)
![GitHub followers](https://img.shields.io/github/followers/JordanWelsman?style=social)

# Overview

 `mathplug` is a lightweight Python package which supplies simple math functions. It was primarily designed as an excuse to learn how to publish a Python package. Secondarily, this will give me an opportunity to learn some of the more complicated mathematical equations since I somehow skipped that part. In the future, you'll be able to `install` and `import` this software into your notebook or Python file and use it to add some numbers together. _How exciting!_

# Table of contents

- [Overview](#overview)
- [Table of contents](#table-of-contents)
- [Install & use](#install--use)
  - [Test](#test)
  - [Build](#build)
- [Objectives](#objectives)
- [History](#history)
  - [`0.0.0` (10.21.2022)](#000-10212022)
  - [`0.0.1` (10.25.2022)](#001-10252022)
  - [`0.0.2` (10.25.2022)](#002-10252022)
  - [`0.0.3` (10.26.2020)](#003-10262020)
  - [`0.1.0` (Planned)](#010-planned)
- [Credits](#credits)
- [License](#license)
- [Links](#links)

# Install & use

1. From terminal:
`shell pip install mathplug`
2. From python environment:
`import mathplug`

## Test

1. Clone repository:
`git clone https://github.com/JordanWelsman/mathplug.git`
2. Build module for testing:
`python3 setup.py bdist_wheel`
3. Install module locally:
`pip install -e . dev`
4. Run tests with `PyTest`:
`pytest`

## Build

1. Build module for distribution:
`python3 setup.py bdist_wheel sdist`
2. Push to `PyPI`:
`pip install twine`
`twine upload dist/*`

# Objectives

- Learn how to publish a Python package
- Learn some more complicated math functions

# History

## `0.0.0` (10.21.2022)

- GitHub repositiry created
- Project created
  - Basic `README.md` written

## `0.0.1` (10.25.2022)

- Simple math functions defined
  - `add()`, `divide()`, `hello_world()`, `multiply`, `square_root()`, `square()`, and `subtract()`
- Package files created
  - `setup.py` and `LICENSE.md`
- Created test files & tested with `pytest`
  - `test_add.py`, `test_divide.py`, `test_hello_world.py`, `test_multiply.py`, `test_square_root.py`, `test_square.py`, and `test_subtract.py`
- Package published to `PyPI`
  - [PyPI Project Link](https://pypi.org/project/mathplug/)

## `0.0.2` (10.25.2022)

- Aggregated all functions into one file
  - Functions should be optionally imported with `import mathplug`, not strictly `from mathplug import function`
  - Functions should be accessed with `mathplug.function()`, not `mathplug.file.function`
- Agregated all test files into one file containing all tests
  - Done for ease of use and to clean up file tree
- Incremented version number

## `0.0.3` (10.26.2020)

- More math functions defined
  - `absolute()`, `cube()`, and `exponent()`
- Created tests for new functions & tested with `PyTest`
  - `absolute()`, `cube()`, and `exponent()`
- Incremented version number

## `0.1.0` (Planned)

- _Stable release_
- _Improve Python accessability_

# Credits

`mathplug` was created, developed, and is currently maintained by **Jordan Welsman**.

# License

`mathplug` is developed and distributed under the `MIT` license.
>See `LICENSE.md` for more details.

# Links

:file_folder: [See this project on GitHub](https://github.com/JordanWelsman/mathplug/)

:gift: [See this project on PyPI](https://pypi.org/project/mathplug/)

:cat: [Follow me on GitHub](https://github.com/JordanWelsman/)

:briefcase: [Connect with me on Linkedin](https://linkedin.com/in/JordanWelsman/)

:email: [Send me an email](mailto:jordan.welsman@outlook.com)

:clapper: [Followed tutorial](https://www.youtube.com/watch?v=GIF3LaRqgXo/) by [Mark Smith (@judy2k)](https://twitter.com/judy2k/)