# Question 2: Write a program that you are given a integer N, and your task is to print all the integers starting from 1 till N (N. inclusive).
# Recursion is used to solve this problem though we can do it using loops.
n=int(input("Enter the number till which you want to print all the numbers starting from 1."))
def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n, end=' ')
printNos(n)
    

