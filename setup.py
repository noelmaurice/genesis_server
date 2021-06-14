#!/usr/bin/env python
import os
import re
from distutils.core import setup


def get_long_description():
    content = ""
    with open("README.md", encoding='utf-8') as FH:
        content = FH.read()
    return content


def get_version():
    version = None
    notes_filepath = "RELEASES_NOTES.md"
    if os.path.exists(notes_filepath):
        with open(notes_filepath) as FH:
            first_line = FH.readline()
            version = re.search("^\#\s+.+\s+(.+)\s+\[", first_line).groups()[0]  # Example: "# v2.5.0 [DEV]"
    return version


def load_requirements(path):
    requirements = []
    with open(path) as FH:
        requirements = [elt.strip().replace(" ", "") for elt in FH]
    return requirements


setup(
    name='variant_project',
    version=get_version(),
    description='Parse annotated VCF files, manage variant database and requests, provide web services.',
    author='Noël MAURICE - IUCT Oncopole Toulouse',
    author_email='maurice.noel@iuct-oncopole.fr',
    license='CeCILL v2.1',
    packages=[],
    install_requires=load_requirements("requirements.txt"),
    url='https://github.com/noelmaurice-iuct-oncopole/variant_project',
    python_requires='>=3.8',
    keywords='bio VCF variant sample filter annotation',
    # long_description_content_type='text/markdown',
    # long_description=get_long_description()
)