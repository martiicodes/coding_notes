# Data Structures and Algorithms

[Source](https://www.w3schools.com/dsa/dsa_intro.php#:~:text=Data%20Structures%20is%20about%20how,data%20to%20solve%20problems%20efficiently.)

**Data Structures** is about how data can be stored in different structures.

**Algorithms** is about how to solve different problems, often by searching through and manipulating data structures.

### What are Data Structures?

A data structure is a way to store data.

Data structures give us the possibility to manage large amounts of data efficiently for uses such as large databases and internet indexing services.

Data structures are essential ingredients in creating fast and powerful algorithms. They help in managing and organizing data, reduce complexity, and increase efficiency.

In Computer Science there are two different kinds of data structures.

**Primitive Data Structures** are basic data structures provided by programming languages to represent single values, such as *integers, floating-point numbers, characters* and *booleans*.

**Abstract Data Structures** are higher-level data structures that *are built using primitive data types* and provide more complex and specialized operations. Some common examples of abstract data structures include *arrays, linked lists, stacks, queues, trees* and *graphs*.

### What are Algorithms?

An algorithm is a set of step-by-step instructions to solve a given problem or achieve a specific goal.

A cooking recipe written on a piece of paper is an example of an algorithm, where the goal is to make a certain dinner. The steps needed to make a specific dinner are described exactly.

When we talk about algorithms in Computer Science, the step-by-step instructions are written in a **programming language** and instead of food ingredients, an algorithm uses **data structures**.

Algorithms are fundamental to computer programming as they provide step-by-step instructions for executing tasks. 

### Data Structures together with Algorithms

Data structures and algorithms (DSA) go hand in hand. 

DSA is about finding efficient ways to store and retrieve data, to perform operations on data, and to solve specific problems.

By understanding DSA, you can:

Decide which data structure or algorithm is best for a given situation.
Make programs that run faster or use less memory.
Understand how to approach complex problems and solve them in a systematic way.

### Theory and Terminology

**Algorithm**: A set of step-by-step instructions to solve a specific problem.

**Data Structure**: A way of organizing data so it can be used efficiently. Common data structures include arrays, linked lists, and binary trees.

**Time Complexity**: A measure of the amount of time an algorithm takes to run, depending on the amount of data the algorithm is working on.

**Space Complexity**: A measure of the amount of memory an algorithm uses, depending on the amount of data the algorithm is working on.

**Big O Notation**: A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. Used in this tutorial to describe the time complexity of an algorithm.

**Recursion**: A programming technique where a function calls itself.

**Divide and Conquer**:	A method of solving complex problems by breaking them into smaller, more manageable sub-problems, solving the sub-problems, and combining the solutions. Recursion is often used when using this method in an algorithm.

**Brute Force**: A simple and straight forward way an algorithm can work by simply trying all possible solutions and then choosing the best one.

## DSA Arrays

An array is a data structure used to store multiple elements.

Arrays are indexed, meaning that each element in the array has an index, a number that says where in the array the element is located.

In Python, this code use index 0 to write the first array element to the console:

    my_array = [7, 12, 9, 4, 11]
        print( my_array[0] )

Before implementing the algorithm using an actual programming language, it is usually smart to first write the algorithm as a step-by-step procedure.

If you can write down the algorithm in something between human language and programming language, the algorithm will be easier to implement later because we avoid drowning in all the details of the programming language syntax.

The two step-by-step descriptions of the algorithm we have written above can be called **'pseudocode'**. Pseudocode is a description of what a program does, using language that is something between human language and a programming language.

    my_array = [7, 12, 9, 4, 11]
    minVal = my_array[0]    # Step 1

    for i in my_array:      # Step 2
        if i < minVal:      # Step 3
            minVal = i
        
    print('Lowest value: ',minVal) # Step 4

## DSA Bubble Sort

Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

How it works:

1. Go through the array, one value at a time.
2. For each value, compare the value with the next value.
3. If the value is higher than the next one, swap the values so that the highest value comes last.
4. Go through the array as many times as there are values in the array.

### Manual Run Through

Before we implement the Bubble Sort algorithm in a programming language, let's manually run through a short array only one time, just to get the idea.

Step 1: We start with an unsorted array.
[7, 12, 9, 11, 3]

Step 2: We look at the two first values. Does the lowest value come first? Yes, so we don't need to swap them.
[7, 12, 9, 11, 3]

Step 3: Take one step forward and look at values 12 and 9. Does the lowest value come first? No.
[7, 12, 9, 11, 3]

Step 4: So we need to swap them so that 9 comes first.
[7, 9, 12, 11, 3]

Step 5: Taking one step forward, looking at 12 and 11.
[7, 9, 12, 11, 3]

Step 6: We must swap so that 11 comes before 12.
[7, 9, 11, 12, 3]

Step 7: Looking at 12 and 3, do we need to swap them? Yes.
[7, 9, 11, 12, 3]

Step 8: Swapping 12 and 3 so that 3 comes first.
[7, 9, 11, 3, 12]

### Bubble Sort Implementation

To implement the Bubble Sort algorithm in a programming language, we need:

1. An array with values to sort.
2. An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
3. An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

The resulting code looks like this:

    my_array = [64, 34, 25, 12, 22, 11, 90, 5]

    n = len(my_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    
    print("Sorted array:", my_array)

### Bubble Sort Improvement

The Bubble Sort algorithm can be improved a little bit more.

Imagine that the array is almost sorted already, with the lowest numbers at the start, like this for example:

my_array = [7, 3, 9, 12, 11]

In this case, the array will be sorted after the first run, but the Bubble Sort algorithm will continue to run, without swapping elements, and that is not necessary.

If the algorithm goes through the array one time without swapping any values, the array must be finished sorted, and we can stop the algorithm, like this:

    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break

    print("Sorted array:", my_array)

## DSA Selection Sort

The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

How it works:

1. Go through the array to find the lowest value.
2. Move the lowest value to the front of the unsorted part of the array.
3. Go through the array again as many times as there are values in the array.

### Manual Run Through

Before we implement the Selection Sort algorithm in a programming language, let's manually run through a short array only one time, just to get the idea.

Step 1: We start with an unsorted array.
[ 7, 12, 9, 11, 3]

Step 2: Go through the array, one value at a time. Which value is the lowest? 3, right?
[ 7, 12, 9, 11, 3]

Step 3: Move the lowest value 3 to the front of the array.
[ 3, 7, 12, 9, 11]

Step 4: Look through the rest of the values, starting with 7. 7 is the lowest value, and already at the front of the array, so we don't need to move it.
[ 3, 7, 12, 9, 11]

Step 5: Look through the rest of the array: 12, 9 and 11. 9 is the lowest value.
[ 3, 7, 12, 9, 11]

Step 6: Move 9 to the front.
[ 3, 7, 9, 12, 11]

Step 7: Looking at 12 and 11, 11 is the lowest.
[ 3, 7, 9, 12, 11]

Step 8: Move it to the front.
[ 3, 7, 9, 11, 12]

Finally, the array is sorted.

## DSA Insertion Sort

The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.

The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

How it works:

1. Take the first value from the unsorted part of the array.
2. Move the value into the correct place in the sorted part of the array.
3. Go through the unsorted part of the array again as many times as there are values.

### Manual Run Through

Before we implement the Insertion Sort algorithm in a programming language, let's manually run through a short array, just to get the idea.

Step 1: We start with an unsorted array.
[ 7, 12, 9, 11, 3]

Step 2: We can consider the first value as the initial sorted part of the array. If it is just one value, it must be sorted, right?
[ 7, 12, 9, 11, 3]

Step 3: The next value 12 should now be moved into the correct position in the sorted part of the array. But 12 is higher than 7, so it is already in the correct position.
[ 7, 12, 9, 11, 3]

Step 4: Consider the next value 9.
[ 7, 12, 9, 11, 3]

Step 5: The value 9 must now be moved into the correct position inside the sorted part of the array, so we move 9 in between 7 and 12.
[ 7, 9, 12, 11, 3]

Step 6: The next value is 11.
[ 7, 9, 12, 11, 3]

Step 7: We move it in between 9 and 12 in the sorted part of the array.
[ 7, 9, 11, 12, 3]

Step 8: The last value to insert into the correct position is 3.
[ 7, 9, 11, 12, 3]

Step 9: We insert 3 in front of all other values because it is the lowest value.
[ 3,7, 9, 11, 12]

Finally, the array is sorted.

## DSA Quicksort

As the name suggests, Quicksort is one of the fastest sorting algorithms.

The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

In this tutorial the last element of the array is chosen to be the pivot element, but we could also have chosen the first element of the array, or any element in the array really.

Then, the Quicksort algorithm does the same operation recursively on the sub-arrays to the left and right side of the pivot element. This continues until the array is sorted.

**Recursion** is when a function calls itself.

After the Quicksort algorithm has put the pivot element in between a sub-array with lower values on the left side, and a sub-array with higher values on the right side, the algorithm calls itself twice, so that Quicksort runs again for the sub-array on the left side, and for the sub-array on the right side. The Quicksort algorithm continues to call itself until the sub-arrays are too small to be sorted.

The algorithm can be described like this:

How it works:

1. Choose a value in the array to be the pivot element.
2. Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
4. Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.


