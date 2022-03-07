import pandas as pd
import numpy as np

def coalcal(data,ab,twob):
    data = data.iloc[:,:].values
    ab = ab.iloc[:,:].values
    twob = twob.iloc[:,:].values
    data = (ab-data)/twob

    def coalbinary(data):
        rows,cols = data.shape
        coaltf = np.zeros((rows,cols))
        for i in range(rows):
            for j in range(cols):
                if data[i,j] >= 0 and data[i,j] < 1:
                    coaltf[i,j] = 1
        return coaltf
    
    data = coalbinary(data)
    return data

def coaltype(data,coaltype):
    m,_ = data.shape
    p_type = ([])
    for i in range(m):
        if (data[i,:] == 1).all():
            p_type = np.hstack((p_type,coaltype.iat[i,0]))

    if len(p_type) == 0:
        for i in range(m):
            if (data[i,:4] == 1).all():
                p_type = np.hstack((p_type,coaltype.iat[i,0]))

    if len(p_type) == 0:
        return False
    else:
        return p_type

def nanlocation(data1,data2,data3):

    def tf2zero(data):
        data = data.isna()
        data.replace({False:0,True:1},inplace=True)
        return data

    data = tf2zero(data1) + tf2zero(data2) + tf2zero(data3)
    return data

def nullreplace(data,nullmap):
    m,n = data.shape
    for i in range(m):
        for j in range(n):
            if nullmap.iat[i,j] != 0:
                data.iat[i,j] = 1
    return data

def coaltypefind(coal):
    coal = pd.read_csv(coal,usecols=['Vm','H','G','Y','b'],dtype=str)
    coal = pd.DataFrame(np.tile(coal.values,(27,1)),columns=['Vm','H','G','Y','b'])
    twob = pd.read_csv("D:/Documents_summary/Code/Web front-end/Vue project/Project1/vue_shop/Flask/2b.csv",usecols=['Vm','H','G','Y','b'],dtype=str)
    ab = pd.read_csv("D:/Documents_summary/Code/Web front-end/Vue project/Project1/vue_shop/Flask/a+b.csv",dtype=str)
    typename = ab.iloc[:,:1]
    ab = ab.iloc[:,1:]

    nullmap = nanlocation(coal,twob,ab)
    coal = nullreplace(coal,nullmap).astype('float')
    twob = nullreplace(twob,nullmap).astype('float')
    ab = nullreplace(ab,nullmap).astype('float')

    coal = coaltype(coalcal(coal,ab,twob),typename)
    return coal

#data = coaltypefind("./Sample.csv")
#print(data)