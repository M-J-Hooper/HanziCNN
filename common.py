import os

#all chars in pinyin which indicate one of the 4 tones
tones = []

tone = ['á', 'é', 'í', 'ó', 'ú', 'ǘ']
tones.append(tone)

tone = ['à', 'è', 'ì', 'ò', 'ù', 'ǜ']
tones.append(tone)

tone = ['ǎ', 'ě', 'ǐ', 'ǒ', 'ǔ', 'ǚ']
tones.append(tone)

tone = ['ā', 'ē', 'ī', 'ō', 'ū']
tones.append(tone)

#standard latin corresponding chars
latin = ['a', 'e', 'i', 'o', 'u', 'u']


#specify paths
originalPath = 'chars/original.txt'
trainPath = 'chars/train.txt'
testPath = 'chars/test.txt'
tempPath = 'chars/temp.txt'
ifPath = 'chars/if.txt'

#helper functions

def getInitialFinal(pinyin):
    initial = ''
    for c in pinyin:
        if c not in latin:
            initial += c
        else:
            break
    final = pinyin.replace(initial, '', 1)
    return initial, final

def startUp():
    f1 = open(trainPath, 'r', encoding='utf8')
    f2 = open(tempPath, 'w', encoding='utf8')
    return f1, f2

def cleanUp(f1, f2):
    f1.close()
    f2.close()
    
    os.remove(trainPath)
    os.rename(tempPath, trainPath)