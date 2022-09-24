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
