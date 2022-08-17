# Python Basics 2

## Conditional Logic

Similar to JS, basic programming concept tbh, if condition: action, elif condition: action, else: action
Tip - elif basically just else if
`and` = Returns True if both statements are true
`or` = Returns True if one of the statements is true
`not` = Reverse the result, returns False if the result is true
Tip - Indentation in python super important

## Truthy and Falsy

Basically type coercion that converts data types to boolean values, fundemantal of computing in action

Truthy - Values that positive ie non-empty string, number, list etc then its true,
Falsy - Values are are nothing ie None , empty string, empty list, dict will be false

## Ternary Operator

Shorthand conditional logic
ex. `condition_if_true if condition else condition_if_else`

## Short circuiting

When doing logical conditional check using `or` then its faster than `and` because expression can evaluate after first condition and skip checking second condition. For `and` if first is false then also short circuits and doesnt check second.

## Logical Operators

`==` - Equal, check for equality of value
`!=` - Not equal
`>` - Greater than
`<` - Less than
`>=` - Greater than or equal to
`<=` - Less than or equal to
`and` - Returns True if both statements are true
`or` - Returns True if one of the statements is true
`not` - Reverse the result, returns False if the result is true

## is vs ==

`==` - Equal, check for equality of value
`is` - Checks if location in memory is the same

## Loops

`for item in [1, 2, 3, 4, 5]:print(item + 5)`
Loop very similar to JS, very simple format

## Iterable Items

Object that can be iterated through, string, list, dictionary, set, tuple
Int and float are not iterable

## Iterating through dict

`for item in users.items():` - Iterate and return the full dict with key and values as a tuple
`for item in users.values():` - Iterate and return the dict values
`for item in users.keys():` - Iterate and return the dict keys
`for key, value in users.items(): print(key, value)` - Uncouple from tuple and print keys and values

## Ranges

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
Tip - When not caring about var can use underscore as var placeholder `_`
Tip - To go in reverse need to use negative for step value ie `-1`

## Enumerate

The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
Useful if you need a index counter for a list, tuple etc

## While Loop

With the while loop we can execute a set of statements as long as a condition is true.
Tip - Can add final action with else statement, else block only executes once while is false, break usage in while will negate else
Tip - While loop for more complex loops with condition or you dont know how long loops needs to run
Tip - While loops with True can exit indefinitely until false, just remember break
`break` - With the `break` statement we can stop the loop even if the while condition is true:
`continue` - Stop current iteration, and continue with next iteration
`pass` - Not very useful, basically can use as placeholder for incomplete loop

## Developer Fundamentas - Good code

Code is clean, follows best standards, easily readable
Use comments to illustrate what expressions do or why it is written that way
Predictability, keep it simple and makes sense, easily readable
DRY, do not repeat yourself

## Functions

`def say_hello():` - How to define functions
`say_hello()` - Call function

## Argument vs parameters

A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

## Default parameters

Normal parameters are positional, they output in the order they were defined in function
Keyword argument - When calling function can use param_value="string", basicaly forcing position change when calling the function
Default argument - Define in function parameter with param="default", only used when no argument provided

## Return

The `return` keyword is to exit a function and return a value.
Functions need to return something, if they done they just output `None`
Functions should do one thing really well, functions should return something
`return` keyword exits the function, ie if statement following return wont get run

## Methods vs Functions

Python have built in functions, called with param ie `list()`
Python methods used dot notation ie. `"haha.capitalize()`

## Docstrings

Comment using `'''Info'''`, do this inside function and then emmett can pick up the info we wrote about function, super useful
Can also be called with `help(function)`, not just in code editor

## Clean Code

Keep code simple, get rid of redundant code, dont use conditions if you can use straight return

## Args and Kwargs

`*args` - Allows multiple arguments to be added even though one was defined in function
`**kwargs` - Allows usage of multiple keyword args even though only one was defined
Order for arguments in envocation - `Rule: params, *args, default parameters, **kwargs`

## Walrus operator

`:=` - Allows you to assign values to variables as part of a larger expression, use parentheses.
ex `if ((n := len(a)) > 10):` - Now we can use `n` in further statements without having to redo the len(a)
