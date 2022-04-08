def binary_search(arr, target):
    print(arr)
    if not arr:
        return -1
    if len(arr) == 1 and arr[0] == target:
        return arr[0]
    if len(arr) == 1 and arr[0] != target:
        return -1
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)
    
print(binary_search([1,2,4,5,6,77], 6))