import numpy as np
import matplotlib.pyplot as plt


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


def BoxPlot(LowWhisker, Q1, Median, Mean, Q3, HighWhisker, XCoord, Width=0.8):
    """
    Create a boxplot from stats about a dataset. Ideal for when the dataset is
    too big to process in python. Width is the width in axis units of the box,
    so typically a value of 0.8 will ensure that boxplots will not touch.

    Call plt.show() or plt.savefig() to view the boxplots.
    """

    # Half the supplied width as the boxes are drawn around a center point
    Width = Width / 2

    plt.hlines(Q1, XCoord - Width, XCoord + Width)
    plt.hlines(Mean, XCoord - Width, XCoord + Width, color='b')
    plt.hlines(Median, XCoord - Width, XCoord + Width, color='r')
    plt.hlines(Q3, XCoord - Width, XCoord + Width)

    plt.vlines(XCoord - Width, Q1, Q3)
    plt.vlines(XCoord + Width, Q1, Q3)

    # whiskers
    plt.vlines(XCoord, Q3, HighWhisker)
    plt.vlines(XCoord, LowWhisker, Q1)

    # end caps
    plt.hlines(HighWhisker, XCoord - (Width / 2.), XCoord + (Width / 2.))
    plt.hlines(LowWhisker, XCoord - (Width / 2.), XCoord + (Width / 2.))

CurvatureData = LoadData('GM', 3, '')
BoxPlot(CurvatureData[1], CurvatureData[2], CurvatureData[3], CurvatureData[4],
        CurvatureData[5], CurvatureData[6], CurvatureData[0])

plt.xlabel("Grid resolution ($m$)")
plt.ylabel("Curvature $m^{-1}$")

plt.show()
