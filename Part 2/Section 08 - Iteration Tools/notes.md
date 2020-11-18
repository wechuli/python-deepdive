## The itertools module

- Slicing - `islice`
- Selecting and Filtering - `dropwhile` `takewhile` `compress` `filterfalse`
- Chaining and Teeing - `chain` `tee`
- Mapping and Reducing - `starmap` `accumulate`
- Infinite iterators - `count`, `cycle`, `repeat`
- Sipping - `zip_longest`
- Combinatorics `product` `permutations` `combinations` `combinations_with_replacement`

### Aggregators

Functions that iterate through an iterable and return a single value that(usually) takes into account e.g sum,max,min

Every object in Python has an associated truth value

Falsy values
- None
- False
- 0
- empty sequence(e.g list, tuple, string)
- empty mapping types (e.g dictionary,set)
- custom classes that implement a `__bool__` or `__len__` method that returns False or 0

A function that takes a single argument and returns True or False is called a predicate

### Selecting and Filtering

- **itertools.compress** - it is basically a way of filtering one iterable, using the truthiness of items in another iterable.
- **itertools.takewhile** - The takewhile function returns an iterator that will yield items while pred(item) is truthy

### Chaining and Teeing

#### Chanining Iterables
This is analogous to sequence concatenation but not the same

#### Copying Iterators

Sometimes we need to iterate through the same iterator multiple times, or even in parallel

We can use `tee` in `itertools`
- returns independent iterators in a tuple

## Mapping and Accumulation

Mapping - applying a callable to each elemtn of an iterable
Accumulation -> reducing an iterable down to a single value e.g sum(iterable),min(iterable),max(iterable),reduce(fn,iterable,[initializer])

#### starmap
Starmap is very similar to map
- it unpacks every sub element of the iterable argument, and passes that to the map function
- useful for mapping a multi-argument function on an iterables of iterables


### Grouping

Sometimes we want to loop over an iterable of elements but we want to group those elements as we iterate through them.

### Combinatorics

Itertool module contains a few functions for generating permutations, combinations.

- Cartesian product
- Permutation - Elements of the iterable are considered unique based on their position, not their value. T
- Combinations - Unlike permutations, the order of elements in a combination is not considered -with or without replacement