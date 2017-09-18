
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

win_title = 'Nobility'

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

starport_code = {'X': 0,
                 'X': 1,
                 'X': 2,
                 'E': 3,
                 'E': 4,
                 'D': 5,
                 'D': 6,
                 'C': 7,
                 'C': 8,
                 'B': 9,
                 'B': 10,
                 'A': 11,
                 'A': 12}

x = []
y = []
z = []
color = []

for row in reader:
    dx = starport_code[row[2]] + roll('FLUX') / 5.4
    x.append(dx)
    dy = hex_code[row[9]] + roll('FLUX') / 10.0
    y.append(dy)
    dz = hex_code[row[6]] + roll('FLUX') / 10.0
    z.append(dz)
    color.append(noble_hex_code[row[24]])
ax.scatter(x, y, z, c=color, marker='o')

# print 'Atmosphere =', x
# print 'Law Level =', y
# print 'Water =', z

# for c, m, zl, zh in [('r', 'o', -50, -35), ('b', '^', -25, 25)]:
#     x = randrange(n, 23, 32)
#     y = randrange(n, 0, 100)
#     z = randrange(n, zl, zh)
#     ax.scatter(x, y, z, c=c, marker=m)

ax.set_xlabel('Starport')
ax.set_ylabel('Tech Level')
ax.set_zlabel('Population')
ax.set_title(win_title)

plt.show()