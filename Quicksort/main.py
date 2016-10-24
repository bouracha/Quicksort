import time

#from pivot_first import QuickSort
#from pivot_last import QuickSort
from pivot_median import QuickSort


### Main ###

A = []

result_file = r'week2_input.txt'
with open(result_file) as file:
    data_array = [[float(digit) for digit in line.split()] for line in file]

for i in range(0, len(data_array)):
    A.append(data_array[i][0])


print "Input array: ", A

start_time = time.time()

num_comparisons = 0
A, num_comparisons = QuickSort(A, 0, (len(A)-1))

end_time = time.time()
print "Runtime: ", (end_time - start_time), " seconds."
print "Number of comparisons: ", num_comparisons
print "Sorted array: ", A
