#
#   Human Name Generator for Traveller RPG
#
#   Written in Python 2.5.4
#
#####################################################

from random import randint

def name_generator():
    
    def pick_sound(s_type):
        if s_type == V:
            sound = v_sounds[randint(1, len(v_sounds)) - 1]
        if s_type == CV:
            sound = ic_sounds[randint(1, len(ic_sounds)) - 1] + v_sounds[randint(1, len(v_sounds)) - 1]
        if s_type == VC:
            sound = v_sounds[randint(1, len(v_sounds)) - 1] + fc_sounds[randint(1, len(fc_sounds)) - 1]
        if s_type == CVC:
            sound = ic_sounds[randint(1, len(ic_sounds)) - 1] + v_sounds[randint(1, len(v_sounds)) - 1] \
            + fc_sounds[randint(1, len(fc_sounds)) - 1]
        if s_type == CC:
            sound = mc_sounds[randint(1, len(mc_sounds)) - 1]
        return sound

    V   = 1
    CV  = 2
    VC  = 3
    CVC = 4
    CC  = 5
    
    ic_sound = ['b','bl','br','c','ch','chr','cl','cr','d','dr','f','fl','fr','g','gl',
                'gr','gw','h','j','k','kl','kr','l','m','n','p','ph','pl','pr','qu','qw',
                'r','s','sc','sch','sh','sl','sk','sm','st','str','sv','sw',
                't','th','tr','tw','v','w','wh','wr','x','z','zh','zw']
    ic_freq = [28,7,12,20,16,22,14,17,27,21,18,6,10,9,7,11,4,20,20,13,11,20,
               28,24,25,27,14,4,12,5,3,24,30,3,4,25,27,20,12,24,
               19,5,12,20,15,14,12,6,6,5,9,2,6,2,3]
    print len(ic_sound), len(ic_freq)
    total_freq = 0
    for n in range(len(ic_sound)):
        print ic_sound[n],ic_freq[n]
        total_freq += ic_freq[n]
    print total_freq
    print
    
    v_sound = ['a','ai','e','ea','au','ee','i','o','u']
    v_freq = [15,3,20,4,5,4,22,17,10]
    print len(v_sound), len(v_freq)
    total_freq = 0
    for n in range(len(v_sound)):
        print v_sound[n],v_freq[n]
        total_freq += v_freq[n]
    print total_freq
    print

    mc_sound = ['kk','lf','lg','ll','ls',
                'nn','ns','nst','pp','rr','ss','tt','zz']
    mc_freq = [3,11,18,30,22,30,18,16,6,10,7,4,1]
    print len(mc_sound), len(mc_freq)
    total_freq = 0
    for n in range(len(mc_sound)):
        print mc_sound[n],mc_freq[n]
        total_freq += mc_freq[n]
    print total_freq
    print

    fc_sound = ['bdi','ch','che','chi','chs','ck','ct','d','da',
                'dai','dal','day','dhal','di','dike','drick',
                'dro','dros','dy','f','ft','g','gal','gh','ghi',
                'ghin','ght','hai','hdi','hi','hn','hr','j','k',
                'ke','ko','l','le','lf','li','lla','lle','ller',
                'llie','llier','ll','lt','ltz','lly','lm','lmes','los','lrick','lynn',
                'm','man','mm','mma','mmer','mms','mmy','mon',
                'mrick','n','nas','ndal','ndel','ndi','ndie','ndle',
                'ndy','ne','nes','nez','ng','ni','nk','nn','nne',
                'nner','nnor','nnie','nnke','nny','nos','ns','nt',
                'nter','nuz','p','ph','pper','que','r','rc','rie','rk','rl','rlie','rly','rr','rrie','rt',
                'rx','ry','s','sen','sha','shi','ski','son','ss','ssex','ssus',
                'st','ster','t','th','ti','tros','tti','tts','tz','v','w','wdi',
                'x','xx','yy','z','za','ze','zo','zy','zyx','zz']
    fc_freq = [6,6,2,14,5,13,4,22,12,4,18,8,10,12,3,5,19,13,12,10,11,24,7,14,3,3,8,3,
               4,9,17,3,16,26,11,6,27,9,14,7,10,6,10,4,8,15,7,4,10,16,7,14,5,7,25,10,5,4,13,5,
               12,16,5,27,11,6,3,18,7,4,12,4,20,18,14,20,26,12,8,13,17,7,5,7,
               19,12,20,7,6,20,13,10,4,24,13,6,23,18,15,10,7,6,20,
               3,21,40,12,3,8,15,20,5,6,4,20,9,15,14,8,12,16,11,6,8,22,5,4,2,1,2,6,2,4,8,2,1]
    print len(fc_sound), len(fc_freq)
    total_freq = 0
    for n in range(len(fc_sound)):
        print fc_sound[n],fc_freq[n]
        total_freq += fc_freq[n]
    print total_freq
    print

    syllable_type = [V,V,V,V,V,V,V,V,VC,VC,VC,VC,CV,CV,CV,CV,
                     CVC,CVC,CVC,CVC,CVC,CVC,CC,CC]

    ic_sounds = []
    for i in range(len(ic_freq)):
        for j in range(ic_freq[i]):
            ic_sounds.append(ic_sound[i])

    v_sounds = []
    for i in range(len(v_freq)):
        for j in range(v_freq[i]):
            v_sounds.append(v_sound[i])

    mc_sounds = []
    for i in range(len(mc_freq)):
        for j in range(mc_freq[i]):
            mc_sounds.append(mc_sound[i])
    
    fc_sounds = []
    for i in range(len(fc_freq)):
        for j in range(fc_freq[i]):
            fc_sounds.append(fc_sound[i])

    males = 0
    females = 0

    for n in range(100):
    
        for i in range(2):
            proper = False
            while not(proper):
                temp = CC
                while temp == CC:
                    temp = syllable_type[randint(1, len(syllable_type)) - 1]
                word = pick_sound(temp)
                building = True
                while building:
                    syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                    while temp == CC and (syllable == CV or syllable == CVC or syllable == CC):
                        syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                    while temp == V and (syllable == V or syllable == VC):
                        syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                    while temp == CV and (syllable == V or syllable == VC):
                        syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                    while temp == VC and (syllable == CV or syllable == CVC or syllable == CC):
                        syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                    while temp == CVC and (syllable == CV or syllable == CVC or syllable == CC):
                        syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                    if temp == VC or temp == CVC:
                        building = False
                    else:
                        word += pick_sound(syllable)
                        temp = syllable
                        
                if len(word) > 2 and len(word) < 15 + i * 4:
                    proper = True

            word = chr(ord(word[0]) - 32) + word[1:len(word)]

            if i == 0:
                human_name = word + ' '
                if word[0] == 'A' \
                       or word[0] == 'E' \
                       or word[0] == 'I' \
                       or word[0] == 'U' \
                       or word[0] == 'Y' \
                       or word[len(word) - 1] == 'a' \
                       or word[len(word) - 3:len(word)] == 'nny' \
                       or word[len(word) - 2:len(word)] == 'ie' \
                       or word[len(word) - 1] == 'i' \
                       or word[len(word) - 3:len(word)] == 'del' \
                       or word[len(word) - 2:len(word)] == 'ly' \
                       or word[len(word) - 4:len(word)] == 'lynn' \
                       or word[len(word) - 2:len(word)] == 'le' \
                       or word[len(word) - 3:len(word)] == 'ndy' \
                       or word[0:2] == 'Gw' \
                       or word[0:2] == 'Qu':
                    sex = 'Female'
                    females += 1
                else:
                    sex = 'Male'
                    males += 1
            else:
                human_name += chr(randint(1,26) + 64) + '. ' + word
            
        print human_name, '(%s)' % sex


    print
    print '%d%s Males' % (males, '%')
    print '%d%s Females' % (females, '%')
    print
        

if __name__ == '__main__':
    name_generator()
