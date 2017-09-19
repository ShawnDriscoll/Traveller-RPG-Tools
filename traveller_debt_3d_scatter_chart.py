
from pylab import *
#from scipy import *
import csv
from pkg_resources import next
from mpl_toolkits.mplot3d import Axes3D
from diceroll import roll

path = 'data/npc_homeworlds.csv'
file_in = open(path, 'rb')
reader = csv.reader(file_in, delimiter=',')

header = next(reader)  # The first line is the header
print header

win_title = 'Debt'

figure(win_title)
ax = subplot(111, projection='3d')

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
    if row[30][:2] == 'Cr':
        #print 'hey1', row[30], row[30][2:]
        dx = int(row[30][2:]) + roll('FLUX') * 2500.0
        x.append(dx)
    else:
        #print 'ZERO'
        x.append(0 + roll('FLUX') * 2500.0)
    if row[32][:2] == 'Cr':
        #print 'hey2', row[32], row[32][2:]
        dy = int(row[32][2:]) + roll('FLUX') * 250.0
        y.append(dy)
    else:
        y.append(0 + roll('FLUX') * 250.0)
    dz = noble_hex_code[row[24]] + roll('FLUX') / 10.0
    z.append(dz)
    if row[31][:2] == 'Cr':
        #print 'heyColor', row[31], row[31][2:]
        color.append(int(row[31][2:]))
    else:
        #print 'NOTHING', row[31]
        color.append(0)
ax.scatter(x, y, z, c=color, marker='o')

ax.set_xlabel('Cash')
ax.set_ylabel('Pension')
ax.set_zlabel('Nobility')
ax.set_title(win_title)

show()