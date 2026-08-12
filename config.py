import configparser
import json
import logging
import jsonschema

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None
        try:
            self.config = self._parse_config()
        except Exception as e:
            logger.error(f"Failed to parse config file: {e}")

    def _parse_config(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                jsonschema.validate(instance=config, schema={'type': 'object'})
                return config
        except FileNotFoundError:
            logger.error(f"Config file not found: {self.config_file}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON config file: {e}")
            raise
        except jsonschema.exceptions.ValidationError as e:
            logger.error(f"Invalid JSON schema: {e}")
            raise

    def get_config(self):
        return self.config

def parse_config(config_file):
    return ConfigParser(config_file)

def load_json_schema(schema_file):
    try:
        with open(schema_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"JSON schema file not found: {schema_file}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON schema file: {e}")
        raise

def validate_config(config, schema):
    try:
        jsonschema.validate(instance=config, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"Invalid JSON schema: {e}")
        raise

def main():
    config_file = "config.json"
    schema_file = "schema.json"
    try:
        config = parse_config(config_file).get_config()
        schema = load_json_schema(schema_file)
        validate_config(config, schema)
        print(config)
    except Exception as e:
        logger.error(f"Failed to parse config file: {e}")

if __name__ == "__main__":
    main()