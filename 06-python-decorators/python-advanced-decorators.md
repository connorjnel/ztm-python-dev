# Python Advanced Decorators

## Decorators

Decorators are the most common use of higher-order functions in Python. It allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

tip - `del` - Keyword in py for deleting functions, objects, lists, dict etc
tip - var and func in py are first class, can be passed as arg,
tip - if passed by ref source object is deleted then object can still be called by child reference

## Higher order function HOC

Higher order function - function that accepts another function as argument or a function that returns another function
Tip - Map, reduce, filter are higher functions

## Tips

tip - Function that wraps another function and enhances it, add extra functionality to other functions, can enqeue actions before and after wrapped functions
tip - if wrapped function has a parameter then wrapper function also needs param as well as wrapped function inside wrapper,
tip - `*args, **kwargs` - can use this pattern for wrapper and wrapped function, will accept multiple args and kwargs without having to worry about updating decorator wrapped function constantly
