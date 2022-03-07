import numpy as np
import pandas as pd

def valuebycenter(center,edge,r):
    l_up = distancecal(center,edge[0,:]) # Feeding one center point and the up edge point
    l_low = distancecal(center,edge[1,:])
    value = 2*r*l_low/(l_up + l_low) + edge[1,1] # edge[1,1] provide the lowest value of Y
    return value

def distancecal(point1,point2):
    l = np.sqrt(np.power(point1[0]-point2[0],2)+np.power(point1[1]-point2[1],2)) # Calculate the distance from center point to the edge point
    return l

def centerresult(parameter,edge,r,x):
    record = pd.DataFrame(columns=['PreValue','Distance'])
    for m in range(parameter.shape[0]): # Parameter came from the model, and here is a bunch of same parameter in the model
        center = parameter.iloc[m,4:6].values # Extract the center point and processing it one by one
        edgepoint = edge.iloc[:,:].values # Extract the edge points (up point and low point, two points 2x and 2y)
        prevalue = valuebycenter(center,edgepoint,r) # Feeding one center point in, and two edge points and the range, provide the value by single center
        distance = np.abs(x-center[0]) # the distance of the center to the predict value (the X input parameter) give the weight to each center
        record.loc[m] = [prevalue,distance] # Record the value and distance
    return record # Return a [Value,distance] multiline matrix (Depends on how many centers for one parameter)

def votePre(input,reverse=True):
    sum = input.iloc[:,1].sum() # Get the sum of distance
    prevalue = 0
    if reverse is True:
        for i in range(input.shape[0]): # Calculate the weighted predict value line by line
            prevalue += input.iloc[i,0]*(1-input.iloc[i,1]/sum) # input.iloc[i,1]/sum means weight of the distance of the center, and the value high means far away from the predict value and should give lower impact by 1-input.iloc[i,1]/sum
        prevalue /= i # Get the average value of the prediction
    elif reverse is False:
        for i in range(input.shape[0]):
            prevalue += input.iloc[i,0]*input.iloc[i,1]/sum # the higher K means higher influence, and should give more weight
    return prevalue

def singlepred(data,model):
    varlist = data.index.values.tolist()
    record = pd.DataFrame(columns=['PreValue','k'])
    for i in range(data.shape[0]):
        p = model.loc[varlist[i],:] # p for parameters
        if p is not None: # for one parameter
            k = p.iloc[0,1]
            c = p.iloc[0,2]
            r = p.iloc[0,3]
            x = data.iloc[i]
            y_up = k*x + c + r
            y_low = y_up - 2*r
            edge = pd.DataFrame(columns=['x','y'])
            edge.loc['up'] = [x,y_up]
            edge.loc['low'] = [x,y_low]
            singleresult = centerresult(p,edge,r,x)
            preValue = votePre(singleresult)
            record.loc[i] = [preValue,np.abs(k)] # Record the value of each parameter and the abs.K for them to evaluate the influence
    output = votePre(record,reverse=False)
    k = model.iloc[0,6]
    c = model.iloc[0,7] 
    #output = (output-c)/k
    output = output*k + c
    return output

def modelpredict(input,model):
    predict = pd.DataFrame(columns=['Prediction'])
    indexlist = input.index.tolist()
    for i in range(0,input.shape[0]):
        parameter = input.iloc[i,1:]
        parameter = parameter.dropna(axis=0,how='any')
        prevalue = singlepred(parameter,model)
        predict.loc[indexlist[i]] = [prevalue]
    return predict