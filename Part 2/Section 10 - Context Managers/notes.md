# Context Managers


## What is a context

The circumstances that form the setting for an event, statement or idea and in terms of which it can be fully understand

In Python: the state surrounding a section of code

## Context Managers Python
- Create a context (a minimal amount of state needed for a block of code)
   - execute some code that uses variables from the context
- Automatically clean up the context when we are done with it

context managers manage data in our scope - on entry, on exit
- very useful for anything that needs to provide Enter/Exit Start/Stop set/Reset e.g
- open/close file
- start db transaction/commit or abort transaction
- set decimal precision to 3/ reset back to original precision


## Context Manager patter
- Create some object. do some work with that object
- Clean up the object after we're done using it

```python
with context as obj_name:
  # with block (can use obj_name)

# after the with block, context is cleaned up automaticcally
```


## The context management protocol

Classes implement the context management protocol by implementing two methods:

- `__enter__` setup and optionally return some object
- `__exit__` tear down/cleanup

## Use Cases
- Very common usage is for opening a file(creating) and closing the file(releasing resource)
- Context managers can be used for much more than creating and releasing resources
Common Patterns
- Open-Close
- Lock - Release
- Change - Reset
- Start - Stop
- Enter - Exit

### Examples
- File context managers
- Decimal contexts

### How Context Protocol Works

Works in conjunction with a `with` statement

```python
with MyClass() as obj:
```
- Creates an instance of `MyClass`
- Calls `my_instance.__enter__()`
- return value from `__enter__` is assigned to `obj` (not the instance of `MyClass` that was created)

after the `with` block, or if an exception occurs inside the `with` block:

-> `my_instance.__exit__` is called

### Scope of `with` block

The `with` block is not like a function or a comprehension

The scope of anything in the `with` block (including the object returned from `__enter__`) is the same scope as the `with` statement itself.

### The `__enter__` Method

```python
def __enter__(self):
  pass
```
The method should perform whatever setup it needs to. It as optionally return an object -> as returned_obj

### The `__exit__` Method

More complicated

`__exit__` runs even if an exception occurs in `with` block. But should it handle things differently if an exception occurred? maybe

- So it needs to know about any exceptions that occurred
- it also needs to tell Python whether to silence the exception, or let it propagate

The `__exit__` method needs 3 arguments:
- the exception type that occurred(if any, `None` otherwise)
- the exception value that occurred(if any, `None` otherwise)
- the traceback object if an exception occurred(if any, `None` otherwise)

Return `True` or `False`
True = Silence any raised exception
False = do not silence a raised exception

```python
def __exit__(self,exec_type,exec_value,exec_trace):
#   do clean up work here
  return True # or False
```


### Additional Uses
- Open/Close patterns
- Pattern: Start -Stop e.g start database transactiion,perform database operations, commit or rollback transacks
- Pattern: Lock - Release
- Pattern: Change - Reset

### The contextlib Module

One of the goals when context managers were introduced to Python was to ensure generator functions could be used to easily create them.