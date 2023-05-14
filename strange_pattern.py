import numpy as np

# implement the function strange pattern

def strange_pattern(size):
    # delete the NotImplementedError when you write your function.
    #arr = np.empty(shape = (m,n))
    #bool_array = np.array(arr, dtype = 'bool')
    bool_array = np.random.choice([True,False], size = size)
    return bool_array


if __name__ == "__main__":
    
    print(strange_pattern((2,3)))
    pass
