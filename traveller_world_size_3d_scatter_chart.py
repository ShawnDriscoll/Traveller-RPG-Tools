
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
from pkg_resources import next
from diceroll import roll

path = 'data/npc_homeworlds.csv'
file_in = open(path, 'rb')
reader = csv.reader(file_in, delimiter=',')

header = next(reader)  # The first line is the header
print header

win_title = 'World Sizes'

fig = plt.figure(win_title)
ax = fig.add_subplot(111, projection='3d')

hex_code = {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
            'G': 16,
            'H': 17,
            'J': 18,
            'K': 19}

noble_hex_code = {'0': 0,
                  '1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  'A': 10,
                  'B': 11,
                  'c': 12,
                  'C': 13,
                  'D': 14,
                  'e': 15,
                  'E': 16,
                  'f': 17,
                  'F': 18,
                  'G': 19,
                  'G': 20,
                  'H': 21}

x = []
y = []
z = []
color = []

for row in reader:
    dx = hex_code[row[4]] + roll('FLUX') / 10.0
    x.append(dx)
    dy = hex_code[row[12]] + roll('FLUX') / 10.0
    y.append(dy)
    dz = hex_code[row[5]] + roll('FLUX') / 10.0
    z.append(dz)
    color.append(hex_code[row[3]])
ax.scatter(x, y, z, c=color, marker='o')

# print 'Atmosphere =', x
# print 'Size =', y
# print 'Water =', z

# for c, m, zl, zh in [('r', 'o', -50, -35), ('b', '^', -25, 25)]:
#     x = randrange(n, 23, 32)
#     y = randrange(n, 0, 100)
#     z = randrange(n, zl, zh)
#     ax.scatter(x, y, z, c=c, marker=m)

ax.set_xlabel('Atmosphere')
ax.set_ylabel('Temperature')
ax.set_zlabel('Hydrographics')
ax.set_title(win_title)

plt.show()