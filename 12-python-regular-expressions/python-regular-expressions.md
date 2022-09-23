# Regular Expressions - regex

- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
- Py has a good regex library, can import using `import re`
- `re` can use patterns for search

## regex tips

- Good place to test patterns - [Regex 101](https://regex101.com/)
- Generate the code on that site and insert into own code
- `r` - When placed in front of string gets treated as pure text, interpreter ignores string
- regex is good for validation of user inputs
- good regex for email - `(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`
- good regex for password - `^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d$%#@]{8,15}$` - 8 - 15 characters defined at end of regex
