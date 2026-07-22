# tests/test_config.py

import pytest
from jsonschema import ValidationError
from config import Config
from config import ConfigError

def test_config_empty():
    # Test creating an empty config
    config = Config()
    assert config.sections() == {}
    assert config.get('foo', 'bar') is None

def test_config_invalid_schema():
    # Test creating a config with invalid schema
    with pytest.raises(ValidationError):
        Config(schema={'type': 'invalid'})

def test_config_load():
    # Test loading config from file
    config = Config('config.json')
    assert config.sections() == {'foo': {'bar': 'baz'}}
    assert config.get('foo', 'bar') == 'baz'

def test_config_get():
    # Test getting a config value
    config = Config('config.json')
    assert config.get('foo', 'bar') == 'baz'

def test_config_set():
    # Test setting a config value
    config = Config()
    config.set('foo', 'bar', 'baz')
    assert config.get('foo', 'bar') == 'baz'

def test_config_save():
    # Test saving config to file
    config = Config('config.json')
    config.set('foo', 'bar', 'baz')
    config.save()

def test_config_invalid_path():
    # Test loading config from invalid path
    with pytest.raises(FileNotFoundError):
        Config('nonexistent.json')

def test_config_invalid_json():
    # Test loading config from invalid JSON
    with pytest.raises(ValidationError):
        Config('invalid.json')