
from pylab import *
#from scipy import *
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from diceroll import roll

matplotlib.rcParams['legend.handlelength'] = 0
matplotlib.rcParams['legend.numpoints'] = 1

df = pd.read_csv('data/npc_homeworlds.csv', delimiter=',').astype(str)

win_title = 'Traveller Planetary TC\n'

px_name = 'Atmosphere'
py_name = 'Hydrographics'
pz_name = 'Size'
bubble_size = 'Size'
scaler = 2.5
worlds = 0

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

asteroids = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'As' in trade_codes:
            asteroids = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(0.3 ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'

if asteroids:
    ax.scatter(x, y, z, marker='h', c='ivory', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='ivory', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Asteroid')

x = []
y = []
z = []
colors = []
sizes = []
 
deserts = False
 
for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'De' in trade_codes:
            deserts = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(ps ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'
                
if deserts:
    ax.scatter(x, y, z, marker='h', c='tan', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='tan', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Desert')

x = []
y = []
z = []
colors = []
sizes = []

fluids = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Fl' in trade_codes:
            fluids = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(ps ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'

if fluids:
    ax.scatter(x, y, z, marker='h', c='orange', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='orange', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Fluid')

x = []
y = []
z = []
colors = []
sizes = []

gardens = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ga' in trade_codes:
            gardens = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(ps ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'

if gardens:
    ax.scatter(x, y, z, marker='h', c='seagreen', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='seagreen', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Garden')

x = []
y = []
z = []
colors = []
sizes = []

ice_caps = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ic' in trade_codes:
            ice_caps = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(ps ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'

if ice_caps:
    ax.scatter(x, y, z, marker='h', c='cyan', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='cyan', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Ice-Capped')

x = []
y = []
z = []
colors = []
sizes = []

vacuums = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Va' in trade_codes:
            vacuums = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(ps ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'

if vacuums:
    ax.scatter(x, y, z, marker='h', c='gray', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='gray', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Vacuum')

x = []
y = []
z = []
colors = []
sizes = []

water_worlds = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Wa' in trade_codes:
            water_worlds = True
            px = hex_code[df.ix[row, px_name]] + roll('FLUX') / 10.0
            x.append(px)
            py = hex_code[df.ix[row, py_name]] + roll('FLUX') / 10.0
            y.append(py)
            pz = hex_code[df.ix[row, pz_name]] + roll('FLUX') / 10.0
            z.append(pz)
            ps = hex_code[df.ix[row, bubble_size]]
            sizes.append(ps ** scaler)
            #sizes.append(scaler)
            worlds += 1
            if hex_code[df.ix[row, 'Population']] >= 11:
                ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='red',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
                print row, df.ix[row, 'Homeworld'], '[' + world_population[hex_code[df.ix[row, 'Population']]] + ']'

if water_worlds:
    ax.scatter(x, y, z, marker='h', c='royalblue', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='royalblue', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Water')

legend(bbox_to_anchor=(1, 1), ncol=2, prop={'size': 12}, fancybox=True, title='World Characteristic Types', shadow = True)

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

ax.set_zlim3d(-1,11)
ax.set_zticks(range(11))
ax.set_zticklabels(['Asteroid Belt', '1,600 km', '3,200 km', '4,800 km', '6,400 km',
                    '8,000 km', '9,600 km', '11,200 km', '12,800 km', '14,400 km', '16,000 km'])
ax.set_zlabel(pz_name + ' (in kilometers)')

title(win_title + ' (' + str(worlds) + ' out of a sampled ' + str(len(range(df.shape[0]))) + ' worlds)')

show()
