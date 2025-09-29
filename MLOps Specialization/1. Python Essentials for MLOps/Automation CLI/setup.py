from setuptools import setup, find_packages


setup(
    name="jformat",
    version="0.0.1",
    description="Format files to stdout",
    install_requires = ["click", "colorama"],
    entry_points="""
    [console_scripts]
    jformat=jformat.main:main
    """,
    author="Landneyker B.",
    author_email="lbetancourthc@unal.edu.co",
    packages=find_packages()
)

