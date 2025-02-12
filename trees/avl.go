package main

import "fmt"

type AVL struct {
	BST
	heights map[int]int
}

func NewAVL() *AVL {
	return &AVL{heights: map[int]int{}}
}

func (a *AVL) Insert(val int) {
	p := a.BST.Insert(val)
	a.fixHeights(p)

	var c, cc *Node = nil, nil
	for ; p != nil; p, c, cc = p.parent, p, c {
		if a.isUnbalanced(p) {
			a.balance(p, c, cc)
			break
		}
	}
}

func (a *AVL) Delete(val int) *Node {
	p := a.BST.Delete(val)
	a.fixHeights(p)

	for ; p != nil; p = p.parent {
		if a.isUnbalanced(p) {
			c := a.getChildWithMaxHeight(p)
			cc := a.getChildWithMaxHeight(c, c == p.left)
			a.balance(p, c, cc)
		}
	}
	return nil
}

func (a *AVL) getChildWithMaxHeight(n *Node, ifEqualLeft ...bool) *Node {
	hl, hr := a.heights[n.left.v()], a.heights[n.right.v()]
	if hl > hr || (hl == hr && len(ifEqualLeft) == 1 && ifEqualLeft[0]) {
		return n.left
	}
	return n.right
}

func (a *AVL) fixHeights(n *Node) {
	for n != nil {
		a.heights[n.value] = max(a.heights[n.left.v()], a.heights[n.right.v()]) + 1
		n = n.parent
	}
}

func (a *AVL) isUnbalanced(n *Node) bool {
	dif := a.heights[n.left.v()] - a.heights[n.right.v()]
	return dif < -1 || 1 < dif
}

func (a *AVL) balance(p, c, cc *Node) {
	if (p.left == c) != (c.left == cc) { // left, right or right, left rotations
		a.rotate(c, cc)
		c = cc // after rotation a child of child of parent becomes a child of parent (goes up)
	}
	a.rotate(p, c)
}

func (a *AVL) rotate(p *Node, c *Node) {
	right := p.left == c
	fmt.Println("rotate", p.value, c.value, "right:", right)

	t0, t2 := p.parent, c.right
	if !right {
		t2 = c.left
	}
	p.parent, c.parent = c, t0
	if right {
		p.left, c.right = t2, p
	} else {
		p.right, c.left = t2, p
	}

	if t2 != nil {
		t2.parent = p
	}

	if t0 == nil {
		a.root = c
	} else if t0.left == p {
		t0.left = c
	} else if t0.right == p {
		t0.right = c
	}

	a.fixHeights(p)
}

/* THEORY
     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3

rotate right
     t0         t0
     |          |
     p          c
    / \    =>  /  \
   c   t3     t1   p
  / \             / \
 t1  t2         t2  t3
rotate left
   t0              t0
   |               |
   p               c
  /  \     =>     / \
 t1   c          p   t3
     / \        / \
   t2  t3      t1  t2
*/
