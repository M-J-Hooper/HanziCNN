import re
from random import randint
import os

import common
import load

#heads = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', '', 'y', 'w']
#tails = ['a', 'o', 'ai', 'ei', 'ao', 'an', 'en', 'ang', 'eng', 'i', 'ie', 'iao', 'ian', 'in', 'ing', 'u', 'ou', 'ia', 'e', 'iu', 'uo', 'ui', 'uan', 'un', 'ong', 'iang', 'ue', 'ua', 'uai', 'uang', 'iong', '', 'er', 'ung']


def formatPinyin():
    f1 = open('chars/original.txt', 'r', encoding='utf8')
    f2 = open('chars/train.txt', 'w', encoding='utf8')
    
    for line in f1:
        if len(line.split(',')[0]) == 1:
            f2.write(re.sub(r'\([^)]*\)', '', line).strip() + '\n')
        
    f1.close()
    f2.close()


def tabulateTones():
    f1, f2 = common.startUp()
    
    for line in f1:
        toneNum = 3
        pinyin = line.split(',')[1]
        pinyin = pinyin.replace('ü', 'u') #only non tone related special char
       
        for c in pinyin:
            for i in range(len(common.tones)):
                for j in range(len(common.tones[i])):
                    if c == common.tones[i][j]:
                        pinyin = pinyin.replace(c, common.latin[j])
                        toneNum = i
        
        f2.write(','.join([line.strip(), pinyin.strip(), str(toneNum)]) + '\n') 
    
    common.cleanUp(f1, f2)
    
    
def findInitialsFinals():
    initials = []
    finals = []
    f1 = open(common.trainPath, 'r', encoding='utf8')
    f2 = open(common.ifPath, 'w', encoding='utf8')
    
    for line in f1:
        pinyin = line.split(',')[2]
        initial, final = common.getInitialFinal(pinyin)
        
        if initial not in initials:
            initials.append(initial)
        if final not in finals:
            finals.append(final)
    
    f2.write(','.join(initials) + '\n')
    f2.write(','.join(finals) + '\n')
       
    f1.close()
    f2.close()
    
    
def tabulateInitialsFinals():
    f1, f2 = common.startUp()
    initials, finals = load.loadInitialsFinals()
    
    for line in f1:
        pinyin = line.split(',')[2]
        initial, final = common.getInitialFinal(pinyin)
        
        f2.write(','.join([line.strip(), str(initials.index(initial)), str(finals.index(final))]) + '\n') 
                    
    common.cleanUp(f1, f2)


def splitTrainTest():
    f1, f2 = common.startUp()
    f3 = open(common.testPath, 'w', encoding='utf8')
    
    trainNum = 8000
    
    test = []
    for line in f1:
        test.append(line)
    total = len(test)
                    
    while total - len(test) < trainNum:
        i = randint(0, len(test) - 1)
        f2.write(test[i])
        del test[i]
    
    for line in test:
        f3.write(line)
        
    common.cleanUp(f1, f2)
    f3.close()





formatPinyin()
tabulateTones()
findInitialsFinals()
tabulateInitialsFinals()
splitTrainTest()




    

        
        
    



