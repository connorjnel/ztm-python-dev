# Modules

- Break code into multiple files, easier for debugging, scaling up.
- Modules are bascially just different .py files
- Can import entire file into other file or specific functions only using `from`
- Can use aliases for modules using `as`

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
