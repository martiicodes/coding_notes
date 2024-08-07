# Lists

[Source](https://automatetheboringstuff.com/2e/chapter4/)

List data type and its cousin, the tuple.

## The List Data Type

A list is a value that contains multiple values in an ordered sequence.

Values inside the list are also called items. 
Items are separated with commas (that is, they are comma-delimited).

## Getting Individual Values in a List with Indexes

Indexes can be only integer values, not floats.

Lists can also contain other list values. The values in these lists of lists can be accessed using multiple indexes.

Negative Indexes

While indexes start at 0 and go up, you can also use negative integers for the index. The integer value -1 refers to the last index in a list, the value -2 refers to the second-to-last index in a list, and so on. 

## Getting a List from Another List with Slices

## Getting a List’s Length with the len() Function

The len() function will return the number of values that are in a list value passed to it, just like it can count the number of characters in a string value.

## Working with Lists

When you first begin writing programs, it’s tempting to create many individual variables to store a group of similar values.

It turns out that this is a bad way to write code.

Instead of using multiple, repetitive variables, you can use a single variable that contains a list value.

## Using for Loops with Lists

You learned about using *for loops* to execute a block of code a certain number of times. 

Technically, a *for loop* repeats the code block once for each item in a list value. 

    for i in range(4):
        print(i)

the output of this program would be as follows:

0
1
2
3

## The in and not in Operators

You can determine whether a value is or isn’t in a list with the **in** and **not** in operators. 

Like other operators, in and not in are used in expressions and connect two values: a value to look for in a list and the list where it may be found. 

These expressions will evaluate to a Boolean value. 

## Augmented Assignment Operators

## Methods

A method is the same thing as a function, except it is “called on” a value.

The method part comes after the value, separated by a period.

Each data type has its own set of methods.

## Sequence Data Types

Lists aren’t the only data types that represent ordered sequences of values.

The Python sequence data types include lists, strings, range objects returned by range(), and tuples.

Many of the things you can do with lists can also be done with strings and other values of sequence types: indexing; slicing; and using them with for loops, with len(), and with the in and not in operators.

## The Tuple Data Type

The tuple data type is almost identical to the list data type, except in two ways. 

First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ].

But the main way that tuples are different from lists is that tuples, like strings, are *immutable*.

Tuples cannot have their values modified, appended, or removed.

## Summary

Lists are useful data types since they allow you to write code that works on a modifiable number of values in a single variable.

Lists are a sequence data type that is mutable, meaning that their contents can change. 

Tuples and strings, though also sequence data types, are immutable and cannot be changed.

A variable that contains a tuple or string value can be overwritten with a new tuple or string value, but this is not the same thing as modifying the existing value in place—like, say, the append() or remove() methods do on lists.

Variables do not store list values directly; they store *references* to lists.

This is an important distinction when you are copying variables or passing lists as arguments in function calls. Because the value that is being copied is the list reference, be aware that any changes you make to the list might impact another variable in your program. 
You can use copy() or deepcopy() if you want to make changes to a list in one variable without modifying the original list.
