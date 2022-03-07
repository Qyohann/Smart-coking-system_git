import pandas as pd
data = pd.read_csv("CoalData_WWN.csv")
from ModelPredict import modelpredict
model = pd.read_pickle('./model_weight/Model_DIS_CSR.pkl')
dis_data = data.iloc[:,0:12]
print(dis_data)
dis_r = modelpredict(dis_data,model)
print (dis_r)