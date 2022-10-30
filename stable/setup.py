from setuptools import setup, find_packages
from os.path import abspath, dirname, join


README_MD = open(join(dirname(abspath(__file__)), "c:\\Users\\HP\\Documents\\Software-Projects\\Python\\Python-Projects\\FooDB\\README.md")).read()

setup(
    name="foodb",
    version="1.0.0",
    packages=find_packages(),
    description="FooDB is a small, open-source, extendable, and fully customizable JSON database written in Python using the json and os modules.",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/SteveJobs91/FooDB",
    author_name="softwaredeveloper12",
    author_email="devaanshdudeja@gmail.com",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only"
    ],
    keywords="database, extendable, customizable, fast database, web development, GUI, app development, database"
)