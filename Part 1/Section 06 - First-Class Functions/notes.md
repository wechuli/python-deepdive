

Classes and objects have attributes - an object that is bound (to the class or the object). An attribute that is callable, is called a method.

Any object that can be called using the () operator callables always return a value.

### callables
- built-in functions
- built-in methods
- user-defined functions
- methods
- classes
- class intances
- generators,corotines, asynchronous generators

### Higher Order Functions

A function that takes a function as a parameter or returns a function

### Built in Reducing Functions
- **min**
- **max**
- **sum**
- **any**
- **all**

#### The reduce initializer
 The reduce function has a third(optional) parameter: initializer (defaults to None)
 It is specified, it is essentially like adding it to the front of the iterable.. It is often used to provide some kind of default in case the iterable is empty.

 ## Partial Functions

 Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixxed values set for the more limited function.

 ## Operator Module

 ### Item Getters
 The **itemgetter** function returns a callable.

 ### Attribute Getters

 The **attrgetter** function is similar to **itemgetter**, but is used to retrieve object attributes. It also returns a callable, that takes the object as an argument.