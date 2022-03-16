
import setuptools

with open("README.md", "r") as fh:
long_description = fh.read()

setuptools.setup(
    name="module_distribution",
    version=0.0.1,
    author=taisei,
    author_email=taiseiyo11@gmail.com,
    description=test,
    long_description=test,

    long_description_content_type="text/markdown",
    url="https://github.com/taiseiyo/module_distribution",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.8',)
