import numpy as np


a = np.array([[3, 1], 
              [1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors[:, 0])
print(eigenvectors[:, 1])

print("asd")