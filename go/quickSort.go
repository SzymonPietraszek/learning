package main

import (
	"fmt"
	"strings"
)

func sort(arr []int) {
	quick_sort(arr, 0, len(arr))
}

func quick_sort(arr []int, start, end int) {
	fmt.Println(arr)
	fmt.Println(strings.Repeat("  ", start) + "| " + strings.Repeat("  ", max(0, end-start-1)) + "|")
	if end-start < 2 {
		return
	} else if end-start == 2 && arr[start] < arr[end-1] {
		swap(arr, start, end-1)
	}
	pivot := arr[start]

	l := start + 1
	r := end - 1
	for l < r {
		for l <= r && arr[l] >= pivot {
			l += 1
		}
		for l <= r && arr[r] < pivot {
			r -= 1
		}
		if l >= r {
			swap(arr, start, l-1)
			quick_sort(arr, start, l-1)
			quick_sort(arr, l, end)
			return
		}

		swap(arr, l, r)
	}
}

func swap(arr []int, i1, i2 int) {
	if i1 != i2 {
		fmt.Println(" " + strings.Repeat("  ", i1) + "x " + strings.Repeat("  ", max(0, i2-i1-1)) + "x")
		arr[i1], arr[i2] = arr[i2], arr[i1]
	}
}

func main() {
	arr := []int{3, 5, 5, 9, 3, 1, 7, 9, 3, 3, 5, 6, 1, 5, 6, 7, 3, 3, 4, 4, 2, 1, 9}
	sort(arr)
	fmt.Println(arr)
}
