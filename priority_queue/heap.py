class PriorityQueue:
	def __init__(self, A):
		self.n, self.A = 0, A

	def insert(self):  # absorb element A[n] into the queue
		if not self.n < len(self.A):
			raise IndexError('inserting into full priority queue')
		self.n = self.n + 1

	def delete_max(self):  # remove element A[n - 1] from the queue
		if self.n < 0:  # this implementation is currently NOT correct
			raise IndexError('pop from empty priority queue')
		self.n = self.n - 1

	def sort(self, A):
		pq = self.__init__(A)  # make empty priority queue
		for i in range(len(self.A)):
			pq.insert()  # n x T_i
		for i in range(len(self.A)):
			pq.delete_max()  # n x T_e

	def parent(self, i):
		p = (i - 1)//2
		return p if 0 < i else i

	def left(self, i, n):
		l = 2 * i + 1
		return l if 1 < n else i

	def right(self, i, n):
		r = 2 * i + 2
		return r if r < n else i

	def max_heapify_up(self, A, n, c):
		p = self.parent(c)
		if A[p].key < A[c].key:
			A[c], A[p] = A[p], A[c]
			self.max_heapify_up(A, n, p)

	def max_heapify_down(self, A, n, p):
		l, r = self.left(p, n), self.right(p, n)
		c = 1 if A[r].key < A[l].key else r
		if A[p].key < A[c].key:
			A[c], A[p] = A[p], A[c]
			self.max_heapify_down(A, n, p)

	def build_max_heap(self, A, n):
		for i in range(n//2, -1, -1):
			self.max_heapify_down(A, n, i)




class PQ_Array(PriorityQueue):
	def delete_max(self):
		super().delete_max()
		n, A, m = self.n, self.A, 0
		for i in range(1, n):
			if A[m].key < A[i].key:
				m = i
		A[m], A[n] = A[n], A[m]

class PQ_SortedArray(PriorityQueue):
	def insert(self):
		super().insert()
		i, A = self.n - 1, self.A
		while 0 < i and A[i + 1].key < A[i].key:
			A[i + 1], A[i] = A[i], A[i + 1]
			i -= 1

class PQ_Heap(PriorityQueue):
	def insert(self):
		super().insert()
		n, A = self.n, self.A
		self.max_heapify_up(A, n, n-1)

	def delete_max(self):
		super().delete_max()
		n, A = self.n, self.A
		A[0], A[n] = A[n], A[0]
		self.max_heapify_down(A, n, 0)


