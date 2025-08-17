def selection_sort_max(arr): # по убыванию
    a = len(arr)
    for x in range(a):
        max_number = arr[x]
        max_index = x
        for y in range(x+1,a):
            #print('числа',arr[x], arr[y])
            if arr[x] < arr[y] and max_number < arr[y]:
                max_number = arr[y]
                max_index = y
        print('min number', max_number)
        arr[x], arr[max_index] = max_number, arr[x]
        print(arr)
    return arr


def selection_sort_min(arr): # по возрастанию
    a = len(arr)
    for x in range(a):
        min_number = arr[x]
        min_index = x
        for y in range(x + 1, a):
            #print('числа', arr[x], arr[y])
            if arr[x] > arr[y] and min_number > arr[y]:
                min_number = arr[y]
                min_index = y
        print('min number', min_number)
        arr[x], arr[min_index] = min_number, arr[x]
        print(arr)
    return arr


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]

print("Отсортированный список по убыванию:", selection_sort_max(my_list))
print("Отсортированный список по возрастанию:", selection_sort_min(my_list))