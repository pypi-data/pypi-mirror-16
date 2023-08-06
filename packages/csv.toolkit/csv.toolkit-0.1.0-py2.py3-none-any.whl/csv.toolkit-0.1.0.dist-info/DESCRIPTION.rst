.. image:: https://travis-ci.org/sietekk/csv.toolkit.svg?branch=master
    :target: https://travis-ci.org/sietekk/csv.toolkit
    :alt: Build Status

.. image:: https://coveralls.io/repos/github/sietekk/csv.toolkit/badge.svg?branch=master
    :target: https://coveralls.io/github/sietekk/csv.toolkit?branch=master
    :alt: Coverage


********************
CSV Toolkit Overview
********************


**NOTE: THIS PROJECT HAS SINCE BEEN FORKED TO THE INTERNAL PROMETHEUS
RESEACH, LLC TOOL PROPS.CSVTOOLKIT**


CSV Toolkit is a `Python`_ package that provides validation tooling
and processing of CSV files. The validation tooling is based on the
fantastic package `Vladiate`_. The interface and extension mechanisms
are similarly implemented as the `rex.core`_ extension mechanisms.

.. _`Python`: https://www.python.org
.. _`Vladiate`: https://github.com/di/vladiate
.. _`rex.core`: https://bitbucket.org/rexdb/rex.core

.. contents:: Table of Contents


Example Usage
=============

This packace comes equipped with validation tooling, a CLI, a tooling interface,
a logging mechaism, and a loader mechanism. All are extensible, allow for
future additions of new tools to this package, and the instroduction of custom
tools depending on this package. This package comes with implementations built
in as well.


Validation Tooling
******************

This application comes with a validation tooling mechanism buil-tin. It allows
for defining a validation schema to run against a CSV file. This was implemented
due to the severe lack of strict validation mechanisms in the Python standard
library's ``csv`` module. While it does implement the ``csv`` module to some
extent, it allows for strict validation with an extensible validation mechanism.
Furthermore, the validation mechanism may be used via the CLI or as a standard,
internal validation mechanism for your pacakge.


Built-In Simple CSV Validator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Included with this package is a simple CSV file validation mechanism to use to
validate simple CSV structures where fields may contain any values or may be
empty. This is also a good example of how to implement a CSV validation schema
as an internal tool available to the CLI.

New Implementations
^^^^^^^^^^^^^^^^^^^

Subclass the ``BaseFileValidator`` class to create a new CSV validation tool. The
required fields ``validators``, ``delimeter``, ``default_validator``,
``check_duplicate_headers``, and ``logger`` attributes must be defined. Creating
a new logger for each CSV validating tool is recommended, but not necessary.

An example bare-bones implementation would be::

    >>> class YourFirstValidatorLogger(Logger):
    >>>     pass
    >>>
    >>> class YourFirstValidator(BaseFileValidator):
    >>>     validators = {
    >>>         "Field1": [],
    >>>         "Field2": [],
    >>>         "Field3": [],
    >>>     }
    >>>     delimiter = ","
    >>>     default_validator = AnyVal
    >>>     check_duplicate_headers = True
    >>>     logger = YourFirstValidatorLogger
    >>>
    >>>     def validate(self):
    >>>         ... validation mechanism here...
    >>>
    >>> validator = YourFirstValidator(LocalFileLoader('/path/to/example.csv'))
    >>> print validator.validate()
    True
    >>> result = validator()
    >>> print result.validation
    True
    >>> print result.log
    ... validation log text...

Obviously, you may call the ``validate`` property directly without a logger, but
you may also call the validator instance, which returns a named tuple ``Result``
with ``validation`` and ``log`` attributes.

Please note, att this time the ``BaseFileValidator`` only supports loggers of the
built-in type. Pull requests and contributions to change this are more than
welcome.

Validator Attribute Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``validators`` attribute must define the validation schema for your type of
CSV. It must be a dictionary with string keys defining the available columns and
list values specifying the validator (with any initialization parameters the
validator requires).

An example validation schema would look like::

    >>> validators = {
    >>>     "Foo": [
    >>>         UniqueVal(),
    >>>     ],
    >>>     "Bar": [
    >>>         RegexVal(r'^baz$'),
    >>>     ],
    >>>     "hello world": [
    >>>         IntVal(empty_ok=True),
    >>>     ],
    >>> }

This schema corresponds to a CSV with headers ``Foo``, ``Bar``, and
``hello world``. The ``Foo`` column must contain unique values, the ``Bar``
column must contain fields matching the regular expression ``^baz$``, and the
``hello world`` column must contain integer values, but allows for empty fields
as well.

Built-In Validators
^^^^^^^^^^^^^^^^^^^

This package comes with built-in validators. For example:

- IntVal: Integer values (allows empty values)
- FloatVal: Float values (allows empty values)
- BoolVal: Boolean values (allows empty values)
- EnumVal: Enumerated values::

    EnumVal(['a', 'list', 'of', 'enumerations',])

- UniqueVal: Unique values only
- RegexVal: Fields must match supplied regex value (or no fields are matched)
- EmptyVal: All fields must be empty
- AnyVal: Any allowed values, but not empty

**NOTE:** Inclusion of a JSON validator has not been made at this time, but
pull requests and contributions of an implementation are welcome.


Logging
*******

The logging mechanism is simple, and records logs to an internal dictionary per
instantiation. This allows for easy storage and retrieval of logs and logging
information pertinent to your CSV tool.

One may use the global logging instance ``logger_main``, the logging context
manager ``logger_context``, or subclass the logging implementation ``Logger``
to create custom logging instances.


Loaders
*******

The loader mechanism provides an easy tool to work with files and string objects.
A simple wrapper around a specified ``loader``, working with file-like objects
becomes much simpler when working with CSV data.

A user may work with the ``StringLoader`` or ``LocalFileLoader`` classes by
instantiating them with a source string or directory. For example::

    >>> mystring = StringLoader(StringIO("A test string."))
    >>> teststring = mystring.open()
    >>> print teststring
    "A test string."

To create new loaders, simply subclass the ``Loader`` class, specify a loader
and any args or kwargs that are necessary for that loader to operate.


Tooling
*******

This package provides a tooling interface to allow automatic discovery of new
tooling commands for the CLI. Simply subclass the ``Tool`` class to create a
new tool, which will be usable via the CLI. Make sure to specify the required
``name`` attribute. A ``description`` atrribute is very useful, and if your
tool/command requires it, specify the ``arguments`` attribute.

The ``implementation`` method must be overriden to tell the application what to
do when the command is run or the tool is used internally to an application. The
function must return a ``0`` if successful and a ``1`` or other if not. The
returned value is passed to stdout for successes and stderror for failures.


Arguments
^^^^^^^^^

The arguments must be a list of tuples with each touple containing the
parameters usually passed to the ``argparse.add_argument()`` function. For
example, a typical implementation looks like::

    >>> self.parser.add_argument(
    >>>     "filename",
    >>>     type=argparse.FileType('r'),
    >>>     help="A file."
    >>> )

which, for a tool implementation, should be converted too::

    >>> arguments = [
    >>>     (
    >>>         'filename',
    >>>         {'type': argparse.FileType('r')},
    >>>         {'help': 'A file.'},
    >>>     ),
    >>> ]

Please note that the ``scripts.py`` file (the entry point for the CLI) will
parse known arguments from the command line, and pass the rest to your tooling
implementation.


The CLI
*******
The command line interface automatically discovers all tooling implementations
subclassed from the interface ``Tool`` super class. The base command line
argument is ``csvtoolkit`` with a named parameter. The named parameter is any of
the available tooling implementations' ``name`` attribute.

For example::

    >>> class MyTool(Tool):
    >>>     name = "my-super-awesome-tool"
    >>>     ... and so on...

This tooling implementation is available via the CLI with the command::

    $ csvtoolkit my-super-awesome-tool

Again, please note that the ``scripts.py`` file (the entry point for the CLI)
will parse known arguments from the command line, and pass the rest to your
tooling implementation.


Contributing
============

Contributions and/or fixes to this package are more than welcome. Please submit
them by forking this repository and creating a Pull Request that includes your
changes. We ask that you please include unit tests and any appropriate
documentation updates along with your code changes. Code must be `PEP 8`_
compliant.

This project will adhere to the `Semantic Versioning`_ methodology as much as
possible, so when building dependent projects, please use appropriate version
restrictions.

.. _`Semantic Versioning`: http://semver.org
.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/

A development environment can be set up to work on this package by doing the
following::

    $ virtualenv csvtools
    $ cd csvtools
    $ . ./bin/activate
    $ git clone https://github.com/sietekk/csv.toolkit.git
    $ pip install -e ./csvtools[dev]


License/Copyright
=================

This project is licensed under The MIT License. See the accompanying
``LICENSE.rst`` file for details.

Copyright (c) 2016, Michael Conroy


