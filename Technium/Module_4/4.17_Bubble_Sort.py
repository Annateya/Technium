def bubble_sort(arr):
    a = len(arr)
    while a > 0:
        for i in range(a-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        a = a - 1
    return arr

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Неотсортированный список:", my_list)
print("Отсортированный список:  ", bubble_sort(my_list))
