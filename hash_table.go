package main

import (
	"fmt"
	"hash/fnv"
)

func hash(v string, mod int) int {
	h := fnv.New32a()
	h.Write([]byte(v))
	return int(h.Sum32()) % mod
}

type HashTable struct {
	data []map[string]string
}

func NewHashTable(size int) *HashTable {
	return &HashTable{data: make([]map[string]string, size)}
}

func (h *HashTable) Set(key string, val string) {
	hkey := hash(key, len(h.data))
	fmt.Println("Set", key, val, "hash", hkey)
	if h.data[hkey] == nil {
		h.data[hkey] = make(map[string]string)
	}
	h.data[hkey][key] = val
}

func (h *HashTable) Get(key string) string {
	hkey := hash(key, len(h.data))
	fmt.Println("Get", key, "hash", hkey)
	return h.data[hkey][key]
}

func main() {
	h := NewHashTable(5)
	d := map[string]string{"qwe": "1", "asd": "2", "zxc": "3", "rty": "4", "fgh": "5"}
	for key, val := range d {
		h.Set(key, val)
	}
	for key, _ := range d {
		fmt.Println(h.Get(key))
	}
}
