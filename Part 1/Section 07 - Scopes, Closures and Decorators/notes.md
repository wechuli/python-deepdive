## Global and Local Namespaces

### Scopes and Namespaces

The variable name and it's binding (name and object) only "exists" in specific parts of our code. The portion of code where that name/binding is defined, is called **lexical scope** of the variable. These bindings are stored in namespaces.

### The Global Scope

The global scope is essentially the module scope. It spans a single file only. There is no concept of a truly global (across all the modules in our entire app) scope in Python. The only exception to this are some of the `built-in` globally available objects, such as `True`, `False`,`None`

The built-in and global variables can be used anywhere inside our module. Global scopes are nested inside the built-in scope.

Global scopes are nested inside the built-in scope. If you reference a variable name inside a scope and Python does not find in that scope's namespace, it will look for it in an enclosing scope's namespace.

### The Local Scope

When we create functions, we can create variable names inside those functions (using assignments). Variables defined inside a function are not create until the function is called. Every time the function is called, a new scope is created. Variables defined inside the function are assigned to that scope - functional scope

### Nested Scopes

Scopes are often nested.

Local Scope -> Module Scope -> Built-in Scope

When requesting the object bound to a variable name:

- Python will try to find the object bound to the variable
  - in current local scope first
  - works up the chain of enclosing scopes

When functions finish running, its variables go out of scope.

When retrieving the value of a global variable from inside a function, Python automatically searches the local scope's namespace, and up the chain of all enclosing scope namespaces.

What about modifying a global variable from inside the function?

```Python
a = 0
def my_func():
    a = 100
    print(a)
```

assignment -> Python interprets this as a local variable (at compile-time). The local variable `a` masks the global variable `a`

### Global keyword

We can tell Python that a variable is meant to be scoped in the global scope by using the global keyword.

### Global and Local Scoping

When Python encounters a function definition at compile-time, it will scan for any labels (variables) that have values assigned to them (anywhere in the function). If the label has not been specified as **global**, then it will be local.

Variables that are referenced but not assigned a value anywhere in the function will not be local, and Python will, at run-time. look for them in enclosing scopes.

### Nonlocal scopes

We can define functions from inside another function. Both functions have access to the global and built-in scopes as well as their respective local scopes. But the inner function also has access to its enclosing scope - the scope of the outer function. That scope is neither local (to inner_func) nor global - it is called a `nonlocal` scope.

Just as with global variables, we have to explicitly tell Python we are modifying a nonlocal variable. We can do that using the **nonlocal** keyword.
whenever Python is told that a variable is nonlocal:

- it will look for it in the enclosing local scopes chain until it first encounters the specified variable name. Beware that it will only look in local scopes, it will not look in the global scope.

## Free Variables and Closures

Functions defined inside another function can access the outer(nonlocal) variables. The term free variable refers to variables used in a function that are neither local variables nor parameters of that function. The term non-local variables is often a synonym in this context.

A closure is a persistent scope which holds on to local variables even after the code execution has moved out of that block. Languages which support closures will allow you to keep a reference to a scope(including its parent scope), even after the block in which those variables were declared has finished executing, provided you keep a reference to that block or function somewhere.

The scope object and all its local variables are tied to the function and will persist as long as that function persists. This gives us function portability. We can expect any variables that were in scope when the function was first defined to still be in scope when we later call the function, even if we call the function in a completely different context.

You can think of the closure as a function plus an extended scope that contains the free variables. The free variables's value is the object the cell points to - so that could change over time! Every time the function in the closure is called and the free variable is referenced:

- Python looks up the cell object, and then whatever the cell is pointing to

Every time we run a function, a new scope is created. If that function generates a closure, a new closure is created every time as well.

## Decorators

A decorator in Python is any callable Python object that is used to modify a function or a class. A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class. The modified functions or classes usually contain calls to the original function "func" or class "C".

In general a decorator function:

- takes a function as an argument
- returns a closure
- the closure usually accepts any combination of parameters
- runs some code in the inner function(closure)
- the closure function calls the original function using the arguments passes to the closure
- returns whatever is returned by that function call

The decorator @ symbol is a convenience to specify decorators.

In general, if **func** is a decorator function, we decorate another function **my_func** using

```Python
my_func = func(my_func)

```

This is so common that Python provides a convenient way of writing that:

```Python
@counter
def add(a,b):
    return a+b

```

is the same as writing

```Python
def add(a,b):
    return a+b

add = counter(add)
```


### Introspection of Decorated Functions

The **functools** module has a wraps function that we can use to fix the metadata of our inner function in our decorator. But it needs to know what was out "original" function

## Memoization

In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

### Parameterized Decorators

