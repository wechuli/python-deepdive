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