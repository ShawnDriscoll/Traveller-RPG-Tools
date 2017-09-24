
from pylab import *
#from scipy import *
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from diceroll import roll

matplotlib.rcParams['legend.handlelength'] = 0
matplotlib.rcParams['legend.numpoints'] = 1

df = pd.read_csv('data/npc_homeworlds.csv', delimiter=',').astype(str)

win_title = 'Traveller Population TC\n'

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

diebacks = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Di' in trade_codes:
            diebacks = True
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
            ax.text(px,
                    py,
                    pz,
                    df.ix[row, 'Homeworld'],
                    size=14,
                    color='black',
                    #horizontalalignment='center',
                    #verticalalignment='center'
                    )
            print row, df.ix[row, 'Homeworld'], '[Dieback]'
            
if diebacks:
    ax.scatter(x, y, z, marker='h', c='black', s=sizes, linewidths=1, edgecolor='red')
    plot([], [], [], marker='h', markerfacecolor='black', markersize = 12, markeredgewidth=1, markeredgecolor='red', label='Dieback')

x = []
y = []
z = []
colors = []
sizes = []

barrens = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ba' in trade_codes:
            barrens = True
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

if barrens:
    ax.scatter(x, y, z, marker='h', c='cyan', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='cyan', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Barren')

x = []
y = []
z = []
colors = []
sizes = []
 
lo_pops = False
 
for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Lo' in trade_codes:
            lo_pops = True
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
 
if lo_pops:
    ax.scatter(x, y, z, marker='h', c='gray', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='gray', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Low Population')

x = []
y = []
z = []
colors = []
sizes = []

non_industrials = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ni' in trade_codes:
            non_industrials = True
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

if non_industrials:
    ax.scatter(x, y, z, marker='h', c='tan', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='tan', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Non-Industrial')

x = []
y = []
z = []
colors = []
sizes = []

pre_highs = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Ph' in trade_codes:
            pre_highs = True
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

if pre_highs:
    ax.scatter(x, y, z, marker='h', c='orange', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='orange', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='Pre-High')

x = []
y = []
z = []
colors = []
sizes = []

hi_pops = False

for row in range(df.shape[0]):
    if not pd.isnull(df.ix[row, 'Trade_Codes']):
        trade_codes = df.ix[row, 'Trade_Codes']
        if 'Hi' in trade_codes:
            hi_pops = True
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
 
if hi_pops:
    ax.scatter(x, y, z, marker='h', c='red', s=sizes, linewidths=1, edgecolor='black')
    plot([], [], [], marker='h', markerfacecolor='red', markersize = 12, markeredgewidth=1, markeredgecolor='black', label='High Population')

legend(bbox_to_anchor=(1, 1), ncol=2, prop={'size': 12}, fancybox=True, title='World Polulation Levels', shadow = True)

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
