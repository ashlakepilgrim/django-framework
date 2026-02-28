# Learning Django Framework

Django is a web framework. To get started, install Python and execute these commands:

```shell
python -m venv venv
cd venv/Scripts
activate
cd ../..
python -m pip install Django
python -m django --version
```

Then create a django project:

```shell
django-admin startproject mysite
```

### Understanding Django Project Directory Structure

But before we proceed, it's important to understand `module` vs `package` vs `library`.

In Python, modules and packages have specific, technical definitions for organizing code, while library is a more general, conceptual term.

- Module: A module is a single Python file with a `.py` extension that contains functions, classes, and variables that can be imported and reused in other programs. For example, a file named math.py would be the math module.

- Package: A package is a directory that organizes related modules into a hierarchical namespace, much like folders on a computer's file system. To be recognized as a standard package, this directory must contain a special file named `__init__.py` (though this is optional for "namespace packages" in Python 3.3+). For example, you could have a sound package directory containing formats and effects subpackages, each with their own modules like `wavread.py` or `echo.py`.

- Library: "Library" is an informal, high-level term used to refer to a collection of modules and packages designed to provide a broad set of reusable functionalities for common tasks, such as data manipulation or scientific computing. Libraries like NumPy or pandas are technically implemented as large packages (or collections of packages) but are conceptually referred to as libraries because of their wide range of applications. The Python Standard Library is the extensive collection of built-in modules and packages that come with a standard Python installation.

Now, the django project directory structure:

```shell  
.
└── mysite/
    ├── manage.py
    └── mysite/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

- `manage.py`: kind of like a control panel for the whole project
- `mysite`: directory that is the actually a python package for our project
- `mysite/__init__.py`: an empty file that tells Python to treat the directory it's in as a Python package
- `mysite/settings.py`: settings or configs for the django project
- `mysite/urls.py`: urls or endpoints are declared in this file
- `mysite/asgi.py`: for asynchronous configuration
- `mysite/wsgi.py`: for synchronous configuration

Alongwith, `mysite` directory, there could be more folders which are referred to as `apps` in django project.