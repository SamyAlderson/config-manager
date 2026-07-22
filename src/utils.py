# Utilities for config management

import os
import json
import yaml
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def load_config(filename):
    """
    Load config from JSON or YAML file.

    :param filename: Path to config file
    :return: Config data (dict)
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Config file '{filename}' not found")

    # Try to load JSON config
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If JSON fails, try YAML
        logging.info(f"Failed to load JSON config, trying YAML")
        try:
            with open(filename, 'r') as file:
                return yaml.safe_load(file)
        except yaml.YAMLError:
            raise ValueError(f"Invalid config file format: {filename}")

def validate_config(config):
    """
    Validate config data against schema.

    :param config: Config data (dict)
    :return: Validated config data (dict)
    """
    # For now, just return the config as-is
    # In the future, we can add a schema validation library like jsonschema
    return config