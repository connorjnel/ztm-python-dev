# Python Generators

Generators allow us to generate sequence of values over time
Generators more efficient to create a iterable list when needed and acted upon rather than saving it in memory upfront

`range` - One type of generator, returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
`yield` - To end a function, returns a generator

Tip. Iterable - An iterator is an object that contains a countable number of values. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.
Tip. Everything used as a Generator is iterable but not every iterable is a generator. Generators are actually functions just like range(:) is a function. Generator functions have yield keyword instead of return keyword in their function.
Tip. Yield keyword pauses the function and comes back to it when it encounters a next keyword. As such it hold only the most recent value of the iterable in the memory. next( ) can be called until the range provided in our generator function expires. Just as the range expires, our code will throw a Stop Iteration Error.
