#!/usr/bin/env python
"""
Use :mod:`setuptools` to build and install this package.

.. moduleauthor:: {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
"""
from setuptools import find_packages, setup

requirements = [{%- if cookiecutter.command_line_interface|lower == "click" %}"Click>=7.0"{%- endif %}]
test_requirements = [{%- if cookiecutter.use_pytest == "y" %}"pytest>=3"{%- endif %}]

{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}


def get_history():
    """Load HISTORY.md as a string."""
    with open("HISTORY.md", "r") as history_file:
        return history_file.read()


def get_readme():
    """Load README.md as a string."""
    with open("README.md", "r") as readme_file:
        return readme_file.read()


if __name__ == "__main__":
    history, readme = get_history(), get_readme()
    setup(
        author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
        author_email="{{ cookiecutter.email }}",
        python_requires=">=3.6",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        description="{{ cookiecutter.project_short_description }}",
        {%- if "no" not in cookiecutter.command_line_interface|lower %}
        entry_points={
            "console_scripts": [
                "{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main",
            ],
        },
        {%- endif %}
        install_requires=requirements,
        long_description=readme + "\n\n" + history,
        include_package_data=True,
        keywords="{{ cookiecutter.project_slug }}",
        name="{{ cookiecutter.project_slug }}",
        packages=find_packages(include=["{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.*"]),
        test_suite="{{ cookiecutter.project_slug }}",
        tests_require=test_requirements,
        url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
        version="{{ cookiecutter.version }}",
        zip_safe=False,
    )
