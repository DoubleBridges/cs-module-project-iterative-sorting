# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(len(arr) - 1):

        # search the unsorted tail of the arr
        start_index = i
        for j in range(i, len(arr)):
            if arr[start_index] > arr[j]:
                start_index = j

        # swap the lowest value from the unsorted tail for the first index
        # in the usorted tail
        arr[i], arr[start_index] = arr[start_index], arr[i]

    return arr

    # TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    i1 = 0
    i2 = 1
    end = len(arr) - 1
    while i2 <= end and end > 0:
        if arr[i1] > arr[i2]:
            high = arr[i1]
            low = arr[i2]
            arr[i1] = low
            arr[i2] = high
        if i2 == end:
            i1 = 0
            i2 = 1
            end -= 1
        else:
            i1 += 1
            i2 += 1

    return arr


"""
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def count_sort(arr, maximum):
    # Your code here
    count_list = [0] * maximum

    for val in range(0, len(arr) - 1):
        count_list[val] = +1

    sorted = []

    for val in count_list:
        if val != 0:
            for i in range(val):
                sorted.append(val)

    arr = sorted

    return arr
