n, p = 10, 4  # observations x features

np.random.seed(0)                      # we seed the random number generator (RNG), This ensures reproducibility — every run gives the same random numbers.
Y = np.random.randint(2, size=n)       # 1D array of n outputs from values {0,1},Represents a binary classification target
# Y =  [0 0 1 1 0 0 0 1 1 1]
X = np.random.randint(10, size=(n, p)) # 2D array data matrix with n observations from values {0,1,2,3,4,5,6,7,8,9}, Creates a 10×4 matrix. Represents 4 features per observation
# X = 
 [[9 9 5 7]
 [6 0 4 7]
 [8 1 6 2]
 [2 1 3 5]
 [8 1 8 7]
 [8 1 0 5]
 [4 1 5 4]
 [7 6 0 0]
 [9 2 4 5]
 [8 8 7 5]]
print('Y = ', Y)
print('X = \n', X)

import numpy as np

np.random.seed(0) # Initialize RNG with state 0
print(np.random.randint(10, size=5))
# → [5 0 3 3 7]

np.random.seed(3) # Initialize RNG with state 3
print(np.random.randint(10, size=5))
# → [8 9 3 8 8]
