from modulus import * #importing the modulus function defined in modulus.py
from sq_root import * #importing the sq_root function from sq_root.py file

n1 = input("Enter first number: ") #get the first number from user and store it in n1 variable
n2 = input("\nEnter second number: ") #get the second number from user and store it in n2 variable

print ("\nPress number according to desired function \n1-Add\n 2-Subtract\n 3-Multiply\n 4-Divide\n 5-Modulus\n 6-Square Root\n") #print the available calculator operations

fun = input("Enter operation: ") #get the user input for operation to be performed

if fun == 1:
    add(n1, n2)

elif fun == 2:
    subtract(n1, n2)

elif fun == 3:
    multiply(n1, n2)

elif fun == 4:
    divide(n1, n2)

elif fun == 5:
    modulus(n1, n2) #calling the modulus function

elif fun == 6:
    sq_root(n1, n2) #calling the square root function

