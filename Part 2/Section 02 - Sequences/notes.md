## Sequence Types

A type of data representation where elements are ordered and can be referenced by their position using an index.
There are six sequence types:strings, byte sequecnes, byte arrays, lists,tuples, range objects

## Iterable Type vs Sequence Type

What does it mean for an object to be iterable ?

It is a container type of object and we can list out the elements in that object one by one. So any sequence type is iterable. But an iterable is not necessarily a sequence type. Iterables are more general e.g sets or dicts.

## List Vs Tuples

- **Constant folding** - Constant folding is the process of recognizing and evaluating constant expression at compile time rather than computing them at runtime.

## Copy Sequences

Sometimes you want to make sure that whatever sequence you are working with cannot be modified, either indarvadently by yourself or by 3rd party functions.

```python

def reverse(s):
    s.reverse()
    return s

```

Bad code.

Generally we write functions that do not modify the contents of their arguments. But sometimes we really want to do so, and that's perfectly fine -> in-place methods. However, to clearly indicate to the caller that something is happening in-place, we should not return the object we modified.

### How to Copy a Sequence

- Simple loop
- List Comprehension
- Copy method
- Slicing
- `list()`

Using any of the techniques above, we have obtained a copy of the original, a shallow copy.


### Deep Copies

So, if collections contain mutable elements, shallow copies are not sufficient to ensure the copy can never be used to modify the original. Instead we have to do a something called a deep copy.

The standard library **copy** module has generic copy and deepcopy operations.

The **copy** function will create a shallow copy. The **deepcopy** function will create a deep copy, handling nested objects, and circular reference properly.

Custom classes can implement the `__copy__` and `__deepcopy__` methods to allow you to override how shallow and deep copies are made for your custom objects.