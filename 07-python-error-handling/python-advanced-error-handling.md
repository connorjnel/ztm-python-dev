# Python Advanced Error handling

Python throws a error, or a exception when it runs into a issue and stops execution
Error handling lets script continue even if error happens

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:
The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.
The `finally` block lets you execute code, regardless of the result of the try- and exWcept blocks.
ex. `try: print(x) except: print("An exception occurred")`

The `raise` keyword is used to raise an exception, can display custom error message without having to use print
The `break` keyword is used to break out a for loop, or a while loop.
The `continue` keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

Tip. Dont use bare except, it catches all errors, define excetion error being caught
ex `except ValueError:`
Tip. Use descriptive outputs for except print identifying issue
Tip. Finally runs regardless at the end, can use to log incomplete actions
