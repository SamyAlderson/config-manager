# config-manager
Simple config management tool for devops

## What it does

This tool provides a simple way to manage configuration files, parsing them into a structured format for easier use in devops scripts. It supports section-based and key-value config formats. I wrote it because I needed something like this for my own projects.

## Install

You can install it using pip:
```bash
pip install config-manager
```
Or, if you're lazy, just clone the repo and run:
```bash
python setup.py install
```

## Usage

To use it, just import the `Config` class and parse your config file:
```python
from config_manager import Config

config = Config('config.ini')
print(config.section['key'])  # prints the value of 'key' in the 'section' section
```
You can also use the `parse_config()` function to parse a string:
```python
config_str = 'section.key=value'
config = parse_config(config_str)
print(config.section['key'])  # prints 'value'
```
## Build from source

You can build from source by running:
```bash
python setup.py build
```
This will create a `config_manager` package in the `build` directory.

## Run tests

To run the tests, just use:
```bash
python -m unittest discover
```
## Project structure

* `config_manager.py`: main module with the `Config` class
* `config_parser.py`: parser for config files
* `test_config_manager.py`: test suite for the `Config` class
* `setup.py`: setup script for installing and building from source
* `README.md`: this file
* `LICENSE`: MIT license

## License

Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.