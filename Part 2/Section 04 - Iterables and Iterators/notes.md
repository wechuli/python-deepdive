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