def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def Task1():
    arr = [1, 2, 3, 4, 5]

    num = int(input("input number: "))

    i = int(input("input index for array: "))
    arr[i] = num

    arr.pop()

    print(arr)
    print(f"Len array = {len(arr)}")

def Task2():
    arr = [5, 3, 10, 23, 1, 4, 3]
    print(arr)
    bubble_sort(arr)
    print(arr)

def Task3():
    arr = [1, 3, 6, 8, 3, 1, 3, 2, 2, 7, 8, 1, 3, 4, 6, 8]
    unique_arr = []
    for elem in arr:
        if elem not in unique_arr:
            unique_arr.append(elem)
    print(unique_arr)


def Task4():
    matrix = [["_" for _ in range(8)] for _ in range(8)]
    matrix[0][0] = "тура"
    matrix[7][0] = "тура"
    matrix[0][7] = "тура"
    matrix[7][7] = "тура"

    print(matrix)
