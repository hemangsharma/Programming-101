# Bubble Sort example
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 2, 8, 1, 9]
print(bubble_sort(arr))  # [1, 2, 5, 8, 9]