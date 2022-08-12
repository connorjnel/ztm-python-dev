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
