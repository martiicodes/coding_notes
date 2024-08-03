# Flow control 

Flow control statements can decide which Python instructions to execute under which conditions.

**Flowcharts** represent these branching points with diamonds, while the other steps are represented with rectangles. The starting and ending steps are represented with rounded rectangles.

## Boolean Values

While the integer, floating-point, and string data types have an unlimited number of possible values, the Boolean data type has only two values: True and False. 

## Comparison Operators

Comparison operators, also called relational operators, compare two values and evaluate down to a single Boolean value. 

==
Equal to

!=
Not equal to

<
Less than

>
Greater than

<=
Less than or equal to

>=
Greater than or equal to

## Boolean Operators

The three Boolean operators (and, or, and not) are used to compare Boolean values. Like comparison operators, they evaluate these expressions down to a Boolean value. Let’s explore these operators in detail, starting with the and operator.

### Binary Boolean Operators

The and and or operators always take two Boolean values (or expressions), so they’re considered binary operators. The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False. Enter some expressions using and into the interactive shell to see it in action.

## Mixing Boolean and Comparison Operators

(4 < 5) and (5 < 6)
True

(4 < 5) and (9 < 6)
False

(1 == 2) or (2 == 2)
True

## Elements of Flow Control

Flow control statements often start with a part called the condition and are always followed by a block of code called the clause.

### Conditions

The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions; condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False. A flow control statement decides what to do based on whether its condition is True or False, and almost every flow control statement uses a condition.

### Blocks of Code

- Blocks begin when the indentation increases.
- Blocks can contain other blocks.
- Blocks end when the indentation decreases to zero or to a containing block’s indentation.

## Program Execution

In the previous chapter’s hello.py program, Python started executing instructions at the top of the program going down, one after another. The program execution (or simply, execution) is a term for the current instruction being executed.

## Flow Control Statements

### *if* Statements

The most common type of flow control statement is the if statement. An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the condition is False.

...an if statement could be read as, “If this condition is true, execute the code in the clause.” In Python, an if statement consists of the following:

- The if keyword
- A condition (that is, an expression that evaluates to True or False)
- A colon
- Starting on the next line, an indented block of code (called the if clause)

All *flow control statements* end with a colon and are followed by a new block of code (the clause).

This *if statement’s clause* is the block with print('Hi, Alice.').

### *else* Statements

An if clause can optionally be followed by an else statement. The else clause is executed only when the if statement’s condition is False.

“If this condition is true, execute this code. Or else, execute that code.”

An else statement doesn’t have a condition, and in code, an else statement always consists of the following:

- The else keyword
- A colon
- Starting on the next line, an indented block of code (called the else clause)

### elif Statements

While *only one* of the **if** or **else** clauses will execute, you may have a case where you want *one of many* possible clauses to execute.

The elif statement is an **“else if”** statement that *always follows an if or another elif statement*.

It provides another condition that is checked *only if all of the previous conditions were False*. 

In code, an elif statement always consists of the following:

- The elif keyword
- A condition (that is, an expression that evaluates to True or False)
- A colon
- Starting on the next line, an indented block of code (called the elif clause)

  if name == 'Alice':
    print('Hi, Alice.')
  elif age < 12:
    print('You are not Alice, kiddo.')

The elif clause executes if age < 12 is True and name == 'Alice' is False.

However, **if both of the conditions are False**, then *both of the clauses are skipped*.

When there is a *chain of **elif** statements*, **only one or none of the clauses will be executed**.

Once one of the statements’ conditions is found to be True, the rest of the elif clauses are automatically skipped.

**The order of the elif statements *does matter*, however**.

Remember that the rest of the elif clauses are automatically skipped once a True condition has been found, so if you swap around some of the clauses in vampire.py, you run into a problem.

Remember that at most only one of the clauses will be executed, and for elif statements, the order matters!

Optionally, you can have an **else** statement *after the last **elif** statement*.

In that case, it is guaranteed that at least one (and only one) of the clauses will be executed. If the conditions in every if and elif statement are False, then the else clause is executed.

  name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

“If the first condition is true, do this. Else, if the second condition is true, do that. Otherwise, do something else.” 

When you use *if*, *elif*, and *else* statements together, remember these rules about how to order them to avoid bugs.

- First, there is **always exactly one *if* statement**.
- Any *elif* statements you need **should follow the *if* statement**.
- If you want to be sure that **at least one clause is executed, close the structure with an *else* statement**.

### *while* Loop Statements

You can make a block of code *execute over and over again* using a while statement. 

The code in a *while clause* will be executed as long as the while statement’s condition is True. 

In code, a while statement always consists of the following:

- The while keyword
- A condition (that is, an expression that evaluates to True or False)
- A colon
- Starting on the next line, an indented block of code (called the while clause)

*while* statement looks similar to an *if* statement.
The difference is in how they behave.

At the end of an *if clause*, the program execution **continues after the if statement**. 
But at the end of a *while clause*, the program execution **jumps back to the start of the while statement**.

The *while clause* is often called the **while loop** or just the **loop**.

Let’s look at an if statement and a while loop that use the same condition and take the same actions based on that condition. 

Here is the code with an if statement:

  spam = 0
  if spam < 5:
    print('Hello, world.')
    spam = spam + 1

Here is the code with a while statement:

  spam = 0
  while spam < 5:
    print('Hello, world.')
    spam = spam + 1 

These statements are *similar* — both if and while check the value of spam, and if it’s less than 5, they print a message.

But when you run these two code snippets, something very different happens for each one.

For the *if statement*, the output is simply "Hello, world."

But for the *while statement*, it’s "Hello, world." repeated five times!

The code with the *if statement* checks the condition, and it prints Hello, world. only once *if that condition is true*.

The code with the *while loop*, on the other hand, will print it five times. The loop stops after five prints because the *integer in spam increases by one at the end of each loop iteration*, which means that the *loop will execute five times before spam < 5 is False*.

In the while loop, the condition is always checked at the start of each iteration (that is, each time the loop is executed). If the condition is True, then the clause is executed, and afterward, the condition is checked again. The first time the condition is found to be False, the while clause is skipped.

### *break* Statements

There is a shortcut to getting the program execution *to break out of a while loop’s clause early*.

If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.

### *continue* Statements

Like *break statements*, *continue statements* are used inside loops.

When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. 
(This is also what happens when the execution reaches the end of the loop.) ???

If you ever run a program that has a bug causing it to get stuck in an infinite loop, press CTRL-C or select Shell ▸ Restart Shell from IDLE’s menu. This will send a KeyboardInterrupt error to your program and cause it to stop immediately.


“TRUTHY” AND “FALSEY” VALUES:

Conditions will consider some values in other data types equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True. 

## *for* Loops and the range() Function

The *while loop* keeps looping while its **condition is True** (which is the reason for its name), 
but what if you want to **execute a block of code only a certain number of times**? 
You can do this with a *for loop statement* and the *range() function*.

In code, a for statement looks something like for i in range(5): and includes the following:

- The for keyword
- A variable name
- The in keyword
- A call to the range() method with up to three integers passed to it
- A colon
- Starting on the next line, an indented block of code (called the for clause)

You can use break and continue statements inside for loops as well.

In fact, *you can use continue and break statements only inside **while** and **for loops***. 
If you try to use these statements elsewhere, Python will give you an error.

## An Equivalent while Loop

You can actually use a while loop to do the same thing as a for loop; 
*for loops are just more concise*.

## The Starting, Stopping, and Stepping Arguments to range()

Some functions can be called with **multiple arguments separated by a comma**, and *range()* is one of them.

  for i in range(12, 16):
    print(i)

The first argument will be where the for loop’s variable starts, and the second argument will be up to, *but not including*, the number to stop at.

12
13
14
15

The range() function can also be called with *three arguments*.

The first two arguments will be the *start* and *stop values*, and the third will be the *step argument*.

The step is the amount that the variable is increased by after each iteration.

  for i in range(0, 10, 2):
    print(i)

0
2
4
6
8

You can even use a *negative number for the step argument* to make the for loop count down instead of up.

  for i in range(5, -1, -1):
      print(i)

5
4
3
2
1
0

Running a for loop to print i with range(5, -1, -1) should print from five down to zero.

## Importing Modules

All Python programs can call a basic set of functions called built-in functions, including the print(), input(), and len() functions you’ve seen before.

Python also comes with a *set of modules* called the *standard library*.

Each module is a Python program that contains a related group of functions that can be embedded in your programs.

Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:

- The import keyword
- The name of the module
- Optionally, more module names, as long as they are separated by commas

Once you *import a module*, you can use all the *functions of that module*.

DON’T OVERWRITE MODULE NAMES:

When you save your Python scripts, take care not to give them a name that is used by one of Python’s modules, such as random.py, sys.py, os.py, or math.py. If you accidentally name one of your programs, say, random.py, and use an import random statement in another program, your program would import your random.py file instead of Python’s random module. This can lead to errors such as AttributeError: module 'random' has no attribute 'randint', since your random.py doesn’t have the functions that the real random module has. Don’t use the names of any built-in Python functions either, such as print() or input().

## from import Statements

An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for example, from random import *.

With this form of import statement, calls to functions in random will not need the random. prefix.

However, using the full name makes for more readable code, so it is better to use the import random form of the statement.

## Ending a Program Early with the sys.exit() Function

The last flow control concept to cover is *how to terminate the program*.

Programs always terminate if the program execution reaches the bottom of the instructions.

However, you can cause the program to terminate, or exit, before the last instruction by *calling the sys.exit() function*.

Since this function is in the sys module, you have to **import sys** before your program can use it.

## Summary

By using expressions that evaluate to True or False (also called conditions), you can write programs that make decisions on what code to execute and what code to skip.

You can also execute code over and over again in a loop while a certain condition evaluates to True. 

The break and continue statements are useful if you need to exit a loop or jump back to the loop’s start.













