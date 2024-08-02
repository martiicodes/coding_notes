x = int(input("Please enter an integer: "))

if x < 0:
    x = 0 # ne razumem? Znam da ne znači da je x jednako 0. Value of 0 assigned to x.

          # This is likely done to handle negative input values by converting them to 0. 
          # It ensures the program doesn't process or display negative numbers in subsequent operations.

          # After changing x to 0, it prints 'Negative changed to zero' to inform the user of this change.
          # In Python, a colon (:) is used to start a block of code that is indented, 
          # indicating that it belongs to a control structure like if, elif, else, for, while, etc. 
          # The line x = 0 is an assignment statement, not a control structure, so it does not need a colon.

          # Assignment statement, no colon needed.

    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# There can be zero or more elif parts, and the else part is optional.
# The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. 
# An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.