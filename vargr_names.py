#
#   Written in Python 2.5.4
#
#   By Shawn Driscoll
#   shawndriscoll@hotmail.com
#

from random import randint

v_sound = ['a','ae','e','i','o','oe','ou','u','ue']
v_freq = [5,4,2,1,4,2,2,3,3]

ic_sound = ['d','dh','dz','f','g','gh','gn','gv',
            'gz','k','kf','kh','kn','ks','l','ll','n',
            'ng','r','rr','s','t','th','ts','v','z']
ic_freq = [5,5,3,4,10,6,2,4,4,10,3,6,3,3,4,4,2,2,5,4,5,4,4,2,5,6]

fc_sound =['dh','dz','g','gh','ghz','gz','k','kh',
           'khs','ks','l','ll','n','ng','r','rr',
           'rrg','rrgh','rs','rz','s','th','ts','z']
fc_freq = [1,1,3,2,1,1,2,2,1,1,2,1,5,5,3,3,1,1,1,1,1,1,1,2]

syllable_type = [1,2,2,2,3,3,3,4,4,4]

#   V CV VC CVC

def pick_sound(s_type):
    if s_type == 1:
        sound = v_sounds[randint(1, len(v_sounds)) - 1]

    if s_type == 2:
        sound = ic_sounds[randint(1, len(ic_sounds)) - 1] + v_sounds[randint(1, len(v_sounds)) - 1]

    if s_type == 3:
        sound = v_sounds[randint(1, len(v_sounds)) - 1] + fc_sounds[randint(1, len(fc_sounds)) - 1]

    if s_type == 4:
        sound = ic_sounds[randint(1, len(ic_sounds)) - 1] + v_sounds[randint(1, len(v_sounds)) - 1] + fc_sounds[randint(1, len(fc_sounds)) - 1]
    
    return sound

##print len(v_sound), len(v_freq),
v_sounds = []
for i in range(len(v_freq)):
    for j in range(v_freq[i]):
        v_sounds.append(v_sound[i])
##print v_sounds, len(v_sounds)
##print
##print len(ic_sound), len(ic_freq),
ic_sounds = []
for i in range(len(ic_freq)):
    for j in range(ic_freq[i]):
        ic_sounds.append(ic_sound[i])
##print ic_sounds, len(ic_sounds)
##print
##print len(fc_sound), len(fc_freq),
fc_sounds = []
for i in range(len(fc_freq)):
    for j in range(fc_freq[i]):
        fc_sounds.append(fc_sound[i])
##print fc_sounds, len(fc_sounds)
##print

for names in range(20):
    
    vargr_name = ''

    for i in range(2):
        proper = False
        while not(proper):
            temp = syllable_type[randint(1, len(syllable_type)) - 1]
            word = pick_sound(temp)

            #print word, temp

            building = True
            while building:
                
                syllable = syllable_type[randint(1, len(syllable_type)) - 1]
                if (temp == 1 or temp == 2) and (syllable == 1 or syllable == 3):
                    building = False
            #        print syllable
                else:
                    word += pick_sound(syllable)
                    temp = syllable
            #        print word, temp

            if len(word) > 1 and len(word) < 11 + i * 2:
                proper = True

        word = chr(ord(word[0]) - 32) + word[1:len(word)]

        vargr_name += word + ' '

    print vargr_name


    
