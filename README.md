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

>:memo: **Note:** The PyPI shield will not work until a PyPI package is uploaded.

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
  - [`0.0.1`](#001)
  - [`0.0.2` (Planned)](#002-planned)
- [Credits](#credits)
- [License](#license)

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

## `0.0.1`

- Simple math functions defined
- Package files created
- Created test files & tested with `pytest`

## `0.0.2` (Planned)
- _Package published to `PyPI`_

# Credits

`mathplug` was created, developed, and is currently maintained by **Jordan Welsman**.

# License

`mathplug` is developed and distributed under the `MIT` license.
>See `LICENSE.md` for more details.
