def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    array = [241, 124, 6, -124, 0, 241421, 5]
    print("Исходный список:", array)
    bubble_sort(array)
    print("Отсортированный список:", array)