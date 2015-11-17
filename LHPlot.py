import numpy as np
import matplotlib.pyplot as plt
import BoxPlotter


def LoadData(Prefix, InPath):
    """
    Load the data into a 2d array with the column format:

    X_coord, PC2, PC25, Median, Mean, PC75, PC98, Minimum, Maximum
    """

    with open(InPath + Prefix + '_LHResData_.txt', 'r') as f:
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
    Wrapper to generate hillslope length plots from a series of data files.
    """

    prefixes = ['SC', 'OR', 'GM']
    headings1 = ['Santa Cruz Island', 'Oregon Coast Range', 'Gabilan Mesa']
    Path = ''

    for p, h1 in zip(prefixes, headings1):
        CurvData = LoadData(p, Path)
        BoxPlotter.BoxPlot(CurvData[1], CurvData[2], CurvData[3], CurvData[4],
                           CurvData[5], CurvData[6], CurvData[0])

        plt.xlabel("Grid resolution ($m$)")
        plt.ylabel("Hillslope length ($m$)")
        plt.title(h1 + ' hillslope length')
        plt.savefig(p + '_LH.png')
        plt.clf()

CreatePlots()
