# Dayuan Tan created on Oct. 1, 2018
# merge sort without merge

import random
import math

# generate 10 random numbers to be sorted
data = []
for i in range(1,11,1):
    data.append(random.randint(1,100))
print('Unsorted array is: ', data)

def swap(a, b):
    return b, a

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r, 1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = swap(A[i], A[j])  
    A[i + 1], A[r] = swap(A[i + 1], A[r])    
    return i + 1  

def quick_sort(A, p, r):
    if p < r:
        q =  partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

# mian
quick_sort(data, 0, len(data)-1)
print('Sorted array is: ', data)