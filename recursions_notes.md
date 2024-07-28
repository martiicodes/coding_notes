# Recursions

Python also accepts function **recursion**, which means a *defined function can call itself*.

**Recursion** is a common mathematical and programming concept. 
It means that a *function calls itself*. 
You can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing 
a function which never terminates, or one that uses excess amounts of memory or processor power. 

A Recursive function can be defined as a routine that calls itself directly or indirectly.

In other words, a recursive function is a function that solves a problem by solving smaller 
instances of the same problem. This technique is commonly used in programming to solve problems 
that can be broken down into simpler, similar subproblems.

Recursion is an amazing technique with the help of which we can reduce the length of our code and 
make it easier to read and write. It has certain advantages over the iteration technique.

- Performing the same operations multiple times with different inputs.
- In every step, we try smaller inputs to make the problem smaller.
- Base condition is needed to stop the recursion otherwise infinite loop will occur.


## Algorithm: Steps

**The algorithmic steps for implementing recursion in a function** are as follows:

**Step 1** - *Define a base case*: Identify the simplest case for which the solution is known or trivial. 
This is the stopping condition for the recursion, as it prevents the function from infinitely calling itself.

**Step 2** - *Define a recursive case*: Define the problem in terms of smaller subproblems. 
Break the problem down into smaller versions of itself, and call the function recursively to solve each subproblem.

**Step 3** - *Ensure the recursion terminates*: Make sure that the recursive function eventually reaches the base case, 
and does not enter an infinite loop.

**Step 4** - *Combine the solutions*: Combine the solutions of the subproblems to solve the original problem.


## A Mathematical Interpretation

Let us consider a problem that a programmer has to determine the sum of first n natural numbers, 
there are several ways of doing that but the simplest approach is simply to add the numbers starting from 1 to n. 
So the function simply looks like this:

**approach(1) – Simply adding one by one**

f(n) = 1 + 2 + 3 +……..+ n

*but* there is another mathematical approach of representing this:

**approach(2) – Recursive adding**

f(n) = 1                  n=1

f(n) = n + f(n-1)         n>1

There is a simple difference between the *approach (1)* and *approach(2)* and that is 
in approach(2) the function “ f( ) ” itself is being called inside the function, so 
*this phenomenon is named recursion*, and the *function containing recursion* is called **recursive function**.


## How are recursive functions stored in memory?

Recursion uses more memory, because the recursive function adds to the stack with each recursive call,
and keeps the values there until the call is finished. The recursive function uses **LIFO (LAST IN FIRST OUT)**. 
Structure just like the *stack data structure*.


What is the base condition in recursion? 
In the recursive program, the solution to the base case is provided and the solution to the bigger problem 
is expressed in terms of smaller problems. 
 

  int fact(int n)
  {
    if (n < = 1) // base case
        return 1;
    else    
        return n*fact(n-1);    
  }

In the above example, the base case for n < = 1 is defined and the larger value of a number can be solved by 
converting to a smaller one till the base case is reached.


## Recursion VS Iteration

Recursion:	

1. Terminates when the base case becomes true.	
2.	Used with functions.	
3.	Every recursive call needs extra space in the stack memory.	
4.	Smaller code size.	

Iteration:

1. Terminates when the condition becomes false.
2. Used with loops.
3. Every iteration does not require any extra space.
4. Larger code size.


## Real Applications of Recursion in real problems

Recursion is a powerful technique that has many applications in computer science and programming. 
Here are some of the common applications of recursion:

- Tree and graph traversal: Recursion is frequently used for traversing and searching data structures such as trees and graphs. 
Recursive algorithms can be used to explore all the nodes or vertices of a tree or graph in a systematic way.

- Sorting algorithms: Recursive algorithms are also used in sorting algorithms such as quicksort and merge sort. 
These algorithms use recursion to divide the data into smaller subarrays or sublists, sort them, and then merge them back together.
  
- Divide-and-conquer algorithms: Many algorithms that use a divide-and-conquer approach, such as the binary search algorithm, 
use recursion to break down the problem into smaller subproblems.

- Fractal generation: Fractal shapes and patterns can be generated using recursive algorithms. For example, the Mandelbrot set 
is generated by repeatedly applying a recursive formula to complex numbers.

- Backtracking algorithms: Backtracking algorithms are used to solve problems that involve making a sequence of decisions, 
where each decision depends on the previous ones. These algorithms can be implemented using recursion to explore all possible paths 
and backtrack when a solution is not found.

(N-Queens and Sudoku)

- Memoization: Memoization is a technique that involves storing the results of expensive (?) function calls and returning the cached result 
when the same inputs occur again. Memoization can be implemented using recursive functions to compute and cache the results of subproblems.


(side note)

**Traversal Tasks**:

Definition: Operations that involve visiting all the nodes or elements in a data structure (e.g., trees, graphs, arrays).

Example: In-order traversal of a binary tree, depth-first search (DFS), breadth-first search (BFS).

**Pattern Recognition Tasks**:

Definition: Processes that identify regularities or patterns in data.

Example: Recognizing handwritten digits, detecting spam emails, identifying recurring sequences in time-series data.


