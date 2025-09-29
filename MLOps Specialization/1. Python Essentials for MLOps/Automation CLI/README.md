# Automation with CLI

## Key Terms

**Click:** A Python package for building command line interfaces.
```python
import click

@click.command()
@click.option('--count', default=1)
def hello(count):
    for x in range(count):
        click.echo('Hello World!')

if __name__ == '__main__':
    hello()
```

**ArgParse:** A Python module for parsing command-line arguments.
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', action='store_true')
args = parser.parse_args()

if args.verbosity:
    print("Verbose mode enabled")
```

**sys.argv:** A Python module containing command line arguments.
```python
import sys

print(f"Script name: {sys.argv[0]}")
print(f"First argument: {sys.argv[1]}")
print(f"Second argument: {sys.argv[2]}
```

**Setuptools:** A package for building and distributing Python projects.
```python
from setuptools import setup

setup(
    name='mypackage',
    version='1.0',
    install_requires=['requests', 'click']
)
```

**Entry points:** Definitions linking scripts to functions in Setuptools.
```python
from setuptools import setup

setup(
  #...,
  entry_points = {
    'console_scripts': [
      'myscript = mypackage.mymodule:main_func',
  }
)
```

### Lesson Reflection
**Summary of Lesson:**
This lesson covered building automation by creating reusable command-line interface (CLI) tools in Python. It showed parsing command arguments, handling flags, declaring dependencies, packaging projects, and using frameworks like Click and ArgParse.

**Top 3 Key Points:**
* CLI tools allow automating tasks instead of manual work
* Frameworks like Click simplify building robust CLIs
* Packaging projects enables sharing and reusing CLIs

**Reflection Questions:**
* What manual tasks could you automate with a custom CLI tool?
* How might ArgParse vs Click affect your CLI tool design?
* What dependencies would your automation tools need?
* How could you make your CLIs easy for others to install and run?
* Where could CLI automation provide the most value in your role?

**Challenge Exercises:**
* Build a CLI to reformat a JSON file
* Create a CLI tool to preprocess data
* Package a project with dependencies, help text, and commands
* Automate an ML workflow by chaining multiple CLIs
* Research best practices for Python CLI project structure

