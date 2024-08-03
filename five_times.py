print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# The code in the for loop’s clause is run five times. 
# The first time it is run, the variable i is set to 0. 
# The print() call in the clause will print Jimmy Five Times (0). 
# After Python finishes an iteration through all the code inside the for loop’s clause, 
# the execution goes back to the top of the loop, and the for statement increments i by one. 
# This is why range(5) results in five iterations through the clause, with i being set to 0, then 1, then 2, then 3, and then 4. 
# The variable i will go up to, but will not include, the integer passed to range().