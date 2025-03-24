def print_array(arr):
    print("[" + ' '.join(map(str, arr)) + "]")

def sort(arr: list[int]):
    merge_sort(arr, 0, len(arr))

def merge_sort(arr: list[int], start: int, end: int):
    print_array(arr)
    print("  " * start + "| " + "  " * (end - start - 1) + "|")
    if end - start < 2:
        return
    if end - start == 2:
        if arr[start] < arr[end - 1]:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]
        return

    pivot = (start + end) // 2
    merge_sort(arr, start, pivot)
    merge_sort(arr, pivot, end)

    sorted = []
    l, r = start, pivot
    while l < pivot or r < end:
        if r == end or (l < pivot and arr[l] >= arr[r]):
            sorted.append(arr[l])
            l += 1
        else:
            sorted.append(arr[r])
            r += 1
    arr[start:end] = sorted

arr = [3,5,5,9,3,1,7,9,3,3,5,6,1,5,6,7,3,3,4,4,2,1,9]
sort(arr)
print_array(arr)
