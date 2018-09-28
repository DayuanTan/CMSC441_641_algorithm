import random

# generate 10 random numbers to be sorted
data = []
for i in range(1,10,1):
    data.append(random.randint(1,100))
print('Unsorted array is: ', data)

for j in range(1, len(data)):
    key = data[j]
    i = j - 1
    while data[i] > key and i >= 0:
        data[i + 1] = data[i]
        i = i - 1
    data[i + 1] = key

print('Sorted array is: ', data)
    

