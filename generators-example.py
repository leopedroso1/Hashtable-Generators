# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:20:42 2021

@author: Leonardo
"""

"""
Generators is a powerfull python mechanism that retain the state of some function/object, in other words
you checkpoint the processing being able to return from that point instead starting all over again, hence improving the performance. 

They´re commonly used when you need to work with massive processing for data in special for streamming data and file processing. 
For example, imagine that you need to compute massively the rows in a file reading operation.

In order to understand properly the power of generators, firstly we need to understand the 'yield' keyword.
"""

"""
Yield Keyword:
    The yield statement suspends function’s execution and sends a value back to the caller, 
but retains enough state to enable function to resume where it is left off. 
    
    When resumed, the function continues execution immediately after the last yield run. 
    
    This allows its code to produce a series of values over time, 
rather than computing them at once and sending them back like a list.

"""

# Generates squares from 1 to 100 using yield, therefore a generator
def nextSquare():
    i = 1
    while True:
        yield i * i
        i += 1

print("Generates square numbers from 1 to 100")
for num in nextSquare():
    if num > 100:
        break;
    print(num)

"""
Generator Functions: 
    They´re like any normal function, but whenever it needs to generate a value,  
it does so with the 'yield' keyword rathen than return. If the body of a def constraints yield, the
function automatically becomes a generator function.
"""  

def myFunnyGenerator():
    yield 1
    yield 2
    yield 3

print("\nGenerator Function")    
for value in myFunnyGenerator():
    print(value)
    
    
"""
Generator Objects:
    Generator functions return a generator object. Those objects are used either by calling the 'next'
    method on the generator object or using the generator object in a 'for in' loop.
"""

# x stands for generator object
x = myFunnyGenerator()

print("\nGenerator Object")
print(x.__next__())
print(x.__next__())
print(x.__next__())

"""
Remember: A generator function return an generator object that is iterable, i.e, can be used as an Iterators
let´s see an example using generator for Fibonacci Numbers   
"""

def fibonacci(limit):
    a, b = 0, 1
    
    while a < limit:
        yield a
        a, b = b, a + b

#x = fibonacci(5)
#x.__next__()

print("Fibonacci Generator")
for i in fibonacci(50):
    
    print(i)
    
# More content at >> http://www.dabeaz.com/finalgenerator/