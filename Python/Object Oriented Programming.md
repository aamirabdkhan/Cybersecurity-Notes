# Basics
## Objects
A "bundle" of related attributes (Variables) and methods (functions)
	Example: Phone, Cup, Book.
	You need a class to create a many objects
**Attributes** --> They are variable that an Object hasw
## Class
Blueprint used to design the structure and layout of an object

## Methods
Actions that our objects can perform

# Class Variables
- Shared among all instances of a class
- Defined outside the Constructor
- Allow you to share data among all objects created from that class
- **Note** : It is a good practice to access Class Variable through class name instead of the object created through class
# Inheritance
- Allows a class to inherit attributes and methods from another class
- Helps with code reusability and extensibility
Syntax
```Inheritance
class Parent:
	color = "pink"

class Child(Parent):
	pass
```
## Multiple Inheritance
- Inherit from more than one parent class
Syntax
```Multiple
Class Father:
	color="Pink"
class Mother:
	eyes="Brown"
	
class Child(Father, Mother):
	pass
```
## Multilevel Inheritance
- Inherit from a parent which inherits from another parent
- `C(B) <- B(A) <- A`
# Abstract Classes
- A class that cannot be instantiated on it's own; Meant to be subclassed.
- They can contain abstract methods, which are declared but have no implementation.
- Abstract Classes benefits:
	1. Prevents instantiation of the class itself
	2. Requires children to use inherited abstract methods.
# Super Function `super()`
- Function used in a child class to call methods from a parent class (superclass)
- Allows you to extend the functionality of the inherited methods
### **Method Overwriting**
	- When parent and child class both have similar method methods then childs method will overwrite the parent's method; Means we will get the child method in the output
### **Method Extending**
- If we want to display parent method with the child method we can extend the method using the super() 
- syntax: `super().parent_method()`
# Polymorphism
- Greek word that means 'to have many forms and faces'
	- Poly = Many
	- Morphe = form
- Two ways to achieve polymorphism
	 1. Inheritance --> An object could be treated of the same type as a parent class
	 2. Duck Typing --> Object must have necessary attributes/methods.

## Duck Typing
- Another way to achieve polymorphism besides Inheritance
- Object must have the minimum attributes/methods
- "If it looks like a duck and quacks like a duck, It must be a duck"
# Aggregation
- Represents a relationship where one object (the whole) contains references to one or more INDEPENDENT objects (the parts)
- A relationship where one object contains references to other INDEPENDENT objects
- They have a "has-a" relationship
# Composition
- The composed object directly owns it's components, which cannot exist independently
- The have a "owns-a" relationship  
# Nested Class
- A class defined within another class
Syntax
```Nested
class Outer:
	class Inter:
```
#### Benefits
- Allows you to logically group classes that are closely related
- Encapsulates private details that aren't relevant outside of the outer class
- Keeps the namespace clean; reduces the possibility of naming conflicts   
Example:
```
class Company:
	class Employee:
		pass

class non_profit:
	class Employee:
		pass
```
# Static Methods
- A method that belong to a class rather than any object from that class (instance) usually used for general utility functions.
**Instance methods** --> Best for operations on instances of the class (objects)
**Static methods** --> Best for utility functions that do not need access to class data
# Class Methods
- Allow operations related to the class itself
- Take (cls) as the first parameter, which represents the class itself
**Instance methods** --> Best for operations on instances of the class (objects)
**Static methods** --> Best for utility functions that do not need access to class data
**Class methods** --> Best for class-level data or require access to the class itself
# Magic Methods
- Dunder Methods (Double underscore) `__init__, __str__, __eq__`
- They are automatically called by many of Python's built-in operations
- They allow developers to define or customize the behavior of objects
# Property Decorator
- Decorator used to define a method as a property (it can be accessed like an attribute)
- Benefit: Add additional logic when read, write, or delete attributes
- Gives you getter, setter, and deleter method