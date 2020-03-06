# Tuples

A data structure where the position of the elements have meaning.

## Named Tuples

Named tuples are a subclass of tuples and add a layer to assign property names to the positional elements. Located in the collections standard library module.

```python
from collections import namedtuple
```

`namedtuple` is a function which generates a new class -> class factory . that new class inherits from tuple

`namedtuple` needs a few things to genertae this class:

- the class name we want to use
- a sequence of field names(strings) we want to assign, in the order of the elements in the tuple:
  - field names can be any valid variable name except that they cannot start with an underscore
- The return value of the call to namedtuple will be a class

We need to assign that class to a variable name in our code so we can use it to construct instances. In general, we use the same name as the name of the class that was generated.
