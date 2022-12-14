# Python Advanced FP

Functional programming is a style of programming that emphasizes the evaluation of expressions rather than the execution of commands.
Seperating of concerns, seperate data and methods/functions.

## FP Code Goals

Clean and understandable
Easy to extend
Easy to maintain
Memory Efficient
DRY

## Pure Functions

Functions are simple, have repeatable results, output is always the same if input is the same, does not produce side effects
Seperate the data of a program from function of a program
Side effects = Effecting the outside world, printing onto screen, changing var in seperate scope
Tip. print inside function is a side effect, so does outputting to outside variable
Tip. FP generally generates less errors as control is maintained, testing is easier, easier to understand
Tip. Pure functions are a guideline, not a rule. If something can be pure then do it, if you cant dont freak out about it

## Map function

`map()` = Function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
ex. `mapped_list = list(map(multiply_by4, new_list))`
Tip. Map does not mutate original data source

## Filter function

`filter()` = Function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
ex. `filtered_list = list(filter(only_odd, new_list))`
Tip. Filter does not mutate original data source

## Zip function

`zip()` = Function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
ex. `zipped_list = list(zip(list_1, list_2))`
Tip. Zip does not mutate original data source

## Reduce function

`reduce()` - The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
Tip. Reduce needs to be imported to be used - `from functools import reduce`
Tip. Accumulator default to 0 if not defined in accumulator function
ex. Acc function - `def accumulator(acc, item):return acc + item` - Acc defaults to zero if not defined in function
ex. reduce function - `reduced_list = reduce(accumulator, list_3, 0)` - 0 does not need to be defined here either

## Lambda Expressions

A lambda function is a small anonymous function - function doesnt have a name
A lambda function can take any number of arguments, but can only have one expression.
`lambda parameter: function / action (param)`
ex. `mapped_list_lambda = list(map(lambda item: item*2, new_list))`
ex. `filtered_list_lambda = list(filter(lambda item: item % 2 != 0, new_list))`
ex. `reduced_list_lambda = reduce(lambda acc, item: acc + item, new_list)`
Tip. Can use lambda inside of other methods, for example can use lambda as key in sorted

## Sort and sorted

`sort` - Mutates original, only usable on lists, returns nothing, list method
`sorted` - Does not mutate, usable on iterables, returns result

## List comprehensions

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing iterable.
ex. `my_list2 = [char for char in "hello"]`
ex. `my_list3 = [num for num in range(0, 100)]`
ex. `my_list4 = [num*2 for num in range(0, 100)]`
ex. `my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]`
Tip. Can add conditions and operators to comprehensions

## Set and dictionary comprehensions

Set & Dict comprehension offers a shorter syntax when you want to create a new set or dict based on the values of an existing iterable.
ex. `my_set2 = {char for char in "hello"}`
ex. `my_dict = {key: value**2 for key, value in simple_dict.items()}`
