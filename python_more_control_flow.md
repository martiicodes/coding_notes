# More Control Flow Tools

[Source](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

As well as the *while* statement just introduced, Python uses a few more...

## *if* Statements

Perhaps the most well-known statement type is the *if statement*.
For example:

    x = int(input("Please enter an integer: "))
    
    if x < 0:
        x = 0
    print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

There can be zero or more elif parts, and the else part is optional.

The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.

An **if … elif … elif** … sequence is a *substitute* for the **switch** or **case statements** found in other languages.

## *for* Statements

The *for statement* in Python *differs a bit* from what you may be used to in C or Pascal.

Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

# Measure some strings:

    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

cat 3
window 6
defenestrate 12

Code that modifies a collection while iterating over that same collection can be tricky to get right. 

*Instead*, it is usually more straight-forward to **loop over a copy of the collection** or **to create a new collection**:

Create a sample collection

    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

Strategy:  Iterate over a copy

    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

Strategy:  Create a new collection

    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
            
## The range() Function

If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

    for i in range(5):
        print(i)

0
1
2
3
4

**The given end point is never part of the generated sequence**; 

range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):

    list(range(5, 10))
[5, 6, 7, 8, 9]

    list(range(0, 10, 3))
[0, 3, 6, 9]

    list(range(-10, -100, -30))
[-10, -40, -70]

To iterate over the indices of a sequence, you can combine range() and len() as follows:

    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb

In most such cases, however, it is convenient to use the *enumerate() function*.

A strange thing happens if you just print a range:

    range(10)
range(0, 10)

In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.

It is an *object* which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

We say such an *object is iterable*, that is, suitable as a target for **functions** and **constructs** that expect something from which they can obtain successive items until the supply is exhausted.

We have seen that the *for statement* is such a **construct**, while an example of a **function** that takes an iterable is *sum()*:

    sum(range(4))  # 0 + 1 + 2 + 3
6

## *break* and *continue* Statements, and *else* Clauses on Loops

The *break statement* breaks out of the innermost enclosing *for* or *while loop*.

A *for* or *while loop* can include an *else clause*.

In a *for loop*, the *else clause* is executed after the loop reaches its **final iteration**.

In a *while loop*, it’s executed **after the loop’s condition becomes false**.

In either kind of loop, the *else clause* is **not executed** if the **loop was terminated by a break**.

This is exemplified in the following *for loop*, which searches for prime numbers:

    for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:

loop fell through without finding a factor
print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

(Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)

When used with a loop, the else clause has more in common with the else clause of a *try statement* than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs.

The continue statement, also borrowed from C, continues with the next iteration of the loop:

    for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9

## *pass* Statements

*The pass statement does nothing*. It can be used when a statement is required syntactically but the program requires no action. 

## *match* Statements

A *match statement* takes an expression and compares its value to successive patterns given as one or more case blocks.

This is superficially similar to a *switch statement* in C, Java or JavaScript (and many other languages), but it’s more similar to *pattern matching* in languages like Rust or Haskell.

## Defining Functions

The keyword **def** introduces a function definition. 

It must be followed by the *function name* and the *parenthesized list of formal parameters*. 

The statements that form the *body of the function* start at the *next line*, and *must be indented*.

The first statement of the function body can optionally be a *string literal*; this string literal is the *function’s documentation string*, or *docstring*. 

The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; 
thus, arguments are passed using call by value.















