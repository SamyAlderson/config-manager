from setuptools import setup, find_packages

def read_file(filename):
    """Read the contents of a file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError(f"File not found: {filename}")

def get_version():
    """Get the version number from the README file."""
    return read_file('README.md').splitlines()[1].strip()[1:-1]

setup(
    name='config-manager',
    description='Simple config management tool for devops',
    long_description=read_file('README.md'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[],
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