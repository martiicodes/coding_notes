# Quicksort

Source: Grokking Algorithms - Aditya Y. Bhargava

Quicksort is a sorting algorithm. It’s much faster than selection sort
and is frequently used in real life.

Quicksort also uses D&C.

Empty arrays and arrays with just one element will be the base case. You
can just return those arrays as is—there’s nothing to sort:

    def quicksort(array):
        if len(array) < 2:
            return array

Let’s look at bigger arrays. An array with two elements is pretty easy to
sort, too.

What about an array of three elements?

Remember, you’re using D&C. So you want to break down this array
until you’re at the base case. 

Here’s how quicksort works. First, pick an
element from the array. This element is called the *pivot*.

Now find the elements smaller than the pivot and the elements larger
than the pivot.

This is called *partitioning*.

Now you have:

- A sub-array of all the numbers less than the pivot
- The pivot
- A sub-array of all the numbers greater than the pivot

The two sub-arrays aren’t sorted. They’re just partitioned. But if they
were sorted, then sorting the whole array would be pretty easy.

Both sub-arrays have only one element, and you know how to sort
those. So now you know how to sort an array of three elements. 

Here are the steps:

1. Pick a pivot.
2. Partition the array into two sub-arrays: elements less than the pivot
and elements greater than the pivot.
3. Call quicksort recursively on the two sub-arrays.

## Inductive proofs

Inductive proofs are one way to prove that your algorithm works.

Each inductive proof has two steps: 
- the base case 
and 
- the inductive case. 

Sound familiar?

________________

Here’s the code for quicksort:

    def quicksort(array):
        if len(array) < 2:
            return array 
        else:
            pivot = array[0] 
            less = [i for i in array[1:] if i <= pivot] 
            greater = [i for i in array[1:] if i > pivot] 
            return quicksort(less) + [pivot] + quicksort(greater)
        print quicksort([10, 5, 2, 3])

## Merge sort vs. quicksort

But sometimes the constant can make a difference. Quicksort versus
merge sort is one example. Quicksort has a smaller constant than
merge sort.



## Average case vs. worst case

The performance of quicksort heavily depends on the pivot you choose.

Suppose you always choose the first element as the pivot. And you
call quicksort with an array that is already sorted. 
Quicksort doesn’t check to see whether the input array is already sorted. 
So it will still try to sort it.

## Recap

- D&C works by breaking a problem down into smaller and smaller
pieces. If you’re using D&C on a list, the base case is probably an
empty array or an array with one element.

- If you’re implementing quicksort, choose a random element as the
pivot. The average runtime of quicksort is O(n log n)!

- The constant in Big O notation can matter sometimes. That’s why
quicksort is faster than merge sort.

- The constant almost never matters for simple search versus binary
search, because O(log n) is so much faster than O(n) when your list
gets big.

