import numpy as np
import matplotlib.pyplot as plt
import string
from matplotlib import rcParams
import BoxPlotter

# Set up fonts for plots
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

Locations = {'GM': 'Gabilan Mesa', 'SC': 'Santa Cruz Island',
             'OR': 'Oregon Coast Range'}


def LoadData(Prefix, CurvType, InPath):
    """
    Load the data into a 2d array with the column format:

    X_coord, PC2, PC25, Median, Mean, PC75, PC98, Minimum, Maximum
    """

    with open(InPath + Prefix + '_ChtResData_noscaling.txt', 'r') as f:
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


def LoadTanData(Prefix, CurvType, InPath):
    """
    Load the data into a 2d array with the column format:

    X_coord, PC2, PC25, Median, Mean, PC75, PC98, Minimum, Maximum
    """

    with open(InPath + Prefix + '_CurvatureResData_3_noscaling.txt', 'r') as f:
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

Resolutions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24,
               26, 28, 30, 35, 40, 45, 50, 55, 60]

Resolutions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

labels = list(string.ascii_lowercase)[:2]

colors = ['b', 'k', 'r']

for i, q in enumerate(['SC', 'GM', 'OR']):

    CurvData = LoadData(q, 6, 'cht/')

    CHTs = np.array(CurvData[3])
    CHTs_low = CHTs - np.array(CurvData[2])
    CHTs_high = np.array(CurvData[5]) - CHTs

    Resolutions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    plt.subplot(211)
    plt.title('Hilltop Curvature')

    if not i:
        plt.annotate(labels[0], xy=(0.02, 0.95), xycoords='axes fraction',
                     fontsize=14, horizontalalignment='left',
                     verticalalignment='top')

    # plt.plot(Resolutions, CHTs, color=colors[i], label=Locations[q])
    BoxPlotter.BoxPlot(CurvData[1], CurvData[2], CurvData[3],
                       CurvData[4], CurvData[5], CurvData[6],
                       CurvData[0])

    plt.xlabel("Grid resolution ($m$)")
    plt.ylabel("Curvature ($m^{-1}$)")
    plt.tick_params(axis='x', which='both', top='off', length=2)
    plt.tick_params(axis='y', which='both', right='off', length=2)
'''
#    plt.ylim(ymax=0.0025)

    TanData = LoadTanData(q, 6, 'cht/')

    Tans = np.array(TanData[3])
    Tans_low = Tans - np.array(TanData[2])
    Tans_high = np.array(TanData[5]) - Tans

    # plt.subplot(212)
    plt.title('Total Curvature ' + Locations[q])

    '''
    if not i:
        plt.annotate(labels[1], xy=(0.02, 0.95), xycoords='axes fraction',
                     fontsize=14, horizontalalignment='left',
                     verticalalignment='top')
    '''

    # plt.plot(Resolutions, Tans, color=colors[i], label=Locations[q])
    BoxPlotter.BoxPlot(TanData[1], TanData[2], TanData[3],
                       TanData[4], TanData[5], TanData[6],
                       TanData[0])

    LowWhisk = TanData[1]
    HighWhisk = TanData[6]

    for a in range(1, 11):
        path = '/home/s0675405/Resolution/hist/'
        data = np.genfromtxt(path + q + '_' + str(a) + '_Hist.txt',
                             delimiter=' ', skip_header=1)

        pdfs = data[:, 4]
        bin_centers = data[:, 0]

        plt.plot(pdfs[(HighWhisk[a - 1] > bin_centers) & (LowWhisk[a - 1] < bin_centers)] + a,
                 bin_centers[(HighWhisk[a - 1] > bin_centers) & (LowWhisk[a - 1] < bin_centers)],
                 color='k')

        plt.plot((pdfs[(HighWhisk[a - 1] > bin_centers) & (LowWhisk[a - 1] < bin_centers)] * -1.) + a,
                 bin_centers[(HighWhisk[a - 1] > bin_centers) & (LowWhisk[a - 1] < bin_centers)],
                 color='k')

    plt.xlabel("Grid resolution ($m$)")
    plt.ylabel("Curvature ($m^{-1}$)")
    plt.tick_params(axis='x', which='both', top='off', length=2)
    plt.tick_params(axis='y', which='both', right='off', length=2)

    # plt.ylim(ymax=0.0002)

    plt.tight_layout()

#    plt.legend(loc=0)
    plt.show()
