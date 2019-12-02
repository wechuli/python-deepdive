## Unpacking Packed Values

Unpacking is the act of splitting packed values into individual variables containing in a list or tuple. The unpacking into individual variables is based on the relative positions of each element.

The entire RHS is evaluated first and completely then assignments are made to the LHS.

## Extended Unpacking

- The * operator can only be used once in the LHS of an unpacking assignment
- The ** unpacking


- We set a default for dt to None
- Inside the function, we test to see if dt is still None
- If dt is None, set it to the current data/time
- Otherwise, use what the caller specified for dt

In general, always beware of using a mutable object (or a callable) for an argument default

## First Class Functions

### First Class Objects
- Can be passed to a function as an argument
- can be returned from a function
- can be assigned to a variable
- Can be stored in a data structure (such as list, tuple,dictionary)

Types such as int,float,string,tuple,list are first class objects. Functions are also first-class objects.

### Higher Order Function
Higher order functions are functions that:
- take a function as an argument and/or
- return a function

### Topics
- function annotations and documentation
- lambda expressions and anonymous functions
- callables
- function introspection
- built-in higher order functions (such as sorted, map, filter)
- some functions in the functools module such as reduce,all,any
- partials

### Function DocStrings

We can document our functions(and modules, classes) to achieve the same result using docstrings. If the first line in the function body is a string (not an assignment, not a comment, just a string by itself) it will be interpreted as a docstring

- Docstrings are stored in the objects's __doc__ property

### Function Annotations
Function annotations give us an additional way to document our functions

Annotations are stored in the __annotations__ property of the function.

### Lambda Expressions

Lambda expressions are simply another way to create functions anonymous functions
Lambdas, or anonymous fucntions are NOT equivalent to closures.

#### Limitations of Lambdas
- The body of a lambda is limited to a single expression
- No assignments
- No attotations