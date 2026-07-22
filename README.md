# config-manager
Simple config management tool for devops

## What/Why

config-manager is designed to provide a basic yet robust config management tool for devops use cases. It supports section-based and key-value config parsing, making it suitable for a variety of applications.

## Install

To use config-manager, follow these steps:

1. Clone the repository: `git clone https://github.com/samyalder/ config-manager.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the tool: `python src/main.py`

## Usage

config-manager can be used as a command-line tool to parse and manage config files. For example:

```bash
# Parse a config file
$ python src/main.py --config /path/to/config.ini
```

## Build from Source

To build config-manager from source, follow these steps:

1. Install Python 3.x and pip
2. Clone the repository: `git clone https://github.com/samyalder/config-manager.git`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the tool: `python src/main.py`

## Project Structure

The project structure is as follows:

* `README.md`: Project description
* `config.py`: Config file parser
* `tests/test_config.py`: Unit tests for config module
* `setup.py`: Project setup and dependency management
* `src/main.py`: Main entry point
* `src/utils.py`: Utility functions

## License

config-manager is released under the MIT License.

## Dependencies

* `pytest`
* `jsonschema`

## Features

* Config file parsing
* Section-based config
* Key-value config