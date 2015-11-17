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


def CreatePlots():
    """
    Wrapper to generate curvature plots from a series of data files.
    """

    prefixes = ['SC', 'OR', 'GM']
    types = range(3, 7)
    Path = ''

    headings1 = ['Santa Cruz Island', 'Oregon Coast Range', 'Gabilan Mesa']
    headings2 = ['Total Curvature', 'Planform Curvature', 'Profile Curvature',
                 'Tan Curvature']

    for p, h1 in zip(prefixes, headings1):
        for t, h2 in zip(types, headings2):
            CurvData = LoadData(p, t, Path)
            BoxPlotter.BoxPlot(CurvData[1], CurvData[2], CurvData[3],
                               CurvData[4], CurvData[5], CurvData[6],
                               CurvData[0])

            plt.xlabel("Grid resolution ($m$)")
            plt.ylabel("Curvature $m^{-1}$")
            plt.title(h1 + ' ' + h2)
            plt.savefig(p + '_Curv_' + str(t) + '.png')
            plt.clf()

CreatePlots()
