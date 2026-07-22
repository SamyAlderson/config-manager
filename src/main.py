# src/main.py
import argparse
import jsonschema
from config import Config

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Config Manager')
    parser.add_argument('-c', '--config', help='Path to config file')
    parser.add_argument('-s', '--section', help='Section to operate on')
    parser.add_argument('-k', '--key', help='Key to access')
    parser.add_argument('-v', '--value', help='Value to set')
    args = parser.parse_args()
    return args

def main():
    """Main entry point."""
    args = parse_args()
    config = Config(args.config)
    if args.section:
        section = config.get_section(args.section)
        if section:
            if args.key:
                value = section.get(args.key)
                print(f"{args.key}: {value}")
            elif args.value:
                section[args.key] = args.value
                config.save()
                print("Value set successfully")
            else:
                print("Please provide a key or value")
        else:
            print("Section not found")
    elif args.key and args.value:
        config.set(args.key, args.value)
        config.save()
        print("Value set successfully")
    elif args.key:
        value = config.get(args.key)
        print(f"{args.key}: {value}")
    else:
        print("Please provide a config file, section, key, or value")

if __name__ == '__main__':
    main()