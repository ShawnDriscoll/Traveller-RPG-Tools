
from pylab import *
#from scipy import *
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from diceroll import roll

matplotlib.rcParams['legend.handlelength'] = 0
matplotlib.rcParams['legend.numpoints'] = 1

df = pd.read_csv('data/npc_homeworlds.csv', delimiter=',').astype(str)

win_title = 'Traveller Economic TC\n'

px_name = 'Atmosphere'
py_name = 'Hydrographics'
pz_name = 'Population'
bubble_size = 'Population'
scaler = 80

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
                  'G': 20,
                  'H': 21}

starport_code = {'X': 2,
                 'E': 4,
                 'D': 6,
                 'C': 8,
                 'B': 10,
                 'A': 12}

world_population = ['Unpopulated', 'Tens', 'Hundreds', 'Thousands',
                    'Ten Thousands', 'Hundred Thousands', 'Millions',
                    'Ten Millions', 'Hundred Millions', 'Billions',
                    'Ten Billions', 'Hundred Billions', 'Trillions',
                    'Ten Trillions', 'Hundred Trillions', 'Quadrillions']

fig = figure(win_title)
ax = subplot(111, projection='3d')

x = []
y = []
z = []
colors = []
sizes = []

agricultures = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ag' in trade_codes:
            agricultures = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            if ps == 0:
                ps = 0.3
            #sizes.append(ps ** scaler)
            sizes.append(scaler)

if agricultures:
    ax.scatter(x, y, z, marker='h', c='forestgreen', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='forestgreen', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Agricultural')

x = []
y = []
z = []
colors = []
sizes = []
 
non_agricultures = False
 
for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Na' in trade_codes:
            non_agricultures = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            if ps == 0:
                ps = 0.3
            #sizes.append(ps ** scaler)
            sizes.append(scaler)
 
if non_agricultures:
    ax.scatter(x, y, z, marker='h', c='lightblue', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='lightblue', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Non-Agricultural')

x = []
y = []
z = []
colors = []
sizes = []

industrials = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'In' in trade_codes:
            industrials = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            if ps == 0:
                ps = 0.3
            #sizes.append(ps ** scaler)
            sizes.append(scaler)

if industrials:
    ax.scatter(x, y, z, marker='h', c='blue', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='blue', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Industrial')

x = []
y = []
z = []
colors = []
sizes = []

poors = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Po' in trade_codes:
            poors = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            if ps == 0:
                ps = 0.3
            #sizes.append(ps ** scaler)
            sizes.append(scaler)
 
if poors:
    ax.scatter(x, y, z, marker='h', c='tan', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='tan', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Poor')

x = []
y = []
z = []
colors = []
sizes = []

riches = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ri' in trade_codes:
            riches = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            if ps == 0:
                ps = 0.3
            #sizes.append(ps ** scaler)
            sizes.append(scaler)

if riches:
    ax.scatter(x, y, z, marker='h', c='red', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='red', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Rich')

legend(bbox_to_anchor=(1, 1), ncol=2, prop={'size': 12}, fancybox=True, title='World Economy Types', shadow = True)

ax.set_xlim3d(-1,16)
ax.set_xticks(range(16))
ax.set_xticklabels(['Vacuum', 'Trace', 'Very Thin Tainted', 'Very Thin',
                    'Thin Tainted', 'Thin', 'Standard', 'Standard Tainted', 'Dense',
                    'Dense, Tainted', 'Exotic', 'Corrosive', 'Insidious', 'Dense High',
                    'Thin Low', 'Unusual'])
ax.set_xlabel(px_name)

ax.set_ylim3d(-1,11)
ax.set_yticks(range(11))
ax.set_yticklabels(['0','10','20','30','40','50','60','70','80','90','100'])
ax.set_ylabel(py_name + ' Percentage')

ax.set_zlim3d(-1,16)
ax.set_zticks(range(16))
ax.set_zticklabels(['Unpopulated', 'Tens', 'Hundreds', 'Thousands',
                    'Ten Thousands', 'Hund. Thousands', 'Millions',
                    'Ten Millions', 'Hund. Millions', 'Billions',
                    'Ten Billions', 'Hund. Billions', 'Trillions',
                    'Ten Trillions', 'Hund. Trillions', 'Quadrillions'])
ax.set_zlabel(pz_name)

title(win_title + ' (sampled from ' + str(len(range(df.shape[0]))) + ' worlds)')

show()
