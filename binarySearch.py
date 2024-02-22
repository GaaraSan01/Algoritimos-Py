import math
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def binary_search(array: list, x:int) -> int | bool:
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:

        mid_index = math.trunc((start_index + end_index)/2)

        if array[mid_index] == x:
            return mid_index
        
        elif array[mid_index] < x:
            start_index = mid_index + 1

        else:
            end_index = mid_index - 1
    
    return False


print(binary_search(lista_ordenada, 100))