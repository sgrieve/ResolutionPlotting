import numpy as np
import matplotlib.pyplot as plt

Locations = {'GM': 'Gabilan Mesa', 'SC': 'Santa Cruz Island',
             'OR': 'Oregon Coast Range'}
yLims = {'GM': 350000, 'SC': 800000, 'OR': 350000}

prefixes = ['GM', 'OR', 'SC']
path = '/home/s0675405/Resolution/NewChanData/'

for method in ['Dreich', 'Pelletier']:

    for prefix in prefixes:

        data = np.genfromtxt(path + prefix + '_' + method + '_Length_new.txt',
                             delimiter=',', usemask=True)

        data = np.ma.masked_where(data == -9999, data)
        Resolutions = data[:, 0]

        for q in range(1, len(data[0])):
            # plt.plot(Resolutions, data[:, q], 'o', label=str(q))
            # plt.plot(Resolutions, data[:, q],
            #           color=str(round(((q * 1.) / len(data[0])), 3)),
            #           label=str(q))

            plt.plot(Resolutions, data[:, q], color='k', label=str(q))
            plt.text(Resolutions[0], data[:, q][0], str(q))

        plt.xlabel('Resolution (m)')
        plt.ylabel('Channel length (m)')
        plt.ylim(ymax=yLims[prefix])
        plt.title(Locations[prefix] + ' ' + method + ' Length')

        # plt.legend()
        # plt.show()
        plt.savefig(path + prefix + method + '.png')
        plt.clf()
