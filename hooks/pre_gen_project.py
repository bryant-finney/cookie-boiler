import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug `{}` is not a valid ".format(module_name)
        + "Python module name. Please use `-` instead of `_` ."
    )

    # Exit to cancel project
    sys.exit(1)
