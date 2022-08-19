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
