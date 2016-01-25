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

            # Load the data file
            CurvData = LoadData(p, t, Path)

            # Plot the boxplots on the main axes
            BoxPlotter.BoxPlot(CurvData[1], CurvData[2], CurvData[3],
                               CurvData[4], CurvData[5], CurvData[6],
                               CurvData[0])

            plt.xlabel("Grid resolution ($m$)")
            plt.ylabel("Curvature ($m^{-1}$)")
            plt.title(h1 + ' ' + h2)
            plt.xlim(0, 65)

            # Make 2 fake points to build the legend from
            plt.plot(700, 0, 'b.', label='Mean')
            plt.plot(700, 0, 'r.', label='Median')
            plt.legend(loc=4, numpoints=1, fancybox=True, markerscale=2.)

            # Place a Subplot label
            plt.annotate('A', xy=(0.96, 0.98), xycoords='axes fraction',
                         fontsize=16, horizontalalignment='left',
                         verticalalignment='top')

            # Plot the inset of the mean and median data
            inset = plt.axes([0.58, 0.58, 0.28, 0.28])
            plt.plot(CurvData[0], CurvData[3], 'r.')
            plt.plot(CurvData[0], CurvData[4], 'b.')
            plt.hlines(0, 0, 65, linestyles='dotted', zorder=1000)
            plt.xlim(0, 65)
            plt.xlabel("Grid resolution ($m$)", fontsize=10)
            plt.ylabel("Curvature ($m^{-1}$)", fontsize=10)
            plt.tick_params(axis='both', labelsize=9, length=0)

            # Save the figure
            plt.savefig(p + '_Curv_' + str(t) + '.png')
            plt.clf()

CreatePlots()
