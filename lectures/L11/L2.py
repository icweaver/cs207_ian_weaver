import numpy as np

def L2(v, *args):
    """Returns the L2 norm of v with optional weighting provided by *args[0].
    
    INPUTS
    =======
    v: list, vector or length n
    *args: list, optional, vector weights of length n, with components w_i 
    
    RETURNS
    ========
    norm: float
        has the form norm = sqrt(v_1^2 + v_2^2 + ... + v_n^2) if no *args specified,
        norm = sqrt((v_1*w_1)^2 + (v_2*w_2)^2 + ... + (v_n*w_n)^2), otherwise
        
    EXAMPLES
    =========
    >>> L2([3,4])
    5.0
    >>> round(L2([3,4], [1, 0.9]), 3)
    4.686
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)