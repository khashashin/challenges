# Task
# Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 6, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not n is weird.
#
# Input Format
#
# A single line containing a positive integer, n.
#
# Output Format
#
# Print Weird if the number is weird; otherwise, print Not Weird.

#!/bin/python3

import sys


N = int(input().strip())
if N % 2 != 0:
    print("Weird")
elif 2<=N<=5:
    print("Not Weird")
elif 6<=N<=20:
    print("Weird")
elif N>20:
    print("Not Weird")

##############################################################################
######################    Additional examples   ##############################
##############################################################################

if N % 2 != 0 or 6<=N<=20:
    print("Weird")
elif 2<=N<=5 or N>20:
    print("Not Weird")
