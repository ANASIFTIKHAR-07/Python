"""
============================
Python Scope: A Complete Guide
============================

Table of Contents:
1. Introduction to Scope
2. The LEGB Rule
    a. Local Scope
    b. Enclosing Scope
    c. Global Scope
    d. Built-in Scope
3. The global Keyword
4. The nonlocal Keyword
5. Common Pitfalls
6. Interview Questions
7. Summary & Best Practices

============================
1. Introduction to Scope
============================
Scope refers to the region of a program where a variable is recognized. In Python, understanding scope is crucial for writing bug-free and maintainable code.

============================
2. The LEGB Rule
============================
Python resolves variable names using the LEGB rule, which stands for:
- **Local**
- **Enclosing**
- **Global**
- **Built-in**

----------------------------
a. Local Scope
----------------------------
Variables defined inside a function. Only accessible within that function.

Example:
    def my_func():
        x = 10  # Local scope
        print(x)
    my_func()  # prints 10
    # print(x)  # Error: x is not defined outside the function

----------------------------
b. Enclosing Scope
----------------------------
Variables in the local scope of enclosing (outer) functions, visible to inner (nested) functions.

Example:
    def outer():
        y = 'enclosing'
        def inner():
            print(y)  # y is from enclosing scope
        inner()
    outer()  # prints 'enclosing'

----------------------------
c. Global Scope
----------------------------
Variables defined at the top-level of a script or module, or declared global inside a function. Accessible throughout the module.

Example:
    z = 5  # Global scope
    def foo():
        print(z)
    foo()  # prints 5

----------------------------
d. Built-in Scope
----------------------------
Names preassigned by Python (e.g., print, len, list, etc.).

Example:
    print(len([1, 2, 3]))  # print and len are built-in

============================
3. The global Keyword
============================
Use `global` to modify a global variable inside a function.

Example:
    count = 0
    def increment():
        global count
        count += 1
    increment()
    print(count)  # prints 1

============================
4. The nonlocal Keyword
============================
Use `nonlocal` to modify a variable in the enclosing (non-global) scope inside nested functions.

Example:
    def outer():
        msg = 'hello'
        def inner():
            nonlocal msg
            msg = 'world'
        inner()
        print(msg)  # prints 'world'
    outer()

============================
5. Common Pitfalls
============================
- Assigning to a variable inside a function makes it local by default, even if a global variable with the same name exists.
- Using `global` or `nonlocal` incorrectly can lead to confusing bugs.
- Mutable global objects (like lists) can be modified inside functions without `global`, but rebinding requires `global`.

Example:
    x = 10
    def foo():
        x = 20  # This creates a new local variable, does not modify global x
    foo()
    print(x)  # prints 10

    my_list = [1, 2, 3]
    def bar():
        my_list.append(4)  # Modifies the global list
    bar()
    print(my_list)  # prints [1, 2, 3, 4]

============================
6. Interview Questions
============================
- What is the LEGB rule?
- How do you modify a global variable inside a function?
- What is the difference between global and nonlocal?
- What happens if you assign to a variable inside a function that has the same name as a global variable?
- Can you access variables from an enclosing function? How?
- What is the scope of a variable defined in a list comprehension in Python 3?

============================
7. Summary & Best Practices
============================
- Understand the LEGB rule for name resolution.
- Use `global` and `nonlocal` sparingly and only when necessary.
- Avoid using global variables when possible; prefer passing variables as arguments.
- Be careful with variable shadowing (using the same name in different scopes).
- Use descriptive variable names to avoid confusion.

============================
End of Guide
============================
"""








def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

time3 = make_multiplier(3)
print(time3(10)) 


def  f1():
    x = 88
    def f2():
        print(x)
    return f2

result =  f1()
# result()

def func1() :
    x = 34
    def func2():
        print(x)
    return func2
result1 = func1()
# result1()

def chaicode(num):
    def actual(x):
        return x ** num
    return actual

f = chaicode(3)
g = chaicode(2)

print(f(3))
print(g(2))