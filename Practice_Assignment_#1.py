# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:33:44 2023

@author: camtr

Exponent - **
Modulus - %
Integer division / floored quotient - //
Division - /
Multipllication - *
Addition - +
Subtraction - -

Create a program that can use all of these operators
"""

op = ""
num1= 0
num2 = 0
result = 0

validOpList = ["=", "-", "*", "/", "**", "//", "%"]

while(op != "e"):
    
    print("Please type a valid operation from: +, -, *, /, %, **, //; or type e to exit.")
    op = input()
    
    if(op not in validOpList):
        print("Enter a VALID operator; +, -, *, /, %, //, **")
        op = input()
    
    if(op == "e"):
        print("Goodbye!")
        break
    
    print("Please input the first number")
    num1 = input()
    print("Please input the second number")
    num2 = input()
    
    if op == "+":
        result = int(num1) + int(num2)
        print("{0} + {1} = {2}".format(num1, num2, result))
        
    elif (op == "-"):
        result = int(num1) - int(num2)
        print("{0} - {1} = {2}".format(num1, num2, result))
    
    elif(op == "*"):
        result = int(num1) * int(num2)
        print("{0} * {1} = {2}".format(num1, num2, result))

    elif(op == "/"):
        result = int(num1) / int(num2)
        print("{0} / {1} = {2}".format(num1, num2, result))

    elif(op == "//"):
        result = int(num1) // int(num2)
        print("{0} // {1} = {2}".format(num1, num2, result))

    elif(op == "%"):
        result = int(num1) % int(num2)
        print("{0} % {1} = {2}".format(num1, num2, result))

    elif(op == "**"):
       result = int(num1) ** int(num2)
       print("{0} ** {1} = {2}".format(num1, num2, result))
    
    else:
        print("Invalid input.")