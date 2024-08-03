#Question 3: You are given an array A containing the age of persons in your locality, 
#and your task is to find and return an array containing the age of persons that are over 18 (18 included)
def findAdults(arr):
    adultsArray = []
    for i in range(len(arr)):
        if arr[i]>=18:
            adultsArray.append(arr[i])
    print(adultsArray)
arr=[11,23,3,45,72,68]
findAdults(arr)