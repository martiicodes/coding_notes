# Conway's Game of Life

Conway’s Game of Life is an example of cellular automata: a set of rules governing the behavior of a field made up of discrete cells.

In practice, it creates a pretty *animation* to look at.

A filled-in square will be “alive” and an empty square will be “dead.”

If a living square has two or three living neighbors, it continues to live on the next step. 

If a dead square has exactly three living neighbors, it comes alive on the next step.

## Lists 

[Source](https://automatetheboringstuff.com/2e/chapter4/)

We can use a list of lists to represent the two-dimensional field.

The inner list represents each column of squares and stores a '#' hash string for living squares and a ' ' space string for dead squares.





