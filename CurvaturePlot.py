import numpy as np
import matplotlib.pyplot as plt
import BoxPlotter


def LoadData(Prefix, CurvType, InPath):
    """
    Load the data into a 2d array with the column format:

    X_coord, PC2, PC25, Median, Mean, PC75, PC98, Minimum, Maximum
    """

    with open(InPath + Prefix + '_CurvatureResData_'
              + str(CurvType) + '.txt', 'r') as f:

        f.readline()
        data = f.readlines()

    no_of_lines = len(data)
    no_of_cols = len(data[0].split())

    Data = np.zeros((no_of_cols, no_of_lines), dtype='float64')

    for i, r in enumerate(data):
        split = r.split()
        for a in range(no_of_cols):
            Data[a][i] = split[a]

    return Data


CurvatureData = LoadData('GM', 3, '')
BoxPlotter.BoxPlot(CurvatureData[1], CurvatureData[2], CurvatureData[3],
                   CurvatureData[4], CurvatureData[5], CurvatureData[6],
                   CurvatureData[0])

plt.xlabel("Grid resolution ($m$)")
plt.ylabel("Curvature $m^{-1}$")

plt.show()
