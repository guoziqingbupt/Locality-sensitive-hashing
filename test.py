import min_hash
import numpy as np

d1 = [1, 0, 0, 1, 1, 0, 1]
d2 = [1, 1, 0, 1, 1, 0, 0]
d3 = [0, 1, 1, 0, 0, 0, 1]

dataSet = [d1, d2, d3]

query = [1, 1, 0, 1, 1, 0, 0]


def nn_search(dataSet, query):
    """

    :param dataSet: 2-dimension array
    :param query: 1-dimension array
    :return: the data columns in data set that are similarity with query
    """

    result = set()

    dataSet.append(query)
    input_matrix = np.array(dataSet).T
    hashBucket = min_hash.minHash(input_matrix, 20, 5)

    queryCol = input_matrix.shape[1] - 1

    for key in hashBucket:
        if queryCol in hashBucket[key]:
            for i in hashBucket[key]:
                result.add(i)

    result.remove(queryCol)
    return result


print(nn_search(dataSet, query))
