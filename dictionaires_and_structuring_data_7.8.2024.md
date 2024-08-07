# Dictionaires and Structuring Data

Dictionary data type, which provides a flexible way to access and organize data.

## The Dictionary Data Type

Like a list, a dictionary is a *mutable* collection of many values.

But unlike indexes for lists, indexes for dictionaries can use many different data types, not just integers. 

Indexes for dictionaries are called *keys*, and a key with its associated value is called a *key-value pair*.

In code, a dictionary is typed with braces, {}.

### Dictionaries vs. Lists

Unlike lists, items in dictionaries are *unordered*.

But there is no “first” item in a dictionary. While the order of items matters for determining whether two lists are the same, it does not matter in what order the key-value pairs are typed in a dictionary.

Because dictionaries are not ordered, they can’t be sliced like lists.

Though dictionaries are not ordered, the fact that you can have arbitrary values for the keys allows you to organize your data in powerful ways.

### The keys(), values(), and items() Methods

There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys and values: keys(), values(), and items().

The values returned by these methods are not true lists: they cannot be modified and do not have an append() method.

But these data types (dict_keys, dict_values, and dict_items, respectively) can be used in *for* loops.

A *for loop* can also iterate over the *keys* or *both keys and values*.

Notice that the values in the dict_items value returned by the items() method are tuples of the key and value.

If you want a true list from one of these methods, pass its list-like return value to the list() function.

### The get() Method

It’s tedious to check whether a key exists in a dictionary before accessing that key’s value. 

Fortunately, dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.

## Pretty Printing

If you import the pprint module into your programs, you’ll have access to the pprint() and pformat() functions that will “pretty print” a dictionary’s values. 

This is helpful when you want a cleaner display of the items in a dictionary than what print() provides. 



