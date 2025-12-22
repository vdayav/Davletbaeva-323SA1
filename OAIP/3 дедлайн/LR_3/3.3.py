def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1
    
    mid = (low + high) // 2
    guess = arr[mid]

    if guess == target:
        return mid
    
    elif target < guess:
        return binary_search(arr, target, low, mid - 1)
    
    else:
        return binary_search(arr, target, mid + 1, high)

my_list = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(my_list, 40)) 
print(binary_search(my_list, 99)) 