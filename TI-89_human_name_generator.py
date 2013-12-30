#
#   Human Name Generator for Traveller RPG (abridged version)
#
#   Written in Python 2.5.4 for later conversion to C99 for TI-89
#
##################################################################

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
    
    ic_sound = ["b","bl","br","c","ch","cl","cr","d","dr","f","fl","fr","g","gl",
                "gr","h","j","k","kl","l","m","n","p","ph","pl","pr","qu",
                "r","s","sc","sh","sl","sk","st","sv",
                "t","th","tr","tw","v","w","wr","x","z","zh"]
    ic_freq = [10,3,5,7,6,5,6,10,8,7,3,4,4,3,4,7,7,5,4,10,9,9,10,5,
               2,5,2,9,11,2,9,10,7,9,2,7,6,5,5,3,3,4,1,3,1]
    print len(ic_sound), len(ic_freq)
    total_freq = 0
    for n in range(len(ic_sound)):
        print ic_sound[n],ic_freq[n]
        total_freq += ic_freq[n]
    print total_freq
    print
    
    v_sound = ["a","ai","e","ea","au","i","o","u"]
    v_freq = [6,2,7,2,2,8,6,4]
    print len(v_sound), len(v_freq)
    total_freq = 0
    for n in range(len(v_sound)):
        print v_sound[n],v_freq[n]
        total_freq += v_freq[n]
    print total_freq
    print

    mc_sound = ["kk","lf","lg","ll","ls","nn","ns","pp","rr","ss","tt","zz"]
    mc_freq = [2,4,7,11,8,11,7,3,4,3,2,1]
    print len(mc_sound), len(mc_freq)
    total_freq = 0
    for n in range(len(mc_sound)):
        print mc_sound[n],mc_freq[n]
        total_freq += mc_freq[n]
    print total_freq
    print

    fc_sound = ["bdi","ch","che","chi","chs","ck","ct","d","da",
                "dai","dal","day","di",
                "dro","dy","f","ft","g","gal","gh","ghi",
                "ght","hai","hdi","hi","hn","hr","j","k",
                "ke","ko","l","le","lf","li","lla","lle",
                "ll","lt","ltz","lly","lm","los",
                "m","man","mm","mma","mms","mmy","mon",
                "n","nas","ndi",
                "ndy","ne","nes","nez","ng","ni","nk","nn","nne",
                "nny","nos","ns","nt",
                "nuz","p","ph","que","r","rc","rie","rk","rl",
                "rly","rr","rt",
                "rx","ry","s","sen","sha","shi","ski","son","ss",
                "st","t","th","ti","tti","tts","tz","v","w","wdi",
                "x","xx","yy","z","za","ze","zo","zy","zyx","zz"]
    fc_freq = [3,3,1,5,2,5,2,8,5,2,7,3,5,7,5,4,4,9,3,5,2,3,2,2,4,
               6,2,6,9,4,3,10,4,5,3,4,3,6,3,2,4,6,5,9,4,2,2,2,5,6,
               10,4,7,5,2,7,7,5,7,9,5,3,3,7,5,7,3,7,5,2,9,5,3,8,7,
               4,3,7,2,8,14,5,2,3,6,7,2,7,6,5,3,6,4,3,3,8,2,2,1,1,
               1,3,1,2,3,1,1]
    print len(fc_sound), len(fc_freq)
    total_freq = 0
    for n in range(len(fc_sound)):
        print fc_sound[n],fc_freq[n]
        total_freq += fc_freq[n]
    print total_freq
    print

    syllable_type = [V,V,V,V,V,VC,VC,CV,CV,CV,CV,
                     CVC,CVC,CVC,CC]

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
                        
                if len(word) > 2 and len(word) < 10 + i * 4:
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
