package main

import (
	"fmt"
	"slices"
)

type Order int

const (
	Preorder Order = iota
	Inorder
	Postorder
)

func (o Order) String() string {
	switch o {
	case Preorder:
		return "preorder "
	case Inorder:
		return "inorder  "
	case Postorder:
		return "postorder"
	default:
		return ""
	}
}

func DepthFirstSearch(root *Node, ord Order) {
	if slices.Contains([]Order{Preorder, Inorder, Postorder}, ord) {
		fmt.Printf("depth first search %v: %v\n", ord, CollectDFS(root, ord))
	}
}

func CollectDFS(node *Node, ord Order) []int {
	if node == nil {
		return []int{}
	}
	left, root, right := CollectDFS(node.left, ord), []int{node.value}, CollectDFS(node.right, ord)
	switch ord {
	case Preorder:
		return slices.Concat(root, left, right)
	case Inorder:
		return slices.Concat(left, root, right)
	case Postorder:
		return slices.Concat(left, right, root)
	default:
		panic("wrong order")
	}
}

func BreadthFirstSearch(root *Node) {
	values := []int{}
	if root != nil {
		values = CollectBFS(root)
	}
	fmt.Printf("breadth first search        : %v\n", values)
}

func CollectBFS(root *Node) []int {
	var n *Node
	values := []int{}
	nodes := []*Node{root}
	for len(nodes) != 0 {
		n, nodes = nodes[0], nodes[1:]

		values = append(values, n.value)
		if n.left != nil {
			nodes = append(nodes, n.left)
		}
		if n.right != nil {
			nodes = append(nodes, n.right)
		}
	}
	return values
}

func testTreeTraversal() {
	root := NewNode(4,
		NewNode(2,
			NewNode(1, nil, nil),
			NewNode(3, nil, nil)),
		NewNode(5,
			nil,
			NewNode(6, nil, nil)))

	fmt.Println("tree:")
	fmt.Println("     4")
	fmt.Println("   /   \\")
	fmt.Println("  2     5")
	fmt.Println(" / \\     \\")
	fmt.Println("1   3     6")

	DepthFirstSearch(root, Preorder)
	DepthFirstSearch(root, Inorder)
	DepthFirstSearch(root, Postorder)
	BreadthFirstSearch(root)
}
