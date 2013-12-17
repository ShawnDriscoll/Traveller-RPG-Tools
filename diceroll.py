#   For Python 2.5.4
#
#   To use this module: from diceroll import roll
#
#   Make a dice roll for calling module
#
##########################################################

from random import randint

def roll(dice):
    "\nUsage: roll('2D6')   this will roll two D6 dice\n       roll('D66')   this will roll a D66\n       roll('D00')   this will roll a D100\n       roll('1D6+6') this will roll a D6 and add 6 to it\n"
    dm = 0
    # is there any modifier added?
    if len(dice) > 3:
        dm = eval(dice[3:len(dice)])
        dice = dice[0:3]
    if dice == '2D6':
        return randint(1,6) + randint(1,6) + dm
    if dice == '1D6':
        return randint(1,6) + dm
    if dice == '1D3':
        return randint(1,3) + dm
    if dice == 'D66':
        return randint(1,6) * 10 + randint(1,6) + dm
    if dice == '1D2':
        return randint(1,2) + dm
    if dice == '1D4':
        return randint(1,4) + dm
    if dice == 'D00':
        return (randint(1,10) - 1) * 10 + randint(1,10) + dm  # 1 - 100
    if dice == '1D5':
        return randint(1,5) + dm
    if dice == '1D8':
        return randint(1,8) + dm
    if dice == 'D10':
        return randint(1,10) + dm
    if dice == '4D4':
        return randint(1,4) + randint(1,4) + randint(1,4) + randint(1,4) + dm
    print 'DICE ERROR! "%s" unknown.' % dice
    return 0
