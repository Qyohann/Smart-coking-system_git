import pandas as pd
import sklearn

# Delete the outrange value.
# data: two variables DataFrame, x: x variable name, 
# y: y variable name, k: slope, c: constant value, r: half range value
def dataRebuild(data,k,c,r,i,aim): 
    x_value = data.iloc[:,i].values
    y_true = data.loc[:,aim].values
    for i in range(x_value.size):
        y_h = k*x_value[i]+c+r
        y_l = y_h-2*r
        if y_true[i] < y_l or y_true[i] > y_h:
            data = data.rename(index={i:'Delist'})
    return data

# Delist the abnormal value taht doesnt scattered in the normal range
def dataclean(data,aim,round=100,fit=0.7,size=0.9,printresult=False):
    for i in range(1,data.shape[1]-2): # data.shape[1]-2 is adjustable baed on the data's output
        process_data = pd.concat([data.iloc[:,i],data.loc[:,aim]],axis=1)
        process_data = process_data.dropna(axis=0,how='any')
        label = process_data.columns.values.tolist()
        x_label = label[0]
        y_label = label[1]
        k,c,r = ModelFit.rangefinder(
            process_data,
            ratio=fit,area=size,n=round,
            printstatus=printresult
            )
        if printresult is True:
            ModelFit.rangeprint(process_data,x_label,y_label,k,c,r)
        data = dataRebuild(data,k,c,r,i,aim)
    data = data.drop(index='Delist',axis=0)
    data = sklearn.utils.shuffle(data) # Shuffle the data
    return data