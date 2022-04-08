def quicksort(array):
    if len(array) < 2:
        # base case, arrays with 0 or 1 elements are already "sorted"
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array for all elements less than or equal to pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array for all elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))