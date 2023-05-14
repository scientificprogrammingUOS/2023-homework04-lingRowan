import numpy as np

# implement the function strange pattern

def strange_pattern(size):
<<<<<<< HEAD
=======
    # delete the NotImplementedError when you write your function.
    #arr = np.empty(shape = (m,n))
    #bool_array = np.array(arr, dtype = 'bool')
>>>>>>> e5c3f973a73d89a49e128c0f7c925c93bccd02ca
    bool_array = np.random.choice([True,False], size = size)
    return bool_array


if __name__ == "__main__":
    
    print(strange_pattern((2,3)))
    pass
