import min_hash
import numpy as np
import e2LSH
import random

# d1 = [1, 0, 0, 1, 1, 0, 1]
# d2 = [1, 1, 0, 1, 1, 0, 0]
# d3 = [0, 1, 1, 0, 0, 0, 1]
#
# dataSet = [d1, d2, d3]
# query = [1, 1, 0, 1, 1, 0, 0]
#
# print(min_hash.minHash_nn_search(dataSet, query))


def pStableTest():

    dataSet = [(random.randint(-100, 100), random.randint(-100, 100)) for i in range(100)]
    hashTable = e2LSH.e2LSH(dataSet, k=10, L=30, r=1, tableSize=10)
    for node in hashTable:
        for fp in node.buckets:
            if len(node.buckets[fp]) > 1:
                print([dataSet[index] for index in node.buckets[fp]])

if __name__ == "__main__":
    pStableTest()