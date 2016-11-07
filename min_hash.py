import numpy as np
import random
import hashlib


def rowPermutation(matrix):
    """
    * permute the row of the matrix

    :param matrix: a ndarray var
    :return a new matrix that has been permuted: a ndarray var
    """

    # the row sequence set
    seqSet = [i for i in range(matrix.shape[0])]

    # choose a row of matrix randomly
    randomSeq = random.choice(seqSet)

    # build the new matrix
    new_matrix = np.array([matrix[randomSeq]])
    seqSet.remove(randomSeq)

    while len(seqSet) != 0:
        r = random.choice(seqSet)

        # add a new row into new matrix
        new_matrix = np.row_stack((new_matrix, matrix[r]))
        seqSet.remove(r)

    return new_matrix


def sigGen(matrix):
    """
    * generate the signature vector

    :param matrix: a ndarray var
    :return a signature vector: a list var
    """

    result = []

    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[0]):

            # find the first row of i column whose value is not 0(is 1)
            if matrix[j][i] != 0:
                result.append(j)
                break

    # return a list
    return result


def sigMatrixGen(input_matrix, n):
    """
    generate the sig matrix

    :param input_matrix: naarray var
    :param n: the row number of sig matrix which we set
    :return sig matrix: ndarray var
    """

    result = []

    for i in range(n):
        new_matrix = rowPermutation(input_matrix)
        result.append(sigGen(new_matrix))

    # return a ndarray
    return np.array(result)


def minHash(input_matrix, b, r):
    """

    map the sim vector into same hash bucket
    :param input_matrix:
    :param b: the number of bands
    :param r: the row number of a band
    :return the hash bucket: a dictionary, key is hash value, value is column number
    """

    hashBuckets = {}

    # permute the matrix for n times
    n = b * r

    # generate the sig matrix
    sigMatrix = sigMatrixGen(input_matrix, n)

    # begin and end of band row
    begin, end = 0, r

    # count the number of band level
    count = 0

    while end <= sigMatrix.shape[0]:

        count += 1

        # traverse the column of sig matrix
        for colNum in range(sigMatrix.shape[1]):

            # generate the hash object, we used md5
            hashObj = hashlib.md5()

            # calculate the hash value
            band = str(sigMatrix[begin: begin + r, colNum]) + str(count)
            hashObj.update(band.encode())

            # use hash value as bucket tag
            tag = hashObj.hexdigest()

            # update the dictionary
            if tag not in hashBuckets:
                hashBuckets[tag] = [colNum]
            elif colNum not in hashBuckets[tag]:
                hashBuckets[tag].append(colNum)
        begin += r
        end += r

    # return a dictionary
    return hashBuckets


