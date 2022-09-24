# Python Testing

- Testing is massively important as it verifies that new code or existing code will work, can test on whole using IDE and test deployments or on micro level testing functions with unit testing
- Each module can have its own test file, custom written. Never run in production or deployed to production

## Basic forms of testing

- Python linting
- Pyflakes - type of linting
- PyCharm has its own linting
- PEP 8 - standard style guide for Python

## Writing tests - Unit tests

- Py has testing library, called unittest , `import unittest`
- Create test file, import unittest, import module being tested or function, create class - inherit unnittest.TestCase
- TestCase has multiple methods, check comparison, bool, etc
- Use try blocks to catch errors before they throw exceptions
- Use testing to break function, then refactor the function until its less likely to error out
- Test code doenst need to be refactored and optimized, readability is the core concern
- Make sure unit tests only run on correct page using `__name__`
- Run all test files - `py -m unittest`, make sure your in correct folder first.
- Can run all verbose using `py -m unittest - v`, shows full output of tests
- Can add doctring to tests for more verbose output
- `def setUp(self)` - Set up something before each test, default variable, print to terminal
- `def tearDown(self)` - Run after each test, print to terminal, reset variables etc
