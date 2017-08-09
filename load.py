import numpy as np
from PIL import Image

import common

def loadData(typeName, partName):
    temp_y = [] 
    temp_x = []
    
    f = open(typeName + '.txt', 'r', encoding='utf8')
    for line in f:
        if partName == 'tone':
            output_size = len(common.tones)
            partIndex = 3
        if partName == 'head':
            output_size = len(common.heads)
            partIndex = 4
        if partName == 'tail':
            output_size = len(common.tails)
            partIndex = 5
        
        temp_y.append(int(line.split(',')[partIndex]))
        
        c = line.split(',')[0]
        im = Image.open('images\\' + c + '.png')
        imArray = np.mean([np.array(im)], 3).astype('float32')
        temp_x.append(imArray)
    
    x = np.array(temp_x)
#    y = np.eye(output_size)[temp_y].astype('int32')
    y = np.array(temp_y).astype('int32')
    
    return output_size, x, y

def loadInitialsFinals():
    f = open(common.ifPath, 'r', encoding='utf8')
    data = f.readlines()
    
    initials = data[0].strip().split(',')
    finals = data[1].strip().split(',')
    
    f.close()
    
    return initials, finals
    


#loadData('train', 'head')
loadInitialsFinals()