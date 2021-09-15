'''
1. Ordinary Disjoint Set
2. Quick Union
3. Quick Find
4. Union by Rank (For Quick Union)
5. Path Compression (For Quick Union, but optimizes find())
6. 4 & 5 together => Union by Rank with Path Compression

'''


# Quick Find
class QuickFind:
	def __init__(self, size):
		self.root = [i for i in range(len(size))]

	def find(self, vertex):
		return self.root[vertex]

	def connected(self, vertex1, vertex2):
		return self.find(vertex1) == self.find(vertex2)

	def union(self, v1, v2):
		root1 = self.find(v1)
		root2 = self.find(v2)
		# if they're already the same
		# => no need to connect
		if root1 != root2:
			for vertex in range(len(self.root)):
				if self.root[vertex] == root2:
					self.root[vertex] = root1

# Quick Union
class QuickUnion:
	def __init__(self, size):
		self.root = [i for i in range(len(size))]

	def find(self, vertex):
		while vertex != self.root[vertex]:
			vertex = self.root[vertex]
		return vertex

	def union(self, vertex1, vertex2):
		root1 = self.find(vertex1)
		root2 = self.find(vertex2)
		if root1 != root2:
			self.root[root2] = root1

	def connected(self, vertex1, vertex2):
		return self.find(vertex1) == self.find(vertex2)

# Disjoint Set - Union by Rank. For union() function of Quick Union
class RankDisjoinSet:
	def __init__(self, size, rank):
		self.root = [i for i in range(len(size))]
		self.rank = [1 for _ in self.root]

	def connected(self, vertex1, vertex2):
		return self.find(vertex1) == self.find(vertex2)

	def find(self, vertex):
		while vertex != self.root[vertex]:
			vertex = self.root[vertex]
		return vertex

	def union(self, vertex1, vertex2):
		root1 = self.find(vertex1)
		root2 = self.find(vertex2)
		if root1 != root2:
			if self.rank[root1] > self.rank[root2]:
				self.root[root2] = root1
			elif self.rank[root1] < self.rank[root2]:
				self.root[root1] = root2
			else:
				self.root[root2] =  root1
				self.rank[root1] += 1

# Disjoint Set - Path Compression. For find() function of Quick Union
class PathCompression:
	def __init__(self, size):
		self.root = [i for i in range(size)]

	def find(self, vertex):
		if vertex == self.root[vertex]:
			return vertex
		self.root[vertex] = self.find(self.root[vertex])
		return self.root[vertex]

	def union(self, v1, v2):
		root1 = self.find(v1)
		root2 = self.find(v2)
		if root1 != root2:
			self.root[root2] = root1

	def connected(self, v1, v2):
		return self.find(v1) == self.find(v2)

# Union by Rank with Path Compression

'''
!!!!
Pay attention that when we union 
(1, 2) without touching 0, root of 1 is 1 and we'll
add 2 to the 1, not 1.

'''
class OptimizedDisjointSet:
	def __init__(self, size):
		self.root = [i for i in range(size)]
		self.rank = [1 for _ in self.root]

	def find(self, vertex):
		if self.root[vertex] == vertex:
			return vertex
		self.root[vertex] = self.find(self.root[vertex])
		return self.root[vertex]

	def union(self, v1, v2):
		root1 = self.find(v1)
		root2 = self.find(v2)
		if root1 != root2:
			if self.rank[root1] > self.rank[root2]:
				self.root[root2] = root1
			elif self.rank[root1] < self.rank[root2]:
				self.root[root1] = root2
			else:
				self.root[root2] = root1
				self.rank[root1] += 1

	def connected(self, v1, v2):
		return self.find(v1) == self.find(v2)
