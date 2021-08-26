"""
Created by: voidblob
Purpose: Basic Calculator
Date: 12:49 PM EST, 2021-08-26
"""

def calculator():
    print("|BASIC CALCULATOR|")
    print("------------------")
    print()
    repeat = "y"
    start = input("Would you like to start (y/n): ")
    while start == "y" and repeat == "y":
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        ans = 0

        operation = input("\nEnter the operation you would like to perform (x, /, +, -): ")

        if operation == "x":
            ans = num1 * num2
        elif operation == "/":
            ans = num1 / num2
        elif operation == "+":
            ans = num1 + num2
        elif operation == "-":
            ans = num1 - num2

        else:
            print("Please enter a proper operation")
            operation = input("Enter the operation you would like to perform (x, /, +, -): ")
            
        print("Your answer is:",ans)

        repeat = input("\nWould you like to continue (y/n): ")

    if repeat == "n":
        print("\nThank you for using |The Basic Calculator|")
        
calculator()

