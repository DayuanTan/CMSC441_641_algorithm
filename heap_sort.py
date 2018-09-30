import random
import math

# Dayuan Tan created on Sep. 30, 2018
# max heap sort

# generate 10 random numbers to be sorted
data = []
for i in range(1,10,1):
    data.append(random.randint(1,100))
print('Unsorted array is: ', data)

def swap(a, b):
    return b, a

def max_heapify(data, i, heap_size):
    left = 2 * i 
    right = 2 * i + 1
    largest = 0
    if left <= heap_size and data[left - 1] > data[i - 1]:
       largest = left
    else: 
        largest = i
    if right <= heap_size and data[right - 1] > data[largest - 1]:
        largest = right
    if largest != i:
        data[i - 1], data[largest - 1] = swap(data[i - 1], data[largest - 1])
        max_heapify(data, largest, heap_size)

def build_max_heap(data, heap_size):
    not_leaves = math.ceil(len(data) / 2)
    for i in range(not_leaves, 0, -1):
        max_heapify(data, i, heap_size)

# mian
heap_size = len(data)
build_max_heap(data, heap_size)
for i in range(len(data), 1, -1):    
    data[0], data[i - 1] = swap(data[0], data[i - 1])
    heap_size = heap_size - 1
    max_heapify(data, 1, heap_size)

print('Sorted array is: ', data)