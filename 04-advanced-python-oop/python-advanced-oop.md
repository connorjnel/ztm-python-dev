# Python Advanced OOP

Object Orientated Programming
Eveything in python is a object
Objects have methods and attributes that can be accessed with dot notation
OOP basically means we can create our own data types

## Classes

Naming convention is CamelCase
`Class` is like an object constructor, or a "blueprint" for creating objects.
ex. `class BigObject: pass`
`Object` different instances created from class, or instantiated from class
ex. `obj1 = BigObject()`
`__init__()` - Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created
`self` - The `self` parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
Tip - Each object is saved in a different memory location

## Attributes

Attributes - Dynamic data defined in class and instaniated using args for objects, basically object parameters defined in class
Static Attribute - Can define a static attribute in class, just normal var declaration
Tip - Class object attribute / static attribute is part of the class, doesnt change with each object

## Methods

Functions declared inside classes, become methods for objects created using class
Methods - Class methods need `self` as arg and as parent for var callbacks, linting does seem to pick this up though

## `__init__`

Constructor can have conditional checks built in, can also have default parameters
