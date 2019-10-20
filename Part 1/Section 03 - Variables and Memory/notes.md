# Variables and Memory

Objects are stored on the heap and the heap is managed by the Python Memory Manager.

In Python, we can find out the memory address referenced by a variable by using the id() function.

## Reference Counting

In computer science, refernce counting is a programming technique of storing the number of references, pointers or handles to a resource, such as an object , a block of memory, disk space and others. In garbage collection algorithms, reference counts may be used to deallocate objects which are no longer needed.

Python memory manager is responsible for reference counting.

### Memory leak

In computer science, a memory leak is a type of resource leak that occurs when a computer program incorrectly manages memory allocations in such a way that memory which is no longer needed is not released. A memory leak may also happen when an object is stored in memory but cannot be accessed by the running code.

### Garbage collector

In computer science, garbage collection is a form of automatic memory management. The garbage collector, or just collector, attempts to reclaim garbage or memory occupied by objects that are no longer in use by the program.

The oython

### Dynamic Vs Static Typing

A statically typed language variables' types are static, meaning once you set a variable to a type, you cannot change it. This is because typing is associated with the variable rather than the object it refers to.
A dynamically typed language variables' types are dynamic, meaning after you set a variable to a type, you CAN change it. That is because typing is associated with the value it assumes rather than the variable itself.

### Object Mutability

An object whose internal state can be changed is called mutable.
An object whose internal state cannot be changed is called immutable.

#### Immutable Data types

- Numbers (int,float,Booleans etc)
- Strings
- Tuples
- Frozen Sets
- User-Defined Classes

#### Mutable Types

- Lists
- Sets
- Dictionaries
- User-Defined Classes

## Function Arguments and Mutability

- Immutable objects are safe from unintended side-effects but watch out for immutable collection objects that contain mutable objects.
- Mutable objects are not safe from unintended side effects.

## Shared References and Mutability

The term shared reference is the concept of two variables referencing the same object in memory (i.e. having the same memory address)

In some cases, Python's memory manager may decide to automatically reuse memory references for immutable types.
When working with mutable objects, we have to be more careful. With mutable objects, the Python memory will never create shared reference.

## Variable Equality

We can think of variable equality in two fundamentally different ways:

- **Memory Address** - we use **is**
- **Object State**

### The None object

The None object can be assigned to variables to indicate that they are not set (in the way we would expect them to be) i.e. an 'empty' value (or null pointer)
But the **None** object is a real object that is managed by the Python memory manager
Furthermore, the memory manager will always use a shared reference when assiging a variable to **None**

So we can test if a variable is 'not set' or empty by comparing it's memory address to the memory address of **None** using the **is** operator.