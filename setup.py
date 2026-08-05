from setuptools import setup, find_packages

def read_file(filename):
    """Read the contents of a file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError(f"File not found: {filename}")
    except Exception as e:
        print(f"Error reading file: {filename} - {e}")
        raise

def get_version():
    """Get the version number from the README file."""
    try:
        lines = read_file('README.md').splitlines()
        if len(lines) < 2:
            raise ValueError("README file is empty")
        return lines[1].strip()[1:-1]
    except Exception as e:
        print(f"Error getting version: {e}")
        raise

def get_long_description():
    """Get the long description from the README file."""
    try:
        return read_file('README.md')
    except Exception as e:
        print(f"Error getting long description: {e}")
        return ""

setup(
    name='config-manager',
    description='Simple config management tool for devops',
    long_description=get_long_description(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    version=get_version(),
    author='Samy Alderson',
    author_email='samy@alderson.io',
    install_requires=[
        'pytest',
        'jsonschema'
    ],
    url='https://github.com/samyalderson/config-manager',
    license='MIT'
)