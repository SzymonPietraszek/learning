def sort(arr):
    quick_sort(arr, 0, len(arr))


def quick_sort(arr, start, end):
    print(arr)
    print("   " * start + "| " + "   " * (end - start - 1) + "|")
    if end - start < 2:
        return
    if end - start == 2 and arr[start] < arr[end - 1]:
        swap(arr, start, end - 1)
    pivot = arr[start]

    l = start + 1
    r = end - 1
    while l < r:
        while l <= r and arr[l] >= pivot:
            l += 1
        while l <= r and arr[r] < pivot:
            r -= 1
        if l >= r:
            swap(arr, start, l - 1)
            quick_sort(arr, start, l - 1)
            quick_sort(arr, l, end)
            return

        swap(arr, l, r)


def swap(arr, i1, i2):
    if i1 != i2:
        print(" " + "   " * i1 + "x  " + "   " * (i2 - i1 - 1) + "x")
        arr[i1], arr[i2] = arr[i2], arr[i1]


arr = [3, 5, 5, 9, 3, 1, 7, 9, 3, 3, 5, 6, 1, 5, 6, 7, 3, 3, 4, 4, 2, 1, 9]
sort(arr)
print(arr)
