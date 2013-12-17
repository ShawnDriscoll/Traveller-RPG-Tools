#   For Python 2.5.4
#
#   To use this function: from solomani_dna import check_dna
#
#   Perform racial Solomani DNA test for calling program
#
##########################################################

def check_dna(passing, TL, dice, soc, career, rank):
    "To use this check_dna function, add 'from solomani_dna import check_dna'"

    if passing == True and dice == 2:
        if TL <= 5:
            print 'Ancestry records show not true racial Solomani!'
        if TL == 6:
            print 'Blood test shows not true racial Solomani!'
        if TL >= 7:
            print 'DNA test shows not true racial Solomani!'
        soc = int(soc / 2.0 + 0.5)
        print 'Your SOC was reduced to', soc
        if career == 8:
            rank = 0
            print 'Your rank went back to', rank
        return [False, soc, rank]
    else:
        return [passing, soc, rank]
