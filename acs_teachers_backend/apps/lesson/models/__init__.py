"""
An __init__.py for django which allows models to be
organized into separate files without any boilerplate
IOW, go from this...
    ├── models.py
to this...
    ├── models
    │   ├── __init__.py
    │   ├── location.py
    │   ├── customer.py
    │   ├── customer_group.py
without editing __init__.py

Will create:
    ├── Location
    ├── Customer
    ├── CustomerGroup

extend code: https://gist.github.com/perrygeo/1559dad5474d71823e26
"""

"""
String snake_case to CamelCase
source: https://stackoverflow.com/a/19053800
"""
from os import path
from pathlib import Path
from django.db.models import Model

import glob
import importlib


def to_upper_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


# find all *.py files in current dir
modules = glob.glob(path.join(path.dirname(__file__), "*.py"))
# get pair filename, extension
split_names = [path.splitext(path.basename(n)) for n in modules]
# remove __init__.py file
split_names = [n for n in split_names if n[0] != "__init__"]

for filename, extension in split_names:
    class_name = to_upper_camel_case(filename)
    mpath = ".%s" % (filename)

    model_module = importlib.import_module(mpath, __name__)

    try:
        # get class from file
        class_global = model_module.__dict__[class_name]

        # if not class is subclass of model class
        if not issubclass(class_global, Model):
            raise NotImplementedError("Class %s not instance of %s" % (class_global, Model))

        # Add class to globals vars
        globals()[class_name] = class_global

    except KeyError:
        raise ModuleNotFoundError("No class named %s in %s%s" % (class_name, filename, extension))