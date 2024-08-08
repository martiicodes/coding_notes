# Manipulate Strings

[Soource](https://automatetheboringstuff.com/2e/chapter6/)

Text is one of the most common forms of data your programs will handle.

## Working with Strings

### String Literals

Typing string values in Python code is fairly straightforward: they begin and end with a single quote.

    >>> spam = "That is Alice's cat."

Since the string begins with a double quote, Python knows that the single quote is part of the string and not marking the end of the string. However, if you need to use both single quotes and double quotes in the string, you’ll need to use escape characters.

### Escape Characters

An escape character lets you use characters that are otherwise impossible to put into a string. An escape character consists of a backslash (\) followed by the character you want to add to the string.

Escape character Prints as
\'               Single quote
\"               Double quote
\t               Tab
\n               Newline (line break)
\\               Backslash

## Raw Strings

You can place an r before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string

## Putting Strings Inside Other Strings

Putting strings inside other strings is a common operation in programming.

A simpler approach is to use string interpolation, in which the %s operator inside the string acts as a marker to be replaced by values following the string. 
One benefit of string interpolation is that str() doesn’t have to be called to convert values to strings.

Python 3.6 introduced f-strings, which is similar to string interpolation except that braces are used instead of %s, with the expressions placed directly inside the braces.
Like raw strings, f-strings have an f prefix before the starting quotation mark.

## Useful String Methods

Several string methods analyze strings or create transformed string values.

### The upper(), lower(), isupper(), and islower() Methods

The upper() and lower() string methods return a new string where all the letters in the original string have been converted to uppercase or lowercase, respectively. 

Nonletter characters in the string remain unchanged.

Note that these methods do not change the string itself but return new string values. 
If you want to change the original string, you have to call upper() or lower() on the string and then assign the new string to the variable where the original was stored. 
This is why you must use spam = spam.upper() to change the string in spam instead of simply spam.upper().

### The isX() Methods

Along with islower() and isupper(), there are several other string methods that have names beginning with the word is. These methods return a Boolean value that describes the nature of the string. 

Here are some common isX string methods:

- *isalpha()* Returns True if the string consists only of letters and isn’t blank.
- *isalnum()* Returns True if the string consists only of letters and numbers and is not blank.
- *isdecimal()* Returns True if the string consists only of numeric characters and is not blank.
- *isspace()* Returns True if the string consists only of spaces, tabs, and newlines and is not blank.
- *istitle()* Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

### The startswith() and endswith() Methods

The startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively) with the string passed to the method; otherwise, they return False.

### The join() and split() Methods

The join() method is useful when you have a list of strings that need to be joined together into a single string value. The join() method is called on a string, gets passed a list of strings, and returns a string. The returned string is the concatenation of each string in the passed-in list. 

### Splitting Strings with the partition() Method

The partition() string method can split a string into the text before and after a separator string. 

### Justifying Text with the rjust(), ljust(), and center() Methods

The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text. 
The first argument to both methods is an integer length for the justified string.

### Removing Whitespace with the strip(), rstrip(), and lstrip() Methods

Sometimes you may want to strip off whitespace characters (space, tab, and newline) from the left side, right side, or both sides of a string. The strip() string method will return a new string without any whitespace characters at the beginning or end. 

The lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively.

## Numeric Values of Characters with the ord() and chr() Functions

Computers store information as bytes—strings of binary numbers, which means we need to be able to convert text to numbers.

Because of this, every text character has a corresponding numeric value called a *Unicode code point*.

You can use the ord() function to get the code point of a one-character string, and the chr() function to get the one-character string of an integer code point.

These functions are useful when you need to do an ordering or mathematical operation on characters.

## Copying and Pasting Strings with the pyperclip Module

The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard. 
Sending the output of your program to the clipboard will make it easy to paste it into an email, word processor, or some other software.









