import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A=np.asarray(A)


    n,m = A.shape
    B=np.empty((m,n), dtype=A.dtype)
    for i in range(n):
        for j in range(m):
            B[j][i]=A[i][j]

    return B
    pass
