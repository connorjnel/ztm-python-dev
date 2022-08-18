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

## Class methods and static methods

`@classmethod`
`def example_function(cls):`
Class methods don't need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python.
Tip. Can be used without instantiating a class.

`@staticmethod`
`def example_function():`
Static methods are methods that are related to a class in some way, but don't need to access any class-specific data. You don't have to use self, and you don't even need to instantiate an instance, you can simply call your method:

## Dev fundamental 5 - Test assumptions

Test my understanding, if you dont know how it works try to code it, read docs about it, do some tests
`Self` refers to itself, refers to current instance of the class, so if i run it on obj1 it refers to obj1

## 4 Pillars of OOP

### Encapsulation

Using classes that has data and actions in a single blueprint, dont have to repeat yourself

### Abstraction

Dont need to know the smallest detail of how something works, methods and attributes exist that take it out of our hands, good to be curious and look into but not the most efficient use of time

### Inheritance

Allows new objects to inherit properties of existing objects, can inherit classes. Obj can have multiple classes. To inherit from parent class just pass in parent class name into arg of child class.
Need to have parent class and child classes, sometimes called sub classes
`isinstance(instance,class)` - Check if instance is a instance of a specified class.
Tip - Python has a super parent object class, contains dunder methods

## Polymorphism

Object classes can share the same method name, those methods act differently depending on which object calls them

## Private vs public variables

`_var` - Python convention stating that its a private function/variable, dont edit it. Just tells devs not to touch it
`__var__` - Dunder methods, do not edit these

## Super

The super() function is used to give access to methods and properties of a parent or sibling class.
ex. `super().__init__(arg)` - pulls from parent, dont need to add self
ex. `Parent.__init__(self, arg)` - fallback older method
Tip. Remember to add arg in child class that is being pulled from super in child declaration

## Object Introspection

Ability the type of a object at runtime
`dir(obj)` - The dir() function returns all properties and methods of the specified object, without the values.

## self

The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

## Dunder Methods

Special magic methods, not meant to be modified usually but can be redeclared in classes to change the behavior when that specific magic method is called on objects created using that class

## Multiple Inheritances

Object can have multiple inheritances.
Need to init and import parameters from parent classes
ex .`class Hybrid(Wizard, Archer):def __init__(self, name, power, num_arrows):Archer.__init__(self, name, num_arrows)Wizard.__init__(self, name, power)`
