# Question 1: Write a program that takes a number from the user and print the count of digits in that number
#The idea is to count the digits by removing the digits from the input number starting from right(least significant digit) to left(most significant digit) till the number is reduced to 0. We are removing digits from the right because the rightmost digit can be removed simply by performing integer division by 10. For eg: N = 1567, then 1567 / 10 = 156.7 = 156(Integer Division).
# There are 2 approaches to solve this problem. 
# 1. Iterative Solution to count digits in an integer – O(Number of Digits) Time and O(1) Space
# 2. Removing digits using Recursion – O(Number of Digits) Time and O(Number of Digits) Space
# I have used Recursive Python program to count the number of digits in a number

def countDigit(n):
    if n//10 == 0:
        return 1
    return 1 + countDigit(n // 10)

n = int(input("Enter the number to find out the number of digits in it"))
print("Number of digits:", countDigit(n))