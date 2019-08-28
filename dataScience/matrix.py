A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [3, 4], [5, 6]]


# Shape of matrix

def shape(A):
    num_row = len(A)
    num_cols = len(A[0])
    return num_row, num_cols


print(shape(B))


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


print(A[0])
print(B[0])


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)
print(shape(identity_matrix))
