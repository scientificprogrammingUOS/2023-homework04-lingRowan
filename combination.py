import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a,b):
    combining = np.concatenate((a,b))
    return combining


if __name__ == "__main__":
    # use this for your own testing!
    print(combination([1,6,9],[3,5,9]))
    
