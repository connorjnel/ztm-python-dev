# Modules

- Break code into multiple files, easier for debugging, scaling up.
- Modules are bascially just different .py files
- Can import entire file into other file or specific functions only using `from`
- Can use aliases for modules using `as`, good for avoiding name collision

## Tips

- `import` - The import keyword is used to import modules.

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
