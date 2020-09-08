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
