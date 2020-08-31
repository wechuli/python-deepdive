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

## Slicing

Slicing relies on indexing - only works with sequence types

| **Mutable Sequence Types** | **Immutable Sequence Types** |
| -------------------------- | ---------------------------- |
| Extract Data               | Extract data                 |
| assign data                |

slice definitions are actually objects

### Step Value

Slices also support a third argument - the step value. When not specified, the step value defaults to 1.

Any slice essentially defines a sequence of indices that is used to select elements for another sequence. In fact, any indices defined by a slice can also be defined using a range. The difference is that slices are defined independently of the sequence being sliced.

Be careful of empty slices.

The **slice** object has a method, indices, that returns the equivalent range start/stop/step for any slice given the length of the sequence being sliced.

## Creating Custom Sequence Types

At it's most basic, an immutable sequence type should support two things:

- returning the length of the sequence
- given an index, returning the element at that index

If an object provides this functionality, then we should in theory be able to:

- retrieve elements by index using square brackets
- iterate through the elements using Python's native looping mechanisms

Remember that sequence types are iterables, but not all iterables are sequence types.

Sequence types at a minimum, implement the following methods

`__len__`

`__getitem__`

At its most basic, the `__getitem__` method takes in a single integer argument - the index. However, it may also choose to handle a slice type argument.

### The `__getitem__` method

The `__getitem__` method should return an element of the sequence based on the specified index or raise an `IndexError` exception if the index is out of bounds.

### The `__len__` Method

In general sequence types support the Python built-in function `len()`

To support this all we need to do is implement the `__len__` method in our custom sequence type.

### Stable Sorts

A stable sort is one that maintains the relative order of items that have equal keys