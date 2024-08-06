# Functions

[Source](https://automatetheboringstuff.com/2e/chapter3/)

Python provides several built-in functions, but you can also write your own functions. 

**A function is like a miniprogram within a program.**

A major purpose of functions is to group code that gets executed multiple times. Without a function defined, you would have to copy and paste this code each time.

In general, you always want to avoid duplicating code because if you ever decide to update the code—if, for example, you find a bug you need to fix—you’ll have to remember to change the code everywhere you copied it.

**Deduplication** makes your programs shorter, easier to read, and easier to update.

## def Statements with Parameters

When you call the print() or len() function, you pass them **values**, called **arguments**, by typing them *between the parentheses*.

**Parameters** are **variables** that contain **arguments**.

When a function is called with arguments, the arguments are stored in the parameters.

One special thing to note about parameters is that the value stored in a parameter is forgotten when the function returns.

This variable is destroyed after the function call hello('Bob') returns, so print(name) would refer to a name variable that does not exist.

This is similar to how a program’s variables are forgotten when the program terminates.

## Define, Call, Pass, Argument, Parameter

To define a function is to create it, just like an assignment statement like spam = 42 creates the spam variable.

    ➊ def sayHello(name):
       print('Hello, ' + name)
➋ sayHello('Al')

The def statement defines the sayHello() function ➊.

The sayHello('Al') line ➋ calls the now-created function, sending the execution to the top of the function’s code.

This function call is also known as passing the string value 'Al' to the function. 

A value being passed to a function in a function call is an argument.

The argument 'Al' is assigned to a local variable named name.

Variables that have arguments assigned to them are parameters.

## Return Values and return Statements

In general, the value that a function call evaluates to is called the *return value of the function*.

When creating a function using the *def statement*, you can specify what the *return value* should be with a *return statement*. 

A return statement consists of the following:

- The return keyword
- The value or expression that the function should return

Note that since you can pass return values as an argument to another function call, you could shorten these three lines:

    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)

to this single equivalent line:

    print(getAnswer(random.randint(1, 9)))

Remember, **expressions are composed of values and operators**. 
A function call can be used in an expression because the call evaluates to its return value.

## The None Value

In Python, there is a value called **None**, which represents the *absence of a value*.

The None value is the only value of the NoneType data type. 
(Other programming languages might call this value null, nil, or undefined.)

Just like the Boolean True and False values, None must be typed with a capital N.

This value-without-a-value can be helpful when you need to store something that won’t be confused for a real value in a variable. 

One place where None is used is as the return value of print(). The print() function displays text on the screen, but it doesn’t need to return anything in the same way len() or input() does. But since all function calls need to evaluate to a return value, print() returns None.

Behind the scenes, Python adds return None to the end of any function definition with no return statement. This is similar to how a while or for loop implicitly ends with a continue statement. Also, if you use a return statement without a value (that is, just the return keyword by itself), then None is returned.

## Keyword Arguments and the print() Function

Most *arguments* are identified by their position in the function call.

However, rather than through their position, *keyword arguments* are identified by the keyword put before them in the function call.

*Keyword arguments* are often used for *optional parameters*.

For example, the print() function has the optional parameters end and sep to specify what should be printed at the end of its arguments and between its arguments (separating them).

print() function automatically adds a newline character to the end of the string it is passed.

## The Call Stack
(nije mi baš najjasnije)

The *conversation* is **stack-like** because the *current topic is always at the top of the stack*.

The call stack is how Python remembers where to return the execution after each function call.

The call stack isn’t stored in a variable in your program;
rather, Python handles it behind the scenes.

When your program calls a function, Python creates a **frame object** on the top of the call stack.

*Frame objects* store the line number of the original function call so that Python can remember where to return. 

It’s enough to understand that function calls return to the line number they were called from.

## Local and Global Scope

Parameters and variables that are assigned **in** a called function are said to exist in that function’s *local scope*.

Variables that are assigned **outside** all functions are said to exist in the *global scope*. 

A variable that exists in a local scope is called a *local variable*, while a variable that exists in the global scope is called a *global variable*. 

A variable must be one or the other; it cannot be both local and global.

Think of a **scope as a container for variables**. When a scope is destroyed, all the values stored in the scope’s variables are forgotten.

There is only one global scope, and it is created when your program begins.

When your program terminates, the global scope is destroyed, and all its variables are forgotten.

A local scope is created whenever a function is called. Any variables assigned in the function exist within the function’s local scope.

When the function returns, the local scope is destroyed, and these variables are forgotten.

Local variables are also stored in frame objects on the call stack.

*Scopes* matter for several reasons:

- Code in the global scope, outside of all functions, cannot use any local variables. 

- However, code in a local scope can access global variables.

- Code in a function’s local scope cannot use *variables* in any other local scope.

- You can use the same name for different variables if they are in different scopes.

The reason Python has different scopes instead of just making everything a global variable is so that when variables are modified by the code in a particular call to a function, the function interacts with the rest of the program only through its parameters and the return value.

This narrows down the number of lines of code that may be causing a bug.

While using global variables in small programs is fine, it is a bad habit to rely on global variables as your programs get larger and larger.

Multiple local scopes can exist at the same time.

Local variables in one function are completely separate from the local variables in another function.

## The global Statement

If you need to modify a global variable from within a function, use the *global* statement. 

If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.”

There are four rules to tell whether a variable is in a local scope or global scope:

1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

2. If there is a global statement for that variable in a function, it is a global variable.

3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

4. But if the variable is not used in an assignment statement, it is a global variable.

### FUNCTIONS AS “BLACK BOXES”

Often, all you need to know about a function are its inputs (the parameters) and output value; you don’t always have to burden yourself with how the function’s code actually works. When you think about functions in this high-level way, it’s common to say that you’re treating a function as a **“black box.”**

This idea is fundamental to modern programming. Later chapters in this book will show you several modules with functions that were written by other people. While you can take a peek at the source code if you’re curious, you don’t need to know how these functions work in order to use them. And because writing functions without global variables is encouraged, you usually don’t have to worry about the function’s code interacting with the rest of your program.

## Exception Handling

A ZeroDivisionError happens whenever you try to divide a number by zero.

**Errors** can be handled with *try* and *except* statements.

The code that could potentially have an error is put in a **try clause**.
The program execution moves to the start of a following **except clause** if an error happens.

    def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

When code in a try clause causes an error, the program execution immediately moves to the code in the except clause. 
After running that code, the execution continues as normal. 

The output of the previous program is as follows:

21.0
3.5
Error: Invalid argument.
None
42.0

Note that any errors that occur in function calls in a *try* block will also be caught. 

Consider the following program, which instead has the spam() calls in the *try* block:

    def spam(divideBy):
        return 42 / divideBy
    
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(1))
    except ZeroDivisionError:
        print('Error: Invalid argument.')

When this program is run, the output looks like this:

21.0
3.5
Error: Invalid argument.

The reason print(spam(1)) is never executed is because once the execution jumps to the code in the except clause, it does not return to the try clause. Instead, it just continues moving down the program as normal.

## Summary

Functions are the primary way to compartmentalize your code into logical groups.

Since the variables in functions exist in their own local scopes, the code in one function cannot directly affect the values of variables in other functions. This limits what code could be changing the values of your variables, which can be helpful when it comes to debugging your code.

Functions are a great tool to help you organize your code. You can think of them as black boxes: they have inputs in the form of parameters and outputs in the form of return values, and the code in them doesn’t affect variables in other functions.

You learned about *try* and *except* statements, which can run code when an error has been detected. This can make your programs more resilient to common error cases.










