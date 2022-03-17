#!/usr/bin/env python
import argparse
import sys
import os


def arg_parse():
    parser = argparse.ArgumentParser(description="argparse")
    parser.add_argument('-c', '--command', action="store_true",
                        help='implement as a command')
    return parser.parse_args()


def setting_vars():
    try:
        setting = {
            "author": input("Enter author name: "),
            "email": input("Enter email address: "),
            "project_name": input("Enter project name: "),
            "version": input("Enter program version: "),
            "description": input("Enter a brief description: ")
        }
        explanatory_text = f"\n{4 * ' '}name = '{setting['project_name']}', \n{4 * ' '}"
        for key, var in setting.items():
            explanatory_text = explanatory_text + \
                f"{key} = '{var}', \n{4 * ' '}"
        return explanatory_text, setting

    except:
        sys.exit()


def setting_readme(setting):
    if(not os.path.exists(os.getcwd() + "/README.md")):
        f = open("README.md", "w")
        f.write(
            f"# install\n`pip install git+https://github.com/{setting['author']}/" + os.path.basename(os.getcwd())+"`")


def main():
    explanatory_text, setting = setting_vars()
    setting_readme(setting)
    args = arg_parse()
    setup_content = """
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(""" + explanatory_text + """
    long_description_content_type = "text/markdown",
    url = "https://github.com/"""+setting["author"]+"/"+setting["project_name"] + """",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.8',)
"""

    if(args.command):
        setup_content = setup_content[0:-1] + \
            "\n    entry_points = {\n" + \
            f"\tconsole_scripts': ['{setting['project_name']} = {setting['project_name']}.{setting['project_name']}:main']" + "})"

    try:
        os.mkdir(setting["project_name"])
        open(setting["project_name"] + "/__init__.py", "w").write("")
        open("setup.py", "w").write(setup_content)

    except FileExistsError:
        print("already file or directory exist. enjoy!")


main()
