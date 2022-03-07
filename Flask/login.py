from flask import Flask,redirect,request,url_for
from flask_cors import CORS
from coalData import CoalDataGeneration,app,db
from flask import jsonify
import json
from typeClassfication import coaltypefind
import csv
import tensorflow as tf
from tensorflow import keras 
import numpy as np
import geatpy as ea
from genertic_algorithm_geatpy1 import MyProblem
import pandas as pd
from pandas.core.frame import DataFrame
from ModelPredict import modelpredict

model = keras.models.load_model('./Flask/model_weight/predict_model.h5') #相对于terminal的路径
model_expert = pd.read_pickle('./Flask/model_weight/Model_DIS_CSR.pkl') #专家系统预测焦炭质量

CORS(app, supports_credentials=True) #两个文件都最好跨域
CORS(app, resources={r'/*': {'origins': '*'}})

upload_classify = 0 #用于按钮点击上传煤分类

#登录界面
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.data   # POST用该方式
        print(user)
        return "success1"

#煤数据获取
@app.route('/coalData',methods=['POST','GET'])
def getData():
    query_pra = request.values.get('query')
    print(query_pra)
    if request.method == 'GET':
        if query_pra == '':
            CoalData = CoalDataGeneration.query.order_by(CoalDataGeneration.id.desc()).all()
            res = {
            "msg": CoalDataGeneration.response(None, CoalData=CoalData)
            }
            return jsonify(res)
        else:
            query_result = CoalDataGeneration.query.filter(CoalDataGeneration.coal_type == query_pra).all()
            print(query_result)
            res = {
            "msg": CoalDataGeneration.response(None, CoalData=query_result)
            }
            return jsonify(res)

#根据煤id查询煤细数据
@app.route('/coalDetailedData',methods=['POST','GET'])
def getDetailedData():
    query_id = request.values.get('0') # 0代表id对应的键值
    query_result = CoalDataGeneration.query.filter(CoalDataGeneration.id == query_id).all()
    res = {
    "msg": CoalDataGeneration.response(None, CoalData=query_result)
    }
    return jsonify(res)

#煤类别扇形图获取
@app.route('/getFanData',methods=['POST','GET'])
def getFanData():
    if request.method == 'GET':
        CoalData = CoalDataGeneration.query.order_by(CoalDataGeneration.id.desc()).all()
        res = {
        "msg": CoalDataGeneration.response_pie(None, CoalData=CoalData)
        }
        return jsonify(res)

#煤价格直方图获取
@app.route('/getPriceData',methods=['POST','GET'])
def getPriceData():
    if request.method == 'GET':
        CoalData = CoalDataGeneration.query.order_by(CoalDataGeneration.id.desc()).all()
        res = {
        "msg": CoalDataGeneration.response_bar(None, CoalData=CoalData)
        }
        return jsonify(res)

#煤分类数据获取以及焦炭待预测数据获取
@app.route('/getClassifyeData',methods=['POST','GET'])
def getClassifyeData():
    if request.method == 'GET':
        CoalData = CoalDataGeneration.query.order_by(CoalDataGeneration.id.desc()).all()
        res = {
        "msg": CoalDataGeneration.response(None, CoalData=CoalData)
        }
        return jsonify(res)

#准备分类的煤数据传递
@app.route('/getClassifyeResult',methods=['POST','GET'])
def getClassifyeResult():
    if request.method == 'POST':
        prepared_data = request.data   
        prepared_data = json.loads(prepared_data)
        classify_para = [] # 将单条的数据存储在数组里
        para_dict = {} # 读取的单条数据
        classified_result = {} # 预测的单挑数据
        response_result = [] # 将预测的数据存储在数组里
        for data in prepared_data:
            para_dict['id'] = data['id']
            para_dict['Vm'] = data['coal_vdaf']
            para_dict['H'] = data['coal_drynoash_hdaf']
            para_dict['G'] = data['G']
            para_dict['Y'] = data['Y']
            para_dict['b'] = data['b']
            classify_para.append(para_dict)
            headers = ['Type','Vm','H','G','Y','b'] # csv文件头
            #csv路径
            file_name='./Flask/Sample.csv' 
            row = []
            row.append('Test')
            row.append(para_dict['Vm'])
            row.append(para_dict['H'])
            row.append(para_dict['G'])
            row.append(para_dict['Y'])
            row.append(para_dict['b'])

            with open(file_name, 'w', newline = '') as f: # 将读取的煤数据写入csv文件中
                f_csv = csv.writer(f)
                f_csv.writerow(headers)
                f_csv.writerow(row)

            
            single_result = coaltypefind(file_name)
            
            classified_result['id'] = data['id']
            classified_result['name'] = data['coal_name']
            if single_result == False: # 处理False的情况
                classified_result['predicted_type'] = "判据不足"
            else:
                classified_result['predicted_type'] = single_result[0]
                    

            response_result.append(classified_result)
            global upload_classify
            upload_classify = response_result
            para_dict = {} # 要放末尾，不然会被覆盖
            classified_result = {} # 要放末尾，不然会被覆盖

        return jsonify(response_result)

#点击“上传煤分类结果按钮”上传结果至数据库
@app.route('/uploadClassifyeResult',methods=['POST','GET'])
def uploadClassifyeResult():
    if len(upload_classify) != 0:
        for i in upload_classify:
            print(i['predicted_type'])
            query_data = CoalDataGeneration.query.filter(CoalDataGeneration.id == i['id']).update({'coal_type':str(i['predicted_type'])})
            db.session.commit()
    return 'upload successfully'

#焦炭质量预测(AI模型)
@app.route('/getCokeQualityfyeResultAI',methods=['POST','GET'])
def getCokeQualityfyeResultAI():
    if request.method == 'POST':
        prepared_data = request.data   
        prepared_data = json.loads(prepared_data)
        np_predict_data = [] #存储被预测的数据

        for data in prepared_data:
            single_data = []
            single_data.append(data['coal_mad'])
            single_data.append(data['coal_ad'])
            single_data.append(data['coal_vdaf'])
            single_data.append(data['coal_std'])
            single_data.append(data['G'])
            single_data.append(data['X'])
            single_data.append(data['Y'])
            np_predict_data.append(single_data)
        x_max = np.array([12.024,21.660,39.800,4.410,103.000,41.000,31.000])
        x_min = np.array([0.68,7.03,21.36,0.15,56.46,16.00,11.63])
        np_predict_data = (np_predict_data - x_min)/(x_max - x_min)
        np_predict_data = np.array(np_predict_data)
        np_predict_data = model.predict(np_predict_data) #模型的预测结果
        np_predict_data = np_predict_data.astype(np.float64)
        np_predict_data = np.around(np_predict_data, decimals=2) #控制小数位数
        para_dict = {} # 读取的单条数据
        response_result = [] # 将预测的数据存储在数组里

        i = 0
        for single_predicted_data in np_predict_data:
            para_dict['id'] = prepared_data[i]['id']
            para_dict['coal_name'] = prepared_data[i]['coal_name']
            para_dict['M25'] = single_predicted_data[2]
            para_dict['M10'] = single_predicted_data[3]
            para_dict['CRI'] = single_predicted_data[4]
            para_dict['CSR'] = single_predicted_data[5]
            response_result.append(para_dict)
            para_dict = {}
            i+=1
            
        global upload_quality
        upload_quality = response_result
    return jsonify(response_result)

#焦炭质量预测(Expert system模型)
@app.route('/getCokeQualityfyeResultExpertSystem',methods=['POST','GET'])
def getCokeQualityfyeResultExpertSystem():
    if request.method == 'POST':
        prepared_data = request.data   
        prepared_data = json.loads(prepared_data)
        np_predict_data = [] #存储被预测的数据

        for data in prepared_data:
            single_data = []
            single_data.append(data['id'])
            single_data.append(data['coal_mad'])
            single_data.append(data['coal_ad'])
            single_data.append(data['coal_vdaf'])
            single_data.append(data['coal_std'])
            single_data.append(data['coal_drynoash_hdaf'])
            single_data.append(data['coal_drynoash_cdaf'])
            single_data.append(data['coal_drynoash_odaf'])
            single_data.append(data['Rmax'])
            single_data.append(np.nan)
            single_data.append(data['G'])
            single_data.append(data['X'])
            single_data.append(data['Y'])
            single_data.append(data['coal_name'])
            np_predict_data.append(single_data)
        data = DataFrame(np_predict_data)
        data = data.rename(columns={0:'Num',1:'Mt',2:'Ad',3:'Vdaf',4:'St,d',5:'Hdaf',6:'Cdaf',7:'Odaf',8:'Ro',9:'V9-V13',10:'G',11:'X',12:'Y'})
        data = data.iloc[:,0:12]
        dis_r = modelpredict(data,model_expert)
        dis_r = np.array(dis_r) #先将数据框转换为数组
        dis_r = dis_r.tolist()
        para_dict = {} # 读取的单条数据
        response_result = [] # 将预测的数据存储在数组里
        for single_predicted_data in range(len(dis_r)):
            para_dict['id'] = np_predict_data[single_predicted_data][0]
            para_dict['coal_name'] = np_predict_data[single_predicted_data][-1]
            para_dict['CSR'] = round(dis_r[single_predicted_data][0],2)
            response_result.append(para_dict)
            para_dict = {}       
        global upload_quality_expert
        upload_quality_expert = response_result
    return jsonify(response_result)

#点击“上传预测结果结果按钮”上传结果至数据库(AI算法)
@app.route('/uploadQualityResult',methods=['POST','GET'])
def uploadQualityResult():
    if len(upload_quality) != 0:
        for i in upload_quality:
            query_data = CoalDataGeneration.query.filter(CoalDataGeneration.id == i['id']).update({'predicted_CRI':str(i['CRI']),'predicted_CSR':str(i['CSR']),'predicted_M10':str(i['M10']),'predicted_M25':str(i['M25'])})
            db.session.commit()
    return 'upload successfully'

#点击“上传预测结果结果按钮”上传结果至数据库(专家系统算法)
@app.route('/uploadQualityResultExpert',methods=['POST','GET'])
def uploadQualityResultEexpert():
    if len(upload_quality_expert) != 0:
        for i in upload_quality_expert:
            print(i)
            query_data = CoalDataGeneration.query.filter(CoalDataGeneration.id == i['id']).update({'predicted_CSR_expert':str(i['CSR'])})
            db.session.commit()
    return 'upload successfully'

#配煤方案数据显示
@app.route('/coalBlendingData',methods=['POST','GET'])
def getBlendingData():
    if request.method == 'GET':
        CoalData = CoalDataGeneration.query.order_by(CoalDataGeneration.id.desc()).all()
        res = {
        "msg": CoalDataGeneration.response(None, CoalData=CoalData)
        }
        return jsonify(res)

#接收配煤数据和配煤比
@app.route('/predictBlendCoalQuality',methods=['POST','GET'])
def predictBlendCoal():
    if request.method == 'POST':
        prepared_data = request.data
        prepared_data = json.loads(prepared_data) #必须要加才能获得正常数组数据
        blendCoal_mad = 0
        blendCoal_ad = 0
        blendCoal_vdaf = 0
        blendCoal_std = 0
        blendCoal_G = 0
        blendCoal_X = 0
        blendCoal_Y = 0
        for i in prepared_data:
            ratio  = float(i['coalRatio'])/100
            print(ratio)
            blendCoal_mad += i['coal_mad']*ratio
            blendCoal_ad += i['coal_ad']*ratio
            blendCoal_vdaf += i['coal_vdaf']*ratio
            blendCoal_std += i['coal_std']*ratio
            blendCoal_G += i['G']*ratio
            blendCoal_X += i['X']*ratio
            blendCoal_Y += i['Y']*ratio
        blendCoal_mad = round(blendCoal_mad,2)
        blendCoal_ad = round(blendCoal_ad,2)
        blendCoal_vdaf = round(blendCoal_vdaf,2)
        blendCoal_std = round(blendCoal_std,2)
        blendCoal_G = round(blendCoal_G,2)
        blendCoal_X = round(blendCoal_X,2)
        blendCoal_Y = round(blendCoal_Y,2)
        return_result = [{"blendCoal_mad":blendCoal_mad,'blendCoal_ad':blendCoal_ad,'blendCoal_vdaf':blendCoal_vdaf,'blendCoal_std':blendCoal_std,'blendCoal_G':blendCoal_G,'blendCoal_X':blendCoal_X,'blendCoal_Y':blendCoal_Y}]
        return jsonify(return_result)

#最优配煤比预测
@app.route('/predictBestRatio',methods=['POST','GET'])
def predictBestRatio():
    if request.method == 'POST':
        prepared_data = request.data
        prepared_data = json.loads(prepared_data) #必须要加才能获得正常数组数据
        inputDim = len(prepared_data[:-1]) #输入维数，参数1
        print(inputDim)
        print(prepared_data)
        lb = [0 for i in range(inputDim)] #决策变量下界，参数2
        ub = [1 for i in range(inputDim)] #决策变量上界，参数3
        lbin = [1 for i in range(inputDim)] #决策变量下边界（0表示不包含该变量的下边界，1表示包含），参数4
        ubin = [0 for i in range(inputDim)] #决策变量上边界（0表示不包含该变量的下边界，1表示包含），参数5
        price_array = [] #存储价格的数组，参数6
        for i in prepared_data[:-1]:
            price_array.append(i['coal_price'])

        CRI_value = [] #单煤的CRI
        CSR_value = [] #单煤的CSR
        M10_value = [] #单煤的M10
        M25_value = [] #单煤的M25
        for i in prepared_data[:-1]:
            CRI_value.append(i['coke_CRI'])
            CSR_value.append(i['coke_CSR'])
            M10_value.append(i['coke_M10'])
            M25_value.append(i['coke_M25'])
        
        #限制条件的范围
        CRI_min = float(prepared_data[-1][0])
        CRI_max = float(prepared_data[-1][1])
        CSR_min = float(prepared_data[-1][2])
        CSR_max = float(prepared_data[-1][3])
        M10_min = float(prepared_data[-1][4])
        M10_max = float(prepared_data[-1][5])
        M25_min = float(prepared_data[-1][6])
        M25_max = float(prepared_data[-1][7])

        problem = MyProblem(inputDim,lb,ub,lbin,ubin,price_array,CRI_value,CSR_value,M10_value,M25_value,CRI_min,CRI_max,CSR_min,CSR_max,M10_min,M10_max,M25_min,M25_max) # 生成问题对象
        Encoding = 'RI' # 编码方式
        NIND = 100 # 种群规模
        Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # 创建区域描述器
        population = ea.Population(Encoding, Field, NIND) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
        myAlgorithm = ea.soea_DE_rand_1_L_templet(problem, population) # 实例化一个算法模板对象
        myAlgorithm.MAXGEN = 2000 # 最大进化代数
        myAlgorithm.mutOper.F = 0.5 # 差分进化中的参数F
        myAlgorithm.recOper.XOVR = 0.7 # 重组概率
        myAlgorithm.drawing = 0 # 1表示画图，0表示不画图
        [NDSet, population] = myAlgorithm.run() # 执行算法模板
        population.save() # 把最后一代种群的信息保存到文件中

        print("Optimal ratio for coal blending：",NDSet.Phen) # 返回一个np.array数组或是None
        print("Lowest cost price：",NDSet.ObjV)
        
        if type(NDSet.Phen) is np.ndarray: # 判断是否有值
            return_result = []
            return_result.append(NDSet.Phen.tolist()) #第一个最优配煤比
            return_result.append(NDSet.ObjV.tolist()) #第二个最低价格
        else:
            return_result = ['Error']
        return jsonify(return_result)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run('0.0.0.0', debug=False)