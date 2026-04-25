n, p = 10, 4                     # number of n observations and p features
rng = np.random.RandomState(0)   # save the random state object that can be used to seed sampling from distributions
Y, X = rng.randint(2, size=n), rng.randint(10, size=(n, p))

print('Y = ', Y)
print('X = \n', X)

Y =  [0 1 1 0 1 1 1 1 1 1]
X = 
 [[5 2 4 7]
 [6 8 8 1]
 [6 7 7 8]
 [1 5 9 8]
 [9 4 3 0]
 [3 5 0 2]
 [3 8 1 3]
 [3 3 7 0]
 [1 9 9 0]
 [4 7 3 2]]
