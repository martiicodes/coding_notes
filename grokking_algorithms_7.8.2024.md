## Base case and recursive case

Because a recursive function calls itself, it’s easy to write a
function incorrectly that ends up in an infinite loop.

When you write a recursive function, you have to tell it when to stop
recursing.

That’s why **every recursive function has two parts**: 
**the base case** and **the recursive case**.

- The recursive case is when the function calls
itself. 
- The base case is when the function doesn’t call itself again… 
so it doesn’t go into an infinite loop.

## The stack

This section covers the *call stack*.

The stack ofsticky notes is much simpler.

When you insert an item, it gets added to the top of the list. 
When you read an item, you only read the topmost item, and it’s taken off the list. 

So your todo list has only two actions: **push (insert)** and **pop (remove and read)**.

This data structure is called a stack. The stack is a simple data structure.

## The call stack

Every time you make a function call, your computer saves the values
for all the variables for that call in memory like this.

Your computer is using a stack for these boxes. The second box is added
on top of the first one.

Now the topmost box on the stack is for the *greet* function, which
means you returned back to the greet function. 
When you called the *greet2* function, the greet function was *partially completed*.

This is the big idea behind this section: **when you call a function from another function, the calling function is paused in a partially completed state**.

All the values of the variables for that function are still stored in memory.
Now that you’re done with the *greet2* function, you’re back to the
*greet* function, and *you pick up where you left off*.

Recap:

- Recursion is when a function calls itself.
- Every recursive function has two cases: the base case
and the recursive case.
- A stack has two operations: push and pop.
- All function calls go onto the call stack.
- The call stack can get very large, which takes up a lot of memory.

