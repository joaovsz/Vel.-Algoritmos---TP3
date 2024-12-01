def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:  
        return quickselect(right, k - len(left) - len(middle))


lista = [10, 4, 5, 8, 6, 11, 26]
k = 3  
kth_smallest = quickselect(lista, k)
print(f"O {k}° menor elemento é: {kth_smallest}")
