import os
import sys
import math

def PrintStub(n):
    if (n >= 1) and (n <= 20):
        i = 0
        while i < n:
            sqval=0
            sqval=pow(i,2)
            i+=1
            print(sqval)

while True:
    Value = input("Enter the value: ")

    Value = int(Value)

    if (Value >= 0):
        break
    else:
        print("\nPlease enter the positive value.\n")

PrintStub(Value)