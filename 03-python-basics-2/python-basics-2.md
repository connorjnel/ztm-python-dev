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
Tip - With the `break` statement we can stop the loop even if the while condition is true:
Tip - Can add final action with else statement, else block only executes once while is false, break usage in while will negate else
