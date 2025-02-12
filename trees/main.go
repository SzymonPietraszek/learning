package main

import (
	"fmt"
)

func main() {
	tree := NewBST()

	fmt.Println("Empty tree print")
	tree.Print()
	fmt.Println("Empty tree search", tree.Search(0))
	tree.Delete(0)
	fmt.Println("Empty tree delete")

	for _, i := range []int{60, 40, 30, 70, 80, 50, 10, 20} {
		fmt.Printf("insert(%d)\n", i)
		tree.Insert(i)
		tree.Print()
	}

	for _, i := range []int{30, 60, 50, 90} {
		fmt.Printf("search(%d): %s\n", i, tree.Search(i))
	}

	for _, i := range []int{30, 50, 70, 60} {
		fmt.Printf("delete(%d)\n", i)
		tree.Delete(i)
		tree.Print()
	}
}
