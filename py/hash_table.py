class HashTable:
	def __init__(self, size):
		self.size = size
		self.data = [None] * size

	def hkey(self, key):
		return hash(key) % self.size

	def set(self, key, value):
		print("set", self.hkey(key), value)
		if self.data[self.hkey(key)] is None:
			self.data[self.hkey(key)] = {}
		self.data[self.hkey(key)][key] = value

	def get(self, key):
		print("get", self.hkey(key))
		return self.data[self.hkey(key)][key]

ht = HashTable(5)
d = {"qwe": "1", "asd": "2", "zxc": "3", "rty": "4", "fgh": "5"}
for key, val in d.items():
	ht.set(key, val)
for key in d:
	print(ht.get(key))
