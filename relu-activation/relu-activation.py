import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x=np.asarray(x, dtype=float)
    return np.asarray(np.maximum(0,x))
    maxi=0
    for i in range (x.size):
       x[i]=max(0,x[i])
    
    return x
    pass