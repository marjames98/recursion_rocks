# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(arr, n):
    max = arr[0]
    for i in range (1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [1, 4, 45, 6, -50, 10, 2]
n = len(arr)
Value = find_max(arr, n)
print("max number is", Value)            

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45