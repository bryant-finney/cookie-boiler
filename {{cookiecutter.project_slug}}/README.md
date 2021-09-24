# {{ cookiecutter.project_name }}

[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})

[![travis](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

[![docs](https://readthedocs.org/projects/{{ cookiecutter.project*slug | replace("*", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)

{% if cookiecutter.add_pyup_badge == 'y' %}
[![pyup](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}

{{ cookiecutter.project_short_description }}

## Features

- TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the [`bryant-finney/cookie-boiler`](https://github.com/bryant-finney/cookie-boiler)
project template.
