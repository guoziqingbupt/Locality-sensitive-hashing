import e2LSH
from test_helper import *


if __name__ == "__main__":

    C = pow(2, 32) - 5
    dataSet = readData("test_data.csv")
    query = [-2.7769, -5.6967, 5.9179, 0.37671, 1]

    indexes = e2LSH.nn_search(dataSet, query, k=20, L=5, r=1, tableSize=20)
    for index in indexes:
        print(euclideanDistance(dataSet[index], query))
