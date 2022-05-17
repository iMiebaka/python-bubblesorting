from datetime import datetime
from time import time
import random

def bubblesort(elements):
# Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

elements = []
start = time()
print(f"Started - {datetime.now()}")
for _ in range(5):
    elements.append(random.randint(1, 1000))


print("Unsorted list is,")
print( elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)

stop = time()
print(f"Total time taken is {stop - start}")
print(f"Stopped - {datetime.now()}")
