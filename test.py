import min_hash
import numpy as np

d1 = [1, 0, 0, 1, 1, 0, 1]
d2 = [1, 1, 0, 1, 1, 0, 0]
d3 = [0, 1, 1, 0, 0, 0, 1]

input_matrix = np.array([d1, d2, d3]).T

print(len(min_hash.minHash(input_matrix, 20, 5)))
