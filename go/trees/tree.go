package main

import (
	"fmt"
	"strings"
)

const numOfCharsPerValue = 2

type Node struct {
	value               int
	parent, left, right *Node
}

func NewNode(value int, left *Node, right *Node) *Node {
	n := &Node{value: value}
	if left != nil {
		n.left = left
		left.parent = n
	}
	if right != nil {
		n.right = right
		right.parent = n
	}
	return n
}

func (n *Node) String() string {
	return getWithNil(n, strings.Repeat(".", numOfCharsPerValue),
		func(n *Node) string { return fmt.Sprintf("%*d", numOfCharsPerValue, n.value) })
}

func (n *Node) v() int   { return getWithNil(n, 0, func(n *Node) int { return n.value }) }
func (n *Node) l() *Node { return getWithNil(n, nil, func(n *Node) *Node { return n.left }) }
func (n *Node) r() *Node { return getWithNil(n, nil, func(n *Node) *Node { return n.right }) }
func getWithNil[T string | int | *Node](n *Node, defVal T, f func(*Node) T) T {
	if n == nil {
		return defVal
	}
	return f(n)
}

type Tree interface {
	Delete(value int) *Node
	Insert(value int) *Node
	Print()
	Search(value int) *Node
}

func testTree(tree Tree) {
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
