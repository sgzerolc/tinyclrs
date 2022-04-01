# sort in ascending order
def selection_sort(Arr):
	#grow a subset the smallest i items in sorted order
	for i in range(len(Arr)):
		smaller = i;
		for j in range(i, len(Arr)): # offbyone error
			if Arr[j] < Arr[smaller]:
				smaller = j
		Arr[smaller], Arr[i] = Arr[i], Arr[smaller]
	return Arr


def insertion_sort(Arr):
	# grow a subset the first i input items in sorted order
	for i in range(1, len(Arr)): # offbyone error
		pointer = i
		while pointer > 0 and Arr[pointer] < Arr[pointer-1]:
			Arr[pointer], Arr[pointer-1] = Arr[pointer-1], Arr[pointer]
			pointer -= 1
	return Arr

def merge_sort(Arr):
	size = len(Arr)
	if size == 1:
		return Arr
	mid = size//2
	Left = merge_sort(Arr[:mid])
	Right = merge_sort(Arr[mid:])
	i,j = 0,0
	start = 0
	while start < size:
		if j >= len(Right) or (i < len(Left) and Left[i] < Right[j]): # offbyone error
			Arr[start] = Left[i]
			i += 1
		else:
			Arr[start] = Right[j]
			j += 1
		start += 1
	return Arr # missing return value

def Merge_Sort(A, a = 0, b = None):
	if b is None:
		b = len(A)
	mid = (a+b+1)//2
	Merge_Sort(A, a, mid)
	Merge_Sort(A, mid, b)
	L,R = A[a:mid],A[mid:b]
	i,j=0,0
	while a < b:
		if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
			A[a] = L[i]
			i += 1
		else:
			A[a] = R[j]
			j+=1
		a += 1
	



# def direct_access_sort(A):
# 	"sort A assuming items have distinct non-negative keys"
# 	u = 1 + max([x.key for x in A]) # x.key < u(array size)
# 	D = [None]*u
# 	for x in A:
# 		D[x.key] = x
# 	i = 0
# 	for key in range(u):
# 		if D[key] is not None:
# 			A[i] = D[key]
# 			i += 1


def counting_sort(A):
    "sort A assuming items have non-negative keys"
    u = 1 + max([x.key for x in A])
    D = [0] * u
    for x in A:
        D[x.key] += 1
    for k in range(1,u):
        D[k] += D[k-1]
    for x in list(reversed(A)):
        A[D[x.key]-1] = x
        D[x.key] -= 1

def radix_sort(A):
    "sort A assuming items have non-negative keys"
    n = len(A)
    u = 1 + max([x.key for x in A])
    c = 1 + (u.bit_length()//n.bit_length())
    class Obj:pass
    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):
            high,low = divmod(high,n)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item
	



test1 = [0,3,1,8,4,5]
test2=[3,1]
is_sorted = sorted(test1)

def test_sort(f):
	if f(test1) == is_sorted:
		print("Test passed!")
	else:
		print(f(test2))
		print("Failed")
	return;

# test_sort(selection_sort)
# test_sort(insertion_sort)
# test_sort(merge_sort)

