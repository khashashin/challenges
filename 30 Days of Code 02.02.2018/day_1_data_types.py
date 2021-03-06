# Task
# Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:
#
# Declare  variables: one of type int, one of type double, and one of type String.
# Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# Use the  operator to perform the following operations:
# Print the sum of  plus your int variable on a new line.
# Print the sum of  plus your double variable to a scale of one decimal place on a new line.
# Concatenate  with the string you read as input and print the result on a new line.

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
a = 6
b = 2.0
c = 'My string'
# Read and save an integer, double, and String to your variables.
a = int(input())
b = float(input())
c = str(input())
# Print the sum of both integer variables on a new line.
print(a + i)
# Print the sum of the double variables on a new line.
print(b + d)
# Concatenate and print the String variables on a new line
print(s + c)
# The 's' variable above should be printed first.

##############################################################################
######################    Additional examples   ##############################
##############################################################################
x,y = (int(input()) for i in range(2))
print(x*60 + y)

e = int(input())
print(e//60, e%60, sep='\n')

f,h,m = (int(input()) for k in range(3))
y = f%60 + m
print(f//60 + h + y//60, y%60, sep='\n')
