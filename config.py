# config.py

import configparser
import logging
import jsonschema

# Use logging module to handle errors and warnings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConfigParser:
    """Simple config file parser"""
    
    def __init__(self, config_file):
        # Assume config file is a JSON file
        self.config_file = config_file
        self.config = self._parse_config()
        
    def _parse_config(self):
        try:
            with open(self.config_file, 'r') as f:
                # Load JSON config file
                config = json.load(f)
                # Validate JSON schema
                jsonschema.validate(instance=config, schema={'type': 'object'})
                return config
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON config file: {e}")
            raise
        except FileNotFoundError:
            logger.error(f"Config file not found: {self.config_file}")
            raise
        except jsonschema.exceptions.ValidationError as e:
            logger.error(f"Invalid JSON schema: {e}")
            raise
    
    def get_config(self):
        return self.config

def parse_config(config_file):
    """Parse config file and return a ConfigParser object"""
    return ConfigParser(config_file)

# Example usage
if __name__ == "__main__":
    config_file = "config.json"
    parser = parse_config(config_file)
    config = parser.get_config()
    print(config)