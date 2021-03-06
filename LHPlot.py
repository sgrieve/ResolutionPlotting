import numpy as np
import matplotlib.pyplot as plt
import BoxPlotter


def LoadData(Prefix, InPath):
    """
    Load the data into a 2d array with the column format:

    X_coord, PC2, PC25, Median, Mean, PC75, PC98, Minimum, Maximum
    """

    with open(InPath + Prefix + '_LHResData.txt', 'r') as f:
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
        LHData = LoadData(p, Path)
        BoxPlotter.BoxPlot(LHData[1], LHData[2], LHData[3], LHData[4],
                           LHData[5], LHData[6], LHData[0])

        # Make 2 fake points to build the legend from
        plt.plot(0, 0, 'b-', label='Mean')
        plt.plot(0, 0, 'r-', label='Median')
        plt.legend(loc=4, numpoints=1, fancybox=True, markerscale=2.)

        # Place a Subplot label
        plt.annotate('A', xy=(0.96, 0.98), xycoords='axes fraction',
                     fontsize=16, horizontalalignment='left',
                     verticalalignment='top')

        plt.xlabel("Grid resolution ($m$)")
        plt.ylabel("Hillslope length ($m$)")
        plt.title(h1 + ' hillslope length')
        plt.savefig(p + '_LH.png')
        plt.clf()

CreatePlots()
