import random
import math

# Dayuan Tan created on Sep. 29, 2018
# divide and conquer

# generate 10 random numbers to be sorted
data = []
for i in range(1,10,1):
    data.append(random.randint(1,100))
print('Unsorted array is: ', data)


# merge two sorted arrays [p, q] [q + 1, r]
def merge(A, p, q, r):
    # prepare list with customized length
    nleft = q - p + 1
    nright = r - q 
    left = [-1] * nleft
    right = [-1] * nright

    for i in range(p, q + 1): # + 1 for range include left side exclude right side
        left[i - p] = A[i]
    for i in range(q + 1, r + 1):
        right[i - (q + 1)] = A[i]

    # merge
    i = j = 0
    k = p
    while i < nleft and j < nright:
        if left[i] <= right[j]:
            A[k] = left[i]
            i = i + 1
        else:
            A[k] = right[j]
            j = j + 1
        k = k + 1
    # only one of these two array may have some left items 
    while i < nleft:
        A[k] = left[i]
        i = i + 1
        k = k + 1
    while j < nright:
        A[k] = right[j]
        j = j + 1
        k = k + 1

# divide 
def merge_sort(A, p, r):
    if p < r:
        mid = math.ceil((r + p)/2) - 1
        merge_sort(A, p, mid)
        merge_sort(A, mid + 1, r)
        merge(A, p, mid, r)

# mian
merge_sort(data, 0, len(data) - 1)
print('Sorted array is: ', data)
