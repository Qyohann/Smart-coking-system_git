import numpy as np
import geatpy as ea

class MyProblem(ea.Problem):
    def __init__(self,inputDim,lb,ub,lbin,ubin,price,CRI_range,CSR_range,M10_range,M25_range,CRI_min,CRI_max,CSR_min,CSR_max,M10_min,M10_max,M25_min,M25_max):
        name = 'MyProblem'
        M = 1 # 目标维数
        maxormins = [1]
        self.Dim = inputDim # 3
        varTypes = [0] * self.Dim
        lb = lb # 决策变量下界 [0,0,0]
        ub = ub # 决策变量上界 [1,1,1]
        lbin = lbin # 决策变量下边界（0表示不包含该变量的下边界，1表示包含） [0,0,0]
        ubin = ubin # 决策变量上边界（0表示不包含该变量的上边界，1表示包含） [0,0,0]
        ea.Problem.__init__(self, name, M, maxormins, self.Dim, varTypes, lb, ub, lbin, ubin)
        self.price = price
        self.CSR_range = CSR_range # 单煤的CRI, CSR, M10和M25的值
        self.CRI_range = CRI_range
        self.M10_range = M10_range
        self.M25_range = M25_range
        # 混合煤限制条件的范围
        self.CRI_min = CRI_min 
        self.CRI_max = CRI_max
        self.CSR_min = CSR_min
        self.CSR_max = CSR_max
        self.M10_min = M10_min
        self.M10_max = M10_max
        self.M25_min = M25_min
        self.M25_max = M25_max

    def aimFunc(self, pop):
        Vars = pop.Phen
        var_array = []
        for i in range(self.Dim):
            var_array.append(Vars[:,[i]])
        print(len(var_array)) 
        # x1 = Vars[:, [0]]
        # x2 = Vars[:, [1]]
        # x3 = Vars[:, [2]]
        pop.ObjV = 0
        for i in range(len(self.price)):
            pop.ObjV += self.price[i] * var_array[i] #pop.ObjV = 960*x1 + 880*x2 + 840*x3
        
        #比例式子
        proportion_formula_1 = 0
        for i in var_array:
            proportion_formula_1 += i
        proportion_formula_1 = np.abs(proportion_formula_1-1) # 所有比例和为1
        
        #CRI范围式子
        proportion_formula_2 = 0 #最小值
        proportion_formula_3 = 0 #最大值
        for i in range(len(var_array)):
            proportion_formula_2 += var_array[i] * self. CRI_range[i]
        proportion_formula_2 = -(proportion_formula_2-self.CRI_min)
        proportion_formula_3 = proportion_formula_2-self.CRI_max

        #CSR范围式子
        proportion_formula_4 = 0 #最小值
        proportion_formula_5 = 0 #最大值
        for i in range(len(var_array)):
            proportion_formula_4 += var_array[i] * self. CSR_range[i]
        proportion_formula_4 = -(proportion_formula_4-self.CSR_min)
        proportion_formula_5 = proportion_formula_4-self.CSR_max

        #M10范围式子     
        proportion_formula_6 = 0 #最小值
        proportion_formula_7 = 0 #最大值
        for i in range(len(var_array)):
            proportion_formula_6 += var_array[i] * self. M10_range[i]
        proportion_formula_6 = -(proportion_formula_6-self.M10_min)
        proportion_formula_7 = proportion_formula_6-self.M10_max

        #M25范围式子     
        proportion_formula_8 = 0 #最小值
        proportion_formula_9 = 0 #最大值
        for i in range(len(var_array)):
            proportion_formula_8 += var_array[i] * self. M25_range[i]
        proportion_formula_8 = -(proportion_formula_8-self.M25_min)
        proportion_formula_9 = proportion_formula_8-self.M25_max

        #约束条件汇总
        pop.CV = np.hstack([proportion_formula_1,proportion_formula_2,proportion_formula_3,proportion_formula_4,proportion_formula_5,proportion_formula_6,proportion_formula_7,proportion_formula_8,proportion_formula_9])
        # pop.CV = np.hstack([ np.abs(x1 + x2 + x3 - 1), 
        # 37.3*x1+54.0*x2+28.4*x3-45, -37.3*x1-54.0*x2-28.4*x3+40,
        # 39.5*x1+21.6*x2+49.1*x3-35,
        # -39.5*x1-21.6*x2-49.1*x3+30
        # ])