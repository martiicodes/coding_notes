# Example 1:

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# I understand first two recursions (k=1, k=2), but don't understand last 4?


# Example 2:
# A Python 3 program to 
# demonstrate working of 
# recursion 
  
def printFun(test): 
  
    if (test < 1): 
        return
    else: 
  
        print(test, end=" ") 
        printFun(test-1)  # statement 2 
        print(test, end=" ") 
        return
  
# Driver Code 
test = 3
printFun(test) 
  
# This code is contributed by 
# Smitha Dinesh Semwal


# Example 3:
# Python code to implement Fibonacci series
  
# Function for fibonacci 
def fib(n): 
  
    # Stop condition 
    if (n == 0): 
        return 0
  
    # Stop condition 
    if (n == 1 or n == 2): 
        return 1
  
    # Recursion function 
    else: 
        return (fib(n - 1) + fib(n - 2)) 
  
  
# Driver Code 
  
# Initialize variable n. 
n = 5; 
print("Fibonacci series of 5 numbers is :",end=" ") 
  
# for loop to print the fibonacci series. 
for i in range(0,n):  
    print(fib(i),end=" ") 


#Example 4:
# Python3 code to implement factorial 
  
# Factorial function 
def f(n): 
  
    # Stop condition 
    if (n == 0 or n == 1): 
        return 1; 
  
    # Recursive condition 
    else: 
        return n * f(n - 1); 
  

# Example 5: 
# Driver code 
if __name__=='__main__': 
  
    n = 5; 
    print("factorial of",n,"is:",f(n)) 
      
    # This code is contributed by pratham76.


    def factorial(n): 
    # Base case: if n is 0 or 1, return 1 
    if n == 0 or n == 1: 
        return 1
  
    # Recursive case: if n is greater than 1, call the function with n-1 and multiply by n 
    else: 
        return n * factorial(n-1) 
  
# Call the factorial function and print the result 
result = factorial(5) 
print(result)  # Output: 120 


# One of the simplest and most illustrative examples of recursion is the calculation of the factorial of a number. 
# Here’s a Python function that demonstrates this:

def factorial(n):
    # Base case: if n is 0, return 1
    
    # This is the condition that stops the recursion. 
    # If n is 0, the function returns 1 because the factorial of 0 is defined as 1.
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)

    # Here, the function calls itself with the argument n - 1. This process repeats, 
    # reducing the value of n each time, until it reaches the base case.
    else:
        return n * factorial(n - 1)

# Test the function

# When you call factorial(5), it will recursively call itself until it reaches factorial(0), 
# then multiply the results as it unwinds the recursion stack.
print(factorial(5))  # Output: 120




