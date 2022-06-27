# Python Reference
- [Python Reference](#python-reference)
- [Sites](#sites)
- [Language Fundamentals](#language-fundamentals)
- [Modules and Libraries](#modules-and-libraries)
  - [Standard Library](#standard-library)
  - [Asynchronous Programming](#asynchronous-programming)
  - [Concurrency](#concurrency)
  - [Networking Programing](#networking-programing)
  - [Virtual Environments](#virtual-environments)
  - [Linting](#linting)
  - [Static Typing](#static-typing)
  - [Unit Testing](#unit-testing)
- [Other Stuff](#other-stuff)

# Sites

- [Python Docs](https://docs.python.org/3/)

- [Python Reference](https://docs.python.org/3/reference/)

- [Python Wiki](https://wiki.python.org/moin/)

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

- [Intro to Python - Real Python](https://realpython.com/learning-paths/python3-introduction/)

- [Python Playlist](https://www.youtube.com/playlist?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB) (freeCodeCamp)

- [Intermediate Python Programming](https://www.youtube.com/watch?v=HGOBQPFzWKo) (freeCodeCamp)

- [Object Oriented Programming in Python](https://www.youtube.com/watch?v=Ej_02ICOIgs) (freeCodeCamp)

# Language Fundamentals

- [Getting Started - Python Docs](https://docs.python.org/3/tutorial/index.html)

- [Built-in DataTypes](https://docs.python.org/3/library/stdtypes.html)

- [Variables](https://realpython.com/python-variables/)

  - [Scopes](https://realpython.com/python-scope-legb-rule/)

- [Operators](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)

  - [Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)

  - [Ternary Operator](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

  - [Walrus Operator](https://realpython.com/python-walrus-operator/)

- Control Flow

  - `if`, `elif` and `else`

  - [`match`](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) keyword

- Loops

  - [`while` loop](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

  - [`for` loop](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)

  - `break` & `continue`

- Exception Handling

  - `try`, `except` and `finally`

  - `raise` keyword

  - [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

- [Keywords](https://realpython.com/python-keywords/#python-keywords)

- [Expressions](https://docs.python.org/3/reference/expressions.html), [Simple Statements](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) & [Compound Statements](https://docs.python.org/3/reference/compound_stmts.html)

- Functions

  - [Built-In Functions](https://docs.python.org/3/library/functions.html)

  - [Variadic Arguments (`*args` & `**kwargs`)](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) ([realpython](https://realpython.com/python-kwargs-and-args/))

  - Lambda Functions

  - [Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U)

  - Closures and `nonlocal` keyword

  - Generators

- [Data Types and Data Structures](https://docs.python.org/3/library/datatypes.html)

  - [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) ([List Comprehension](https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries))

  - Tuples

  - [Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

  - [Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

  - [Binary Sequence Types](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)

  - [Iterators](https://docs.python.org/3/library/stdtypes.html#iterator-types)

  - [`queue`](https://docs.python.org/3/library/queue.html)

  - [`array`](https://docs.python.org/3/library/array.html)

  - [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq) (min-heap)

  - [`bisect`](https://docs.python.org/3/library/bisect.html#module-bisect) (sorted lists)

  - [`collections`](https://docs.python.org/3/library/collections.html)

  - [`collections.abc`](https://docs.python.org/3/library/collections.abc.html) (abstract base class)

  - [Time Complexities](https://wiki.python.org/moin/TimeComplexity)

- [Mutability](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)

- [Context Managers](https://realpython.com/python-with-statement/)

- [File I/O](https://www.w3schools.com/python/python_ref_file.asp)

- [Object Oriented Programming](https://docs.python.org/3/reference/datamodel.html)

  - [OOP Basics](https://realpython.com/python3-object-oriented-programming/)

  - Constructors (`__init__()` & `__new__()`)

  - Instance and Class Attributes

  - Instance, Class and Static Methods

  - Inheritance (`super()`)

  - [Multiple Inheritance](https://realpython.com/python-super/) (mro)

  - Access Modifiers (\_protected & \_\_private)

  - Getter and Setter ([@property](https://docs.python.org/3/library/functions.html#property) & [property()](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python))

  - [Magic Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)

  - Abstract Classes

  - [Data Classes](https://docs.python.org/3/library/dataclasses.html)

- [Python Packages](https://realpython.com/python-modules-packages/#python-packages) (working with modules)

# Modules and Libraries

## [Standard Library](https://docs.python.org/3/library/) 

- [**Complete Index**](https://docs.python.org/3/py-modindex.html)

- [`argparse`](https://docs.python.org/3/library/argparse.html)

- [`copy`](https://docs.python.org/3/library/copy.html)

- [`csv`](https://docs.python.org/3/library/csv.html)

- [`inspect`](https://docs.python.org/3/library/inspect.html)

- [`logging`](https://docs.python.org/3/library/logging.html)

- [`itertools`](https://docs.python.org/3/library/itertools.html)

- [`os`](https://docs.python.org/3/library/os.html)

- [`pathlib`](https://docs.python.org/3/library/pathlib.html)

- [`random`](https://docs.python.org/3/library/random.html)

- [`shutil`](https://docs.python.org/3/library/shutil.html)

- [`sqlite3`](https://docs.python.org/3/library/sqlite3.html)

- [`subprocess`](https://docs.python.org/3/library/subprocess.html)

- [`sys`](https://docs.python.org/3/library/sys.html)

- [`unittest`](https://docs.python.org/3/library/unittest.html)

- [`urllib`](https://docs.python.org/3/library/urllib.html)

## [Asynchronous Programming](https://docs.python.org/3/library/asyncio.html)

- [`asyncio`](https://docs.python.org/3/library/asyncio-task.html#id3) - [TechWithTim Video](https://www.youtube.com/watch?v=t5Bo1Je9EmE)

- [Streams](https://docs.python.org/3/library/asyncio-stream.html)

## Concurrency

- [threading](https://docs.python.org/3/library/threading.html)

- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures)

## [Networking Programing](https://docs.python.org/3/library/ipc.html)

- [`socket`](https://realpython.com/python-sockets/)

- [`selector`](https://docs.python.org/3/library/selectors.html) (concurrency)

## Virtual Environments

- [venv](https://docs.python.org/3/library/venv.html) (built-in version of virtualenv)

- [virtualenv](https://virtualenv.pypa.io/en/latest/)

- [pipenv](https://realpython.com/pipenv-guide/)

- [pyenv](https://github.com/pyenv/pyenv) (python executable management)

- [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) (environment management system)

## Linting

- [Pylint](https://pylint.pycqa.org/en/latest/)

## Static Typing

- [`typing`](https://docs.python.org/3/library/typing.html) module

- mypy

## Unit Testing

- [pytest](https://docs.pytest.org/en/7.1.x/)


# Other Stuff

- [Static Analysis Tools](https://luminousmen.com/post/python-static-analysis-tools)

- [PEP-8](https://www.python.org/dev/peps/pep-0008/) style guide

- [Docstrings](https://realpython.com/documenting-python-code/) (documenting code)

- [Python Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html)