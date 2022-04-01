class PriorityQueue:
	def __init__(self):
		self.A = {}

	def insert(self, label, key):
		self.A[label] = key

	def extract_min(self):
		min_label = None
		for label in self.A:
			if (min_label is None) or (self.A[label] < self.A[min_label].key):
				min_label = label
			del self.A[min_label]
			return min_label

	def decrease_key(self, label, key):
		if (label in self.A) and (key < self.A[label]):
			self.A[label] = key
