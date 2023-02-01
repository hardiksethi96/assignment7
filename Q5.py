def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def count_occurrences(arr, x):
    index = binary_search(arr, x)
    if index == -1:
        return 0
    count = 1
    left = index - 1
    right = index + 1
    while left >= 0 and arr[left] == x:
        count += 1
        left -= 1
    while right < len(arr) and arr[right] == x:
        count += 1
        right += 1
    return count
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    arr.append(element)
arr.sort()
x = int(input("Enter the element to search for: "))
index = binary_search(arr, x)
if index == -1:
    print("Element not found in the array")
else:
    count = count_occurrences(arr, x)
    print("Element found at index {} and occurs {} times".format(index, count))
