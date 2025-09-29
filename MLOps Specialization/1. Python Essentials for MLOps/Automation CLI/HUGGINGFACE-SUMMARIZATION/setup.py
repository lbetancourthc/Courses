from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    requirements = [line for line in f.read().split("\n")]

setup(
    name="summarize",
    description="Demo Python CLI tool to summarize text using HuggingFace",
    packages=find_packages(),
    author="Landneyker B.",
    author_email="lbetancourthc@unal.edu.co",
    entry_points="""
    [console_scripts]
    summarize=summarize.main:main
    """,
    install_requires=requirements,
    version="0.0.1",
)