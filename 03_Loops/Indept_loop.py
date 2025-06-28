"""
============================
In-Depth Guide to Loops and Iteration in Python
============================

Table of Contents:
1. Introduction
2. Iterables and Iterators
3. The Iteration Protocol
4. StopIteration Exception
5. File Iteration
6. List Iteration
7. Dictionary Iteration
8. Best Practices & Notes

============================
1. Introduction
============================
Loops in Python are built on the concept of iterators and iterables. Understanding these concepts is key to mastering Python loops and iteration.

============================
2. Iterables and Iterators
============================
- **Iterable:** An object capable of returning its members one at a time (e.g., lists, tuples, dictionaries, files).
- **Iterator:** An object representing a stream of data; returned by calling `iter()` on an iterable. It has a `__next__()` method to get the next item.

Example:
    my_list = [1, 2, 3]
    it = iter(my_list)  # 'it' is now an iterator

============================
3. The Iteration Protocol
============================
- An object is iterable if it implements `__iter__()` and returns an iterator.
- An iterator must implement `__next__()` (in Python 3) and `__iter__()` (returns self).

Example:
    it = iter([10, 20, 30])
    print(next(it))  # 10
    print(next(it))  # 20
    print(next(it))  # 30
    # next(it) now raises StopIteration

============================
4. StopIteration Exception
============================
- When there are no more items, `__next__()` raises `StopIteration` to signal the end of iteration.

============================
5. File Iteration
============================
Files are iterable objects in Python. You can loop over them line by line efficiently:

Example 1: Using a for loop
    with open('loop.py') as f:
        for line in f:
            print(line, end='')

Example 2: Using readline() in a while loop
    f = open('loop.py')
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end='')
    f.close()

- Note: `readlines()` reads all lines at once and can use a lot of memory for large files. Iterating line by line is preferred.
- Files are their own iterators: `f.__iter__() is f` and `iter(f) is f` both return True.

============================
6. List Iteration
============================
Lists (and other collections) are iterable, but not iterators themselves:

    my_list = [1, 2, 3, 4]
    it = iter(my_list)  # Creates an iterator
    print(next(it))  # 1
    print(next(it))  # 2

    # my_list.__iter__() is not my_list
    # iter(my_list) is not my_list

============================
7. Dictionary Iteration
============================
Dictionaries are also iterable. You can loop over keys, values, or items:

    d = {'a': 1, 'b': 2}
    for key in d.keys():
        print(key)
    for value in d.values():
        print(value)
    for key, value in d.items():
        print(key, value)

    # Manual iteration
    it = iter(d)
    print(next(it))  # 'a' (or 'b', order is not guaranteed)

============================
8. Best Practices & Notes
============================
- Use `for` loops for most iteration tasks—they handle iterators and StopIteration for you.
- Use `with open(...) as f:` for file operations to ensure files are closed properly.
- Avoid using `readlines()` on large files.
- Any object that implements `__iter__()` or `__getitem__()` (with integer keys starting at 0) is iterable.
- You can create your own iterator by defining `__iter__()` and `__next__()` in a class.
- Iter object is by default in file, but not by default in list, dict etc [have to manually make a variable with iter].
- So, from this short difference we can conclude that, when we store a file in a variable, it becomes a iterable object by 
- it's own. But when we store the list in a variable, that is not it's iterable object. It's just it's actual object reference.

============================
Summary
============================
- Iteration is a core concept in Python, used everywhere from loops to comprehensions.
- Understanding the difference between iterables and iterators, and how the iteration protocol works, will make you a better Python programmer.
"""

#  Here we will learn about the indepth logic of the loops.

#  So, in python the loops are also called the iterators and python have different iterator tools and iterable objects
#  On which the iterator tools iterates and the third thing is __check__ => This is the reponse.
#  The __check__ gives the tools the memory address of the object and displays the first number/value in the memory.
#  Also it has a StopIteration exception to identify that there is no value ahead.
#  One thing which i forgot mentioning is that the iteration tools send a iter() to the objects especially file.
#  Because only the file brings it's own iter tools. No other type has it's own.

#  Now, first we will discuss about the file iterable object. Know as file data type:

f  =  open('loop.py')

#  We can apply method to iterate the lines of code of this file.

f.readline()
#  This is based on the iterate engine of python and gives us the individual line developer friendly.
# f.__check__() 
#  This is the raw version of the previous one. The read line use this on the backend. This tells us the stopiteration error
#  When there is no more line of code in the file

#  We can also apply loop on it

for lines in open('loop.py'):
    print(lines)

#  Initially there is a readlines() method which was used in the loops with (.). But now it is not used as it was making a 
# burden on the memory.
#  Now, one interesting point here, and that is it will stop after iterating the last line when it reaches the last line.
#  How's that possible? Because in the backend they are made according to the engine we talked about and they are 
# iterateable tools. 

while True:
    line = f.readline()
    if not line:
        break
    print(line, end= '')

#  iter() tool for the list.

list = [1,2,3,4]
i = iter(list)  # This iter() method or tool is applied on the iterable objects.
#  Now, what does it show. It shows the memory address of the first value of the iterable object. One interesting thins also
#  Is that when iteration is occuring the i , iter() does not changee the address of memory because, the __next__
#  has an additional pointer which is iterating through the values of the address of the iterable object.
#  The address doesn't changes, the valuse changes as it iterates=> This is frequently asked in interviews.
#  The file has the iter() by default. We don't have to manually assign the file variable manually, it is automatically 
#  done in the python's backend

#  If we check you will know that:

# f.__iter__() is f # They both will return True
# iter(f) is f 

#  BUT WHAT WILL HAPPEN IN THE CASE OF LIST. LET'S SEE:

newlist = [2,3,4,5,6]

# iter(newlist) is newlist # This will return false

#  Why that happens: It's because when we store the file in a variable it becomes a iterable object. But when we store a
#  list in a variable or have given the name of it in memory reference,it is not its iterable object, that's just the 
#  reference of the actual object
#  Apart from these two there are some other also which are iterables:

#  DiCTIONARY:

d = {
    'a' : '1',
    'b' : '2'
}

for key in d.keys():
    print(key)

#  If we want to do this manually:

i = iter(d)
#  This will give the address of memory reference

#  The iter method is also applicable on the range()

# R = range(5)
# i = iter(R)

# next(i)
