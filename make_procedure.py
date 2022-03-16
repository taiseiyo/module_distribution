#!/usr/bin/env python
import argparse
import sys
import os


def arg_parse():
    parser = argparse.ArgumentParser(description="argparse")
    parser.add_argument('-c', '--command', action="store_true",
                        help='implement as a command')
    return parser.parse_args()


def beginning_preparation():
    if(not os.path.exists(os.getcwd() + "/README.md")):
        f = open("README.md", "w")
        f.write("")

    try:
        setting = {
            "author": input("Enter author name: "),
            "email": input("Enter email address: "),
            "project_name": input("Enter project name: "),
            "version": input("Enter program version: "),
            "description": input("Enter a brief description: ")
        }
        return setting

    except:
        sys.exit()


def main():
    setting = beginning_preparation()
    args = arg_parse()
    setup_content = """
import setuptools

with open("README.md", "r") as fh:
long_description = fh.read()

setuptools.setup(
    name="module_distribution",
    """ + f"\tversion = {setting['version']},\n" \
        + f"\tauthor = {setting['author']},\n" \
        + f"\tauthor_email = {setting['email']},\n" \
        + f"\tdescription = {setting['description']},\n" \
        + f"\tlong_description = {setting['description']},\n"\
        + """
    long_description_content_type = "text/markdown",
    url = "",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.8',)"""

    if(args.command):
        setup_content = setup_content[0:-1] + \
            "\n\tentry_points = {\n" + \
            f"\tconsole_scripts': ['{setting['project_name']} = {setting['project_name']}.{setting['project_name']}:main']" + "})"

    try:
        os.mkdir(setting["project_name"])
        open(setting["project_name"] + "/__init__.py", "w").write("")
        open(setting["project_name"] + "/" +
             setting["project_name"]+".py", "w").write("")
        open("setup.py", "w").write(setup_content)

    except FileExistsError:
        print("already file or directory exist. enjoy!")

    print(setup_content)


main()
