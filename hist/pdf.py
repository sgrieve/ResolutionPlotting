import matplotlib.pyplot as plt
import numpy as np

path = '/home/s0675405/Resolution/hist/'

prefix = 'GM'

Locations = {'GM': 'Gabilan Mesa', 'SC': 'Santa Cruz Island',
             'OR': 'Oregon Coast Range'}

for a in range(1, 11):

    data = np.genfromtxt(path + prefix + '_' + str(a) + '_Hist.txt',
                         delimiter=' ', skip_header=1)

    pdfs = data[:, 4]
    bin_centers = data[:, 0]

    plt.plot(pdfs[(0.5 > bin_centers) & (-0.5 < bin_centers)] + a,
             bin_centers[(0.5 > bin_centers) & (-0.5 < bin_centers)],
             label=str(a), color='k')

    plt.plot((pdfs[(0.5 > bin_centers) & (-0.5 < bin_centers)] * -1.) + a,
             bin_centers[(0.5 > bin_centers) & (-0.5 < bin_centers)],
             label=str(a), color='k')

    plt.ylabel('Curvature')
    plt.xlabel('Probability')
    plt.title(Locations[prefix])

plt.show()
