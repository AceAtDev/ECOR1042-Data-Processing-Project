def bubble(arr: list):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


unsortedArr = [11, 3, 2, 5, 97, 8, 9, 1, 3, 100, 110, 120, 130, 1]
print(bubble(unsortedArr))
