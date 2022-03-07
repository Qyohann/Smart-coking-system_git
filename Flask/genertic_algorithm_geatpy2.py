import numpy as np 
import geatpy as ea
from genertic_algorithm_geatpy1 import MyProblem

inputDim = 3
lb = [0 for i in range(inputDim)]
ub = [1 for i in range(inputDim)]
lbin = [1 for i in range(inputDim)]
ubin = [0 for i in range(inputDim)]
price = [960, 880, 840]
CRI_value = [37.3,54,28.4]
CSR_value = [39.5,21.6,49.1]
M10_value = [8.7,10.5,6.3]
M25_value = [90,87.7,92.7]
CRI_min = 30
CRI_max = 50
CSR_min = 30
CSR_max = 50
M10_min = 1
M10_max = 10
M25_min = 80
M25_max = 100

problem = MyProblem(inputDim,lb,ub,lbin,ubin,price,CRI_value,CSR_value,M10_value,M25_value,CRI_min,CRI_max,CSR_min,CSR_max,M10_min,M10_max,M25_min,M25_max) # 生成问题对象
Encoding = 'RI' # 编码方式
NIND = 100 # 种群规模
Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # 创建区域描述器
population = ea.Population(Encoding, Field, NIND) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
myAlgorithm = ea.soea_DE_rand_1_L_templet(problem, population) # 实例化一个算法模板对象
myAlgorithm.MAXGEN = 2000 # 最大进化代数
myAlgorithm.mutOper.F = 0.5 # 差分进化中的参数F
myAlgorithm.recOper.XOVR = 0.7 # 重组概率
myAlgorithm.drawing = 1 # 1表示画图，0表示不画图
[NDSet, population] = myAlgorithm.run() # 执行算法模板
population.save() # 把最后一代种群的信息保存到文件中
# 输出结果
print("----------optimization objective：cost price, constraint condition：1.CRI of blended coal: 40<CRI<45 2.CSR of blended coal 30<CSR<35---------------")
print("Name of coals for blending: 红果(960 yuan)，东源后所(880 yuan)，晋茂(840 yuan)")
print("Optimal ratio for coal blending：",NDSet.Phen)
print("Lowest cost price：",NDSet.ObjV)
print("CRI of blended coal：",NDSet.Phen[0][0]*37.3+NDSet.Phen[0][1]*54.0+NDSet.Phen[0][2]*28.4)
print("CSR of blended coal：",NDSet.Phen[0][0]*39.5+NDSet.Phen[0][1]*21.6+NDSet.Phen[0][2]*49.1)
print("Run time of algorithm:",myAlgorithm.passTime)