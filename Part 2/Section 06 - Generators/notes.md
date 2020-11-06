## generators

A type of iterator

## generator functions

- generator factories
- they return a generator when called

## generator expressions

- uses comprehension syntax
- a more concise way of creating generators
- useful for simple situations

## Performance considerations

## Yield

The `yield` keyword does:

- it emits a value
- the function is effectively suspended (but it retains its current state)
- calling `next` on the function resumes running the function right after the yield statement
- if function returns something instead of yielding(finishes running) -> StopIteration exception

A function that uses the `yield` statement is called a `generator function`.

We can think of functions that contain the `yield` statement as generator factories.

The generator is created by Python when the function is called. The function body will execute until it encounters a `yield` statement. It yields the value (as return value of next()) then it suspends itself until next is called again -> suspended function resumes execution. If it encounters a return before a yield - Stop Iteration exception

Generators are exhausted when the function returns a value
-> StopIteration exception
-> return value is the exception message

Generators are inherently lazy iterators (and can be infinite)

Generators are iterators and can be used in the same way other iterators are used