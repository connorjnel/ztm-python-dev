# Modules

- Break code into multiple files, easier for debugging, scaling up.
- Modules are bascially just different .py files
- Can import entire file into other file or specific functions only using `from`
- Can use aliases for modules using `as`, good for avoiding name collision

## Tips

- `import` - The import keyword is used to import modules.

## Loop Tips

- `break` - The break statement in Python terminates the current loop and resumes execution at the next statement, just like the traditional break found in C. The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.
- `continue` - The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop. The continue statement can be used in both while and for loops.
- `else` - Python supports to have an else statement associated with a loop statements. If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list. If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

## Packages

- Package is a folder containing modules
- To import use folder.file ex. shopping.shopping_cart
- To help with long paths to functions can import function only using `from`. Can import multiple with `,` divider
- Be aware of name collissions, when importing function if it already existed will override, use alias for function colliding or change the function name

## Name

- `if __name__ == "__main__":` - Conditional to run code only if on main file
- `__name__` - Outputs the simple path for file
- `__main__` - This refers to main .py file that is being run, when you run `__name__` on it will get named `__main__`

## Built in modules

- Python interpreter has a number of built-in modules. Just need to be imported for use, VSCODE auto completes
- There are thousands of Python modules and more are getting developed every day.
- Module Index - [Module Index](https://docs.python.org/3/py-modindex.html)
- help(module) - Shows manual for module
- dir(module) - Shows the functions available from module
- random - Nice random module, does a few random functions such as randint, shuffle, choice

## Package Index

- Built in modules are referred to as the standard library
- Lots of other libraries have been built for py that can be imported - used with pip install, kinda like npm?
- [Python package index](https://pypi.org/)
- Check standard py library first before using a community package

## PIP Install

- Use terminal to install, command usually in package
- To install `pip install package-name`
- To uninstall `pip uninstall package-name`
- Can install older version `pip install package-name ==0.5.0`
- Can update packages `pip install package-name --upgrade` or `pip install package-name -U`

## Virtual Environments

- PyCharm has virtual environment built in
- PyCharm better for larger projects
- pipenv a lower end solution `pip install pipenv`

## Useful modules - from collections & datetime &

- `counter` - Creates dict and counts how many times item occurs in iterable
- `defaultdict` - Dict with default factory, The default factory is called without arguments to produce a new value when a key is not present
- Dict are now ordered by default in py 3.7, so only need to use OrderedDict in older codebases
- `OrderedDict` - Dictionary that remembers insertion order
- `datetime` - Concrete date/time and related types
- `array` - Return a new array whose items are restricted by typecode, and initialized from the optional initializer value, faster than list

## Developer Fundamentals

- Packages are not always the best idea, they can be coded badly, can have bugs, security exploits, out of date
- Libraries that are added add weight, they slow down the execution, use when writing something yourself will take longer than using library
