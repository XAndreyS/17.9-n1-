

import time
start_time = time.time()
while True:
    try:
        numbers = list(map(int,input("Введите последовательность чисел через пробел:").split()))
    except ValueError as error:
        print("Не верный ввод!Вы должны вводить только  цифры,через пробел!")
    else:
        break

while True:
    try:
        number = int(input('Введите любое число:'))
    except ValueError as error:
        print("Не верный ввод!Вы должны вводить только цифры,и только одно число")
    else:
        break

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        midle = len(array) // 2
        left = merge_sort(array[:midle])
        right = merge_sort(array[midle:])
        return merge(left,right)

def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count

try:
    def binary_seearch(array, element, left, right):
        if left > right or count_number >1:
            element -=1
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_seearch(array, element, left, middle - 1)
        else:
            return binary_seearch(array, element, middle + 1, right)

except RuntimeError:
    print('Ловим ошибку')#

else:
    print('Используется линеный алгоритм поиска,это может занять больше времени')
    def find(array, element):
        for i, a in enumerate(array):
            if a == element:
                return i
        return False



count_number = count(numbers,number)
for_index_number = merge_sort(numbers)
min_index = for_index_number.index(min(for_index_number))
max_index = for_index_number.index(max(for_index_number))
print()
print(f'Введённая последовательность чисел:{" ".join(map(str,numbers))}')
print(f'Введённое число:{number}')
print(f'Количество повторени введённого числа {number}:{count(numbers,number)} раз(а)')
print(f'Осортированная последовательность введённых чисел:{" ".join(map(str,for_index_number))}')
if count_number == 1:
    print(f'Индекс предыдущего числа:{binary_seearch(for_index_number,number,min_index, max_index)-1}')
elif count_number > 1 and RecursionError:
    print(f'Индекс предыдущего числA:{find(for_index_number, number) - 1}')
else:
    print(f'Индекс предыДущего ЧислA:{binary_seearch(for_index_number, number, min_index, max_index)}')




print("--- %s seconds ---" % (time.time() - start_time))