package main

import (
	"fmt"
	"slices"
	"strings"
)

type BST struct {
	root *Node
}

func NewBST() *BST {
	return &BST{}
}

func (b *BST) find(value int) (*Node, *Node) {
	var parent *Node
	node := b.root

	for node != nil && node.value != value {
		parent = node
		if value < node.value {
			node = node.left
		} else {
			node = node.right
		}
	}
	return parent, node
}

func (b *BST) Insert(value int) *Node {
	if b.root == nil {
		b.root = &Node{value: value}
		return b.root
	}

	parent, node := b.find(value)
	if node != nil { // there is already a node with value
		return node
	}

	new_node := &Node{value: value, parent: parent}
	if value < parent.value {
		parent.left = new_node
	} else {
		parent.right = new_node
	}

	return new_node
}

func (b *BST) Search(value int) *Node {
	_, node := b.find(value)
	return node
}

func (b *BST) Delete(value int) *Node {
	found := b.Search(value)
	if found == nil {
		return nil
	}

	if found.left != nil && found.right != nil { // if there are two children
		nextInOrderNode := found.right
		for nextInOrderNode.left != nil {
			nextInOrderNode = nextInOrderNode.left
		}
		found.value = nextInOrderNode.value // swap found value with the next in order
		found = nextInOrderNode             // mark the next in order node to be deleted
	}

	child := found.right // found node has at maximum one non nil child
	if found.left != nil {
		child = found.left
	}
	if child != nil {
		child.parent = found.parent
	}

	parent := found.parent
	if parent == nil {
		b.root = child
		return b.root
	}

	if parent.left == found {
		parent.left = child
	} else {
		parent.right = child
	}
	return parent
}

func (b *BST) Print() {
	if b.root == nil {
		return
	}

	layer := []*Node{b.root}
	values := [][]string{}
	sep := []int{0, numOfCharsPerValue}

	for slices.IndexFunc(layer, func(n *Node) bool { return n != nil }) != -1 {
		newLayer := []*Node{}
		newValues := []string{}
		for _, n := range layer {
			newValues = append(newValues, n.String())
			newLayer = append(newLayer, n.l(), n.r())
		}

		layer = newLayer
		values = append(values, newValues)
		sep = append(sep, (sep[len(sep)-1]+1)*numOfCharsPerValue)
	}

	for i, vals := range values {
		fmt.Println(strings.Repeat(" ", sep[len(sep)-3-i]) + strings.Join(vals, strings.Repeat(" ", sep[len(sep)-2-i])))
	}
}
