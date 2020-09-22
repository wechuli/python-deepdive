- Iterators
- Iterables
- Consuming iterators manually
- Relationship between sequence types and iterators
- Infinite iterables
- Lazy Evaluation
- Iterator Delegation

In sequences, the items are ordered in the collection. But iteration can be more general than based on sequential indexing. All we need is a bucket of items(collection) and get the `next` item. Just a way to get an item out of the collections

- Sets are unordered collections of items but sets are still iterable.
- Python's `next()` function - We can implement that function for our custom type by implementing the special method: `__next__`


### The Iterator Protocol

A protocol is simply a fancy way of saying that our class is going to implement certain functionality that Python can count on.

The iterator protocol is quite simple - the class needs to implement two methods:

- `__iter__` - this methos should just return the object(class instance itself.)
- `__next__` - this method is responsible for handling back the next element from the collection and raising the `StopIteration` exception when all elements have been handed out.

An object that implements this two methods is called an iterator. If an object is an iterator, we can use it in the for loop or list comprehensions

Separating the Collection from the iterator.

Instead, we would prefer to separate these two:
- Maintaining the data of the collection should be one object
- Iterating over the data should be a separate object ->

The collection is iterable but the iterator is reponsible for iterating over the collection. The iterable is created once. The iterator is created every time we need to start a fresh iteration.

### Iterable

An iterable is a Python object that implements the iterable protocol. The iterable protocol requires that the object implement a single method:

`__iter__` - return a new instance of the iterator object used to iterate over the iterable

So iterators are themselves iterables but they become exhausted.

Iterables on the otther hand never become exhausted, they always return a new iterator that is then used to iterate.

Python has a built-in function `iter()`. It calls the `__iter__` method. The first thing Python does when we try to iterate over an object
- it calles iter() to obtain an iterator
- then is starts calling

If you implement both the Sequence and Iterabble protocol in an object Python prefers to use the Iterator first.