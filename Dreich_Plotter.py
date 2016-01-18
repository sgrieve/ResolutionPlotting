import numpy as np
import matplotlib.pyplot as plt

Resolutions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24,
               26, 28, 30, 35, 40, 45, 50, 55, 60]

maxvals = [500000, 200000, 200000]

location = ['Santa Cruz Island', 'Gabilan Mesa', 'Oregon Coast Range']
prefix = ['SC', 'GM', 'OR']

for a in range(3):

    with open(prefix[a] + '_Dreich_Length.txt', 'r') as f:
        data = f.readlines()

    # find row with most values
    Orders = 0
    o = 0

    for i, d in enumerate(data):
        if len(d.strip(',\n').split(',')) > Orders:
            Orders = len(d.strip(',\n').split(','))
            o = i

    Values = np.zeros((26, Orders), dtype=np.float)

    # Fill the Values array with data, and leave zeros where there is none
    for i, d in enumerate(data):
        for j, v in enumerate(d.strip(',\n').split(',')):
            Values[i][j] = float(v)

    Totals = np.zeros(26)

    for w in range(26):
        Totals[w] = np.sum(Values[w])

    for q in range(Orders):
        plt.plot(Resolutions, Values[:, q], label='Order = ' + str(q + 1))

    plt.plot(Resolutions, Totals, label='Total Stream Length')

    plt.xlabel('Grid resolution (m)')
    plt.ylabel('Stream length (m)')
    plt.title(location[a])
    plt.legend()
    plt.savefig(prefix[a] + '_Length.png')
    plt.clf()

    for i in range(1, 26):
        plt.scatter(Values[0], Values[i], color=str(round((i / 26.), 3)),
                    marker='o', edgecolor='k')

    plt.ylabel('Stream length (m) from reduced resolution data')
    plt.xlabel('Stream length (m) from 1 meter data')
    plt.title(location[a])
    plt.plot((0, maxvals[a]), (0, maxvals[a]), 'k--')
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.savefig(prefix[a] + '_Length_Comparison.png')
    plt.clf()
