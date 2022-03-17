
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'sample', 
    author = 'taiseiyo', 
    email = 'taiseiyo11@gmail.com', 
    project_name = 'sample', 
    version = '0.0.1', 
    description = 'sample test', 
    
    long_description_content_type = "text/markdown",
    url = "https://github.com/taiseiyo/sample",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.8',)
