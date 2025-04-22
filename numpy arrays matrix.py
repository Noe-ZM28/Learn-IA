import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

d = np.array([a, b, c])

x = np.array([a])
y = np.array([b])
z = np.array([c])

# 2a + b  3c = 7
# 5a - 4b + c = -19
# a - b -4c = 4

x1 = np.array(
    [[2, 1, 3], 
     [5,-4, 1], 
     [1,-1, -4]
     ])
x2 = np.array([7, -19, 4])

print(np.linalg.solve(x1, x2))


