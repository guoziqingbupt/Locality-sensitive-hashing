import csv
import numpy as np


def readData(fileName):
    """read csv data"""

    dataSet = []
    with open(fileName, "r") as csvFile:
        reader = csv.reader(csvFile)
        for line in reader:
            dataSet.append([float(item) for item in line])

    return dataSet


def euclideanDistance(v1, v2):
    """get euclidean distance of 2 vectors"""

    v1, v2 = np.array(v1), np.array(v2)
    return np.sqrt(np.sum(np.square(v1 - v2)))