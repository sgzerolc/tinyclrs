# longest increasing subsequence
# bottom up implementation
temp = [32,14,5,7,19,22,45,6,13]
result = [5, 7, 19, 22, 45]
def lis(A):
	x = [1 for _ in A]  # memo
	parent = [None for _ in A]  # parent pointers
	for i in range(1, len(A)):  # solve dynamic program
		for j in range(i):
			if (A[j] < A[i]) and (x[i] < x[j] + 1):
				x[i] = x[j] + 1
				parent[i] = j
	last = 0  # find largest subproblem
	for i in range(1, len(A)):
		if x[last] < x[i]:
			last = i
	sequence = []  # reconstruct backward sequence
	while last is not None:
		sequence.append(A[last])
		last = parent[last]
	return sequence[::-1]  # return reversed sequence

def test_dp(f):
	if f(temp) == result:
		print("Test passed!")
	else:
		print(f(temp))
		print("Failed")
	return

test_dp(lis)

