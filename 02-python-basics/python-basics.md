# Python Fundamental Data Types

int = integer = Whole number
float = floating point number = Number with fractions - Floats take up more memory than normal numbers, js weird exception
bool = True or false
str = String
list = Basic array type
tuple =
set =
dict =

## Math functions

round() = Rounds number down, can take second argument for nth digit
abs() = Return absolute value

## Developer Fundamentals

Dont read the dictionary - Dont try to learn everything, learn what you need when you need it, just master the basics and whats possible
Learn by doing, do practice, projects - Youll quickly learn the most used parts of it, Pareto principle in effect :D
Learn what is possible, dont learn every action or method, just what can be done then google it

## Python also uses a similar type of rule known as PEMDAS

P – `()` - Parentheses.
E – `**` - Exponentiation.
M – `*` - Multiplication.
D – `/` - Division.
A – `+` - Addition.
S – `-` - Subtraction.

## Additional numbers

complex = Complex number type, you use this for heavy AI or Physics
Numbers are stored as binary values in memory
bin() = returns the binary value of a number

## Variables

Way to store information
`var = value` -> Assignment of variables is simple (also called binding)
VAR name best practices -> Use snake_case, start with lowercase or underscore, can include letters, numbers, underscore, case sensitive, dont overwrite keywords, make them descriptive
Tip -> Variable starting with underscore is a private variable
Tip -> Variables can be reassigned
`a,b,c = 1,2,3` -> Assign multiple values quickly

## Constants

`PI = 3.14` -> When declaring use capital letters, can be reassigned.

## Cheatsheet

[Cheatsheet](https://zerotomastery.io/cheatsheets/python-cheat-sheet/#useful-libraries)

## Expression / Statement

Expression - Piece of code that produces a value `iq/5`
Statement - Line of code that performs a action `user_age = iq / 5`

## Augmented assignment operator

Assign new value without having to retype intitial value `some_value += 5`
A initial value needs to be assigned first

## Strings

Any text contained in single or double quotes
Python also allows three single quotes, can do multiple lines

## String Concatenation

Method used to add two strings together using + ex. `print("hello" + "there")`

## Type conversions

Can change data type by using str, int, float etc.

## Escape Sequences

When using double quotes inside double quoted string need to prefix \ in front of the enclosed quotes ex. `"This is a \"hot\" day"`.
`\t` = Adds a tab spacing
`\n` = Moves code to new line

## Formatted Strings

When calling variables in string output can use f in beginning and encapsulate variables in curly brackets -
ex. `print(f"hi {name}. You are {age} years old")`
for python 2 use format instead.
ex. `print("hi {}. You are {} years old".format("Johhny", "55"))`

## String Index

Strings are indexed, so can access specific letter with call using [],
ex `print(string[0],string[1])`
Can extend call using :, which will grab from start to end of two arguments
ex `print(string[0:10])`
Can add a stepover as well as argument, so instead of iterating by 1, steps over by argument
ex `print(string[0:10:2])`
Tip - If no argument provided uses default index values, so `[::1]` will execute and output whole string from start to end stepping by 1
Tip - Can use negative value for step which will reverse string output, reverses order
ex `print(string[::-1])`

## Immutabiity

Strings are immutable, cannot be changed. Generally primitive data types are mutable ie numbers, float, strings, tuples, frozen sets
Strings can be reassigned in full but not in part using index reassignment

## Built in functions + Methods

Methods that can be used have . before and then parentheses ()

`.len()` - Displays length of string or object, useful for strings and lists especially
`.upper()` - Convert to uppercase
`.lower()` - Convert to lowercase
`.capitalize()` - Capitalizes string
`.index()` - Find index location of argument and returns it
`.counts()` - Counts occurences of argument
`.replace("haha","lol")` - Changes occurence in string with second argument

These dont change original string, they dont mutate it

## Booleans

Boolean value have to be capitalized, bool() also exists like string
not keyword for opposite value

## Developer Fundementals

Comment your code, above every line, use good comments that add value

## Lists

Basically arrays, enclosed with square brackets, data structure in python,
calling specific item same as as js - `list[0]`
reassigning is the same as js - `list[0] = "test"`
Tip - Slice method [0:0:0] also works with lists
Tip - List items can be changed, its mutable
Tip - Slicing is a non destructive method, creates new list
Tip - Lists can pass by reference when doing list1 = list2, changes to list1 will reflect in list2
Tip - Copy list without ref `list2 = list1[:]`

## Matrix - Multi dimensional list

Basically a nested array
Tip - Accessing nested value `matrix[0][1]`

## List methods

Some methods mutate original list, some dont

`len(list)` - Length of list
`append()`- Adds an element at the end of the list
`clear()` - Removes all the elements from the list
`copy()` - Returns a copy of the list
`count()` - Returns the number of elements with the specified value
`extend()` - Add the elements of a list (or any iterable), to the end of the current list
`index()` - Returns the index of the first element with the specified value
`insert()` - Adds an element at the specified position
`pop()` - Removes the element at the specified position
`remove()` - Removes the first item with the specified value
`reverse()` - Reverses the order of the list
`sort()` - Sorts the list
`in` - Logical check ex `"a" in "haha"` - returns boolean so True

## Other list methods

`range` - Create range of numbers, accepts start,stop,step
`join()` - Joins string list items with second list item in between list items
TIP - For join can use following syntax for adding empty string or character quickly
ex - `sentence = " ".join(["hi", "my", "name", "is", "JOJO"])`

## List unpacking

ex `a, b, c = [1, 2, 3]` = Assign multiple values quickly
ex `a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]` = Assign first three to variables, rest to list called other

## None

Special data type, represents absence of value

## Dictionary - Object, Hash table, map

Store data in key value pairs, is ordered, passes by reference, written with curly brackets
