def remove_duplicates(arr):
    return list(set(arr))
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
n = int(input("Enter the number of elements in the list: "))
arr = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    arr.append(element)
arr = remove_duplicates(arr)
print("Sorted list using selection sort: ", selection_sort(arr))
print("Sorted list using bubble sort: ", bubble_sort(arr))
