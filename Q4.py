def merge_sort(marks):
    if len(marks) <= 1:
        return marks
    mid = len(marks) // 2
    left = marks[:mid]
    right = marks[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result
n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    mark = int(input("Enter the mark for student {}: ".format(i+1)))
    marks.append(mark)
sorted_marks = merge_sort(marks)
print("The sorted marks are: ", sorted_marks)
def quick_sort(marks, start, end):
    if start >= end:
        return
    pivot = marks[end]
    partition_index = start
    for i in range(start, end):
        if marks[i] < pivot:
            marks[i], marks[partition_index] = marks[partition_index], marks[i]
            partition_index += 1
    marks[end], marks[partition_index] = marks[partition_index], marks[end]
    quick_sort(marks, start, partition_index - 1)
    quick_sort(marks, partition_index + 1, end)
n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    mark = int(input("Enter the mark for student {}: ".format(i+1)))
    marks.append(mark)
quick_sort(marks, 0, len(marks) - 1)
print("The sorted marks are: ", marks)
