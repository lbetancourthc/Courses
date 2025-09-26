# Python for MLOps

## Key Terms 1

**Azure CLI (Azure Command-Line Interface):** A command-line tool that allows management and interaction with Azure services and resources.

```python
mport azure.cli.core

cli = azure.cli.core.AzureCli()
cli.invoke(["storage", "account", "list"])
```

**Azure ML (Azure Machine Learning) Studio:** A cloud-based environment for machine learning development and deployment.

```python
from azureml.core import Workspace

ws = Workspace.create(name='myworkspace',
                     subscription_id='...',
                     resource_group='myresourcegroup',
                     location='eastus')
```

**Transformers:** A Hugging Face library for natural language processing tasks.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love this course!")
print(result)
```

**Datasets:** A Hugging Face library for loading datasets.

```python
from datasets import load_dataset

dataset = load_dataset("glue", "mrpc")
train_dataset = dataset["train"]
print(len(train_dataset))
```

**Open Datasets:** An Azure resource for loading curated public datasets.

```python
from azureml.opendatasets import PublicHolidays

holidays = PublicHolidays()
holidays_df = holidays.to_pandas_dataframe()
print(holidays_df.head())
```

### Lesson Reflection

**Summary of Lesson:**
This lesson provided an overview of working with APIs and SDKs for machine learning tasks. It covered installing and using tools like the Azure CLI and SDKs like Hugging Face Transformers and Datasets. It also showed how to connect these to cloud services.

**Top 3 Key Points:**
* APIs and SDKs allow interacting with ML services programmatically
* Azure provides CLI tools, SDKs, and cloud services for ML
* Hugging Face offers libraries for NLP and loading datasets

**Reflection Questions:**
* What benefits do APIs and SDKs provide over manual point-and-click interaction?
* How could the Azure CLI and SDK help automate an ML workflow?
* What Hugging Face libraries seem most relevant to your work?
* What challenges have you faced working with cloud-based ML services?
* How might you improve efficiency by switching manual workflows to APIs?

**Challenge Exercises:**
* Install and configure the Azure CLI on your machine
* Load a dataset from Hugging Face and analyze it
* Create an Azure Machine Learning workspace using Python
* Build a classifier with Hugging Face Transformers
* Compare Azure tools to other cloud providers like GCP and AWS

## Key Terms 2

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
print(f"Second argument: {sys.argv[2]}")
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
    ]
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

