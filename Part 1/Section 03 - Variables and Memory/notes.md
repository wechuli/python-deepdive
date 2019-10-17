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
