# longest increasing subsequence
# bottom up implementation
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


# Longest Palindromic Sequence
def L(i, j):
    if Dict[i][j] != 0:  # memorization
        return Dict[i][j]
    if i == j:
        Dict[i][j] = 1
        return 1
    if X[i] == X[j]:
        if i + 1 == j:
            Dict[i][j] = 2
            return 2
        else:
            Dict[i][j] = 2 + L(i + 1, j - 1)
            return Dict[i][j]
    else:
        Dict[i][j] = max(L(i + 1, j), L(i, j - 1))
        return Dict[i][j]


def printLPS(i, j):
    if i > j:
        return ""
    if i == j:
        return X[i]
    if X[i] == X[j]:
        return X[i] + printLPS(i + 1, j - 1) + X[j]
    if Dict[i][j - 1] > Dict[i + 1][j]:
        return printLPS(i, j - 1)
    return printLPS(i + 1, j)


## Iteratively,

# False: one dimension data can not cover all the subproblems. That's where
# I was stuck.
# def palindr(X):
# 	C = [1 for _ in X] # prefix
# 	# parent = [None for _ in A]
# 	for i in range(1, len(X)):
# 		for j in range(i):
# 			if X[i] == X[j]:
# 				if i + 1 == j:
# 					C[i] = C[i-1] + 1
# 				else:
# 					C[i] = C[i-1] + 2
# 			else:
# 				C[i] = max(C)
# 	print(C)


def palindr(X):
    n = len(X)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        C[i][i] = 1
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if X[i] == X[j] and L == 2:
                C[i][j] = 2
            elif X[i] == X[j]:
                C[i][j] = C[i + 1][j - 1] + 2
            else:
                C[i][j] = max(C[i][j - 1], C[i + 1][j])

    return C[0][n - 1]


if __name__ == "__main__":
    temp = [32, 14, 5, 7, 19, 22, 45, 6, 13]
    result = [5, 7, 19, 22, 45]
    test_dp(lis)

    X = "underqualified"
    # X = 'apple'
    n = len(X)
    Dict = [[0 for _ in range(n)] for _ in range(n)]
    Seq = ""
    print(L(0, n - 1))
    print("Longest Palindromic Sequence: ", printLPS(0, len(X) - 1))
    for i in range(n):
        print(Dict[i])

    print(palindr(X))
