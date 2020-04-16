# Modules, Packages and Namespaces

A module is an instance of the module type. Python has a way to put definitions in a file and use them in a script or in an interactive instance of the intepreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module.

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module's name (as a string) is available as the value of the global variable `___name__`.

### How Python imports a module

- Checks the `sys.modules` cache to see if the module has already been imported - if so it simply uses the reference in there, otherwise:
- it creates a new module object (types.ModuleType)
- loads the source code from file
- adds an entry to `sys.modules` with name as key and newly created module as the value
- compiles and executes the source code.

We use two built-in functions, `compile` and `exec`. The `compile` function compiles source (e.g text) into a code object. The `exec` function is used to execute a code object. Optionally we can specify what dictionary should be used to store global symbols.

### How does an import actually happen

For example importing as below

```python
# module1.py
import math

```

- Check if `math` is in `sys.modules`, if not, load it and insert a ref of `math` to it in `sys.modules`
- add symbol `math` to module1;s global namespace referencing the same object

```python
import math as r_math

```

- Check if `math` is in `sys.modules`, if not, load it and insert a ref of `math` to it in `sys.modules`
- add symbol `r_math` to module1;s global namespace referencing the same object

```python
from math import sqrt


```

- The math symbol is not in the global namespace but is in the `sys.modules`. This is not anymore efficient because the whole math module was loaded into the `sys.modules`

```python
from math import sqrt as r_sqrt
```

What changes is the global namespace

```python
from math import *
```

add "all" symbols defined in math to module1's global namespace

## Modules Recap

- Modules can be imported using the `import` statement
- When a module is imported:
  - `system cache` is checked first **sys.modules** -> if in cache, just returns cached reference otherwise
  - module has to be located(found) somewhere using finders e.g `sys.meta_path`
  - module code has to be retrieved(loaded) - loaders returned by finders
  - "empty" module typed object is created
  - a reference to the module is added to the system cache sys modules
  - module is compiled
  - module is executed -> sets up the module's namespace (`module.__dict__` is `module.globals()`)

## Module Properties

- built-in
- standard library
- custom module

Python modules may reside

- in built ins
- in files on disk
- they can even be pre-compiled, frozen or even inside zip archives
- anywhere else that can be accessed by a finder and a loader custom finders/loaders -> database, http

## Python Packages

Packages are modules that can contain modules or other packages(sub-packages). If a module is a package, it must have a value set for `__path__`. After you have imported a module, you can easily see if that module is a package by inspecting the `__path__` attribute. (empty -> module, non-empty-> package)

- Remember that modules do not have to be entities in a file system
- By the same token, packages ddo not have to be entities in the file system
- Typically they are - just as typically modules are file entities

### Importing Nested Packages

If you have a statement in your top-level program such as:

```python

import pack1.pack1_1.module1

```

The import system will perform these steps:

- Import `pack1`
- imports `pack.pack1_1`
- imports `pack1.pack1_1.module1`

The `sys.modules` cache will contain entries for `pack1` `pack1.pack1_1` and `pack1.pack1_1.module1`

### File Based Packages

- package paths are created by using file system directories and files
- A package is simply a module that can contain other modules/packages
- On a file system we therefore have to use directories for packages
- The directory name becomes the package name
- So where does the code go for the package - `__init__`

To define a package in our file system, we must:

- create a directory whose name will be the package name
- create a file called `__init.py__` inside that directory

That `__init__.py` file is what tells Python that the directory is a package as opposed to a standard directory. If we don't have an **init**.py

#### What happens when a file based package is imported?

app/
pack1/
**init**.py
module1.py
module2.py

```python

import pack1

```

- the code for `pack1` is in **init**.py
- that code is loaded, executed and cached in `sys.modules` with a key of `pack1`- it's just a module
- the symbol `pack1` is added to our namespace referencing the same object
- but is also has a `__path__` property -> file system directory path(absolute)
- also has a **file** property -> file system path to **init**.py

### Nested Packages

`__file__`,`__path__` and `__package__` properties. Modules have `__file__` and `__package__` properties.

- `__file__` is the location of modules code in the file system
- `__package__` is the package the module code is located in - an empty string if the module is located in the application root

If the module is also a package, then it also has a `__path__` property

- Just because a package is loaded, does not mean the package has loaded everything inside that package. By default it does not

### Using **init**.py

We can use packages `__init__.py` code to export(expose) just what's needed by our users.

### Why Packages

- ability to break code up into smaller chunks, makes our code
  - easier to write
  - easier to test and debug
  - easier to read/understand
  - easier to document
