package main

import (
	"fmt"
	"strings"
)

func sort(arr []int) {
	mergeSort(arr, 0, len(arr))
}

func mergeSort(arr []int, start, end int) {
	fmt.Println(arr)
	fmt.Println(strings.Repeat("  ", start) + "| " + strings.Repeat("  ", max(0, end-start-1)) + "|")
	if end-start < 2 {
		return
	} else if end-start == 2 {
		if arr[start] < arr[end-1] {
			arr[start], arr[end-1] = arr[end-1], arr[start]
		}
		return
	}

	pivot := (start + end) / 2
	mergeSort(arr, start, pivot)
	mergeSort(arr, pivot, end)

	sorted := []int{}
	l, r := start, pivot
	for l < pivot || r < end {
		if r == end || (l < pivot && arr[l] >= arr[r]) {
			sorted = append(sorted, arr[l])
			l++
		} else {
			sorted = append(sorted, arr[r])
			r++
		}
	}
	for i := start; i < end; i++ {
		arr[i] = sorted[i-start]
	}
}

func main() {
	arr := []int{3, 5, 5, 9, 3, 1, 7, 9, 3, 3, 5, 6, 1, 5, 6, 7, 3, 3, 4, 4, 2, 1, 9}
	sort(arr)
	fmt.Println(arr)
}
