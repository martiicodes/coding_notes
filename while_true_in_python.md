# While True in Python

While loop is used to execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.

Example:

  while True: 
    pass

If we run the above code then this loop will run infinite number of times. 
To come out of this loop we will use the break statement explicitly.

Example: While Loop with True to find the sum of first N numbers

  N = 10
  Sum = 0
  
This loop will run forever 

  while True: 
  Sum += N 
  N -= 1

the below condition will tell the loop to stop 

  if N == 0: 
    break
          
  print(f"Sum of First 10 Numbers is {Sum}")

## On Stack Overflow

While True is true -- ie always. This is an infinite loop

Note the important distinction here between True which is a keyword in the language denoting a constant value of a particular type, and 'true' which is a mathematical concept.

I think it's more appropriate to say 'indefinite loop;' the assumption must be that the loop will be interrupted by a break or return at some point. Truly 'infinite' loops are programmer error; 'indefinite loops' are created by design.

The more important part of your question is "What is while True?" is 'what is True', and an important corollary: What is false?

First, for every language you are learning, learn what the language considers 'truthy' and 'falsey'. Python considers Truth slightly differently than Perl Truth for example. Other languages have slightly different concepts of true / false. Know what your language considers to be True and False for different operations and flow control to avoid many headaches later!

There are many algorithms where you want to process something until you find what you are looking for. Hence the infinite loop or indefinite loop. Each language tend to have its own idiom for these constructs. Here are common C infinite loops, which also work for Perl:

  for(;;) { /* loop until break */ }
  /* or */
  while (1) {
   return if (function(arg) > 3);
  }

## Chat GPT

In Python, while True creates an infinite loop, meaning the loop will continue to run indefinitely *unless it's explicitly stopped using a break statement or an external interruption*. 

This construct is often used for continuously running processes, waiting for events, or repeatedly performing a task until a certain condition is met.

Here is a simple example:

  while True:
    user_input = input("Type 'exit' to end the loop: ")
    if user_input == 'exit':
        break
    print(f"You typed: {user_input}")

In this example, the loop will keep running until the user types 'exit', at which point the break statement will terminate the loop.
