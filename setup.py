
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="module_distribution",
    version = '0.0.1',
	author = 'taiseiyo',
	author_email = 'taiseiyo11',
	description = 'sample test',
	long_description = 'sample test',

    long_description_content_type = "text/markdown",
    url = "https://github.com/",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.8',)
