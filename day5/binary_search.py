def binary_search(arr, target, left, right):
    # base case: element not found
    if left > right:
        return -1

    mid = (left + right) // 2

    # base case
    if arr[mid] == target:
        return mid
    # recursive cases
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5      
result = binary_search(arr, target, 0, len(arr) - 1)
print(f"Element {target} found at index {result}")  