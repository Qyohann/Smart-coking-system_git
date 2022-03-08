from flask_sqlalchemy import SQLAlchemy #Flask的SQL管理
from flask import Flask
from flask_cors import CORS #Flask跨域

app = Flask(__name__) #2个文件只要有一个app即可
app.config['JSON_AS_ASCII'] =False #使JSON输出中文时格式正确

CORS(app, supports_credentials=True) #跨域
CORS(app, resources={r'/*': {'origins': '*'}}) #跨域

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://qyh:qyh13860925333@127.0.0.1:3306/coaldata?charset=utf8' #访问数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True #Flask-SQLAlchemy 将会追踪对象的修改并且发送信号

db = SQLAlchemy(app,use_native_unicode='utf8') #定义数据库

#构建煤数据的表结构以及获取方法
class CoalDataGeneration(db.Model):
    __tablename__ = 'CoalData_table' #列表名
    id = db.Column(db.Integer, primary_key=True) #数据类型+是否是主键
    #煤基本索引信息
    coal_name = db.Column(db.String(64))
    coal_belong = db.Column(db.String(64))
    coal_type = db.Column(db.String(64))
    coal_price = db.Column(db.Integer)
    #原始试验煤样筛选组分
    ori_coal_13mm = db.Column(db.Float)
    ori_coal_13_10mm = db.Column(db.Float)  
    ori_coal_10_8mm = db.Column(db.Float)
    ori_coal_8_6mm = db.Column(db.Float)
    ori_coal_6_5mm = db.Column(db.Float)
    ori_coal_5_4mm = db.Column(db.Float)
    ori_coal_4_3mm = db.Column(db.Float)
    ori_coal_3_2mm = db.Column(db.Float)
    ori_coal_2_1mm = db.Column(db.Float)
    ori_coal_1_05mm = db.Column(db.Float)
    ori_coal_05mm = db.Column(db.Float)
    ori_coal_total = db.Column(db.Float)
    ori_coal_fineness = db.Column(db.Float)
    #粉碎后筛选组分
    sma_coal_moi = db.Column(db.Float)
    sma__coal_6mm = db.Column(db.Float)
    sma__coal_6_5mm = db.Column(db.Float)
    sma__coal_5_4mm = db.Column(db.Float)
    sma__coal_4_3mm = db.Column(db.Float)
    sma__coal_3_2mm = db.Column(db.Float)
    sma__coal_2_1mm = db.Column(db.Float)
    sma__coal_1_05mm = db.Column(db.Float)
    sma__coal_05mm = db.Column(db.Float)
    sma__coal_total = db.Column(db.Float)
    sma_coal_fineness = db.Column(db.Float)
    #煤样工业分析
    coal_mad = db.Column(db.Float)
    coal_ad = db.Column(db.Float)
    coal_vdaf = db.Column(db.Float)
    coal_fcd = db.Column(db.Float)
    coal_vd = db.Column(db.Float)
    coal_ada = db.Column(db.Float)
    coal_vad = db.Column(db.Float)
    coal_fcad = db.Column(db.Float)
    coal_std = db.Column(db.Float)
    #元素分析(分析基)
    coal_ana_had = db.Column(db.Float)
    coal_ana_cad = db.Column(db.Float)
    coal_ana_nad = db.Column(db.Float)
    coal_ana_oad = db.Column(db.Float)
    #元素分析(干基)
    coal_dry_hd = db.Column(db.Float)
    coal_dry_cd = db.Column(db.Float)
    coal_dry_nd = db.Column(db.Float)
    coal_dry_od = db.Column(db.Float)
    #元素分析(干燥无灰基)
    coal_drynoash_hdaf = db.Column(db.Float)
    coal_drynoash_cdaf = db.Column(db.Float)
    coal_drynoash_ndaf = db.Column(db.Float)
    coal_drynoash_odaf = db.Column(db.Float)
    #粘结指数
    G = db.Column(db.Float)
    #胶质层指数
    X = db.Column(db.Float)
    Y = db.Column(db.Float)
    #奥亚膨胀度
    T1 = db.Column(db.Float)
    T2 = db.Column(db.Float)
    T3 = db.Column(db.Float)
    a = db.Column(db.Float)
    b = db.Column(db.Float)
    #基氏流动度
    Tp = db.Column(db.Float)
    Tmax = db.Column(db.Float)
    Tk = db.Column(db.Float)
    amax = db.Column(db.Float)
    Tk_Tp = db.Column(db.Float)
    #煤灰熔点
    DT = db.Column(db.Float)
    ST = db.Column(db.Float)
    HT = db.Column(db.Float)
    FT = db.Column(db.Float)
    #灰成分
    SiO2 = db.Column(db.Float)
    Al2O3 = db.Column(db.Float)
    Fe2O3 = db.Column(db.Float)
    CaO = db.Column(db.Float)
    MgO = db.Column(db.Float)
    P2O5 = db.Column(db.Float)
    Na2O = db.Column(db.Float)
    K2O = db.Column(db.Float)
    TiO2 = db.Column(db.Float)
    SO3 = db.Column(db.Float)
    ash_total = db.Column(db.Float)
    #煤样显微组分分析
    V = db.Column(db.Float)
    I = db.Column(db.Float)
    E = db.Column(db.Float)
    M = db.Column(db.Float)
    live_idle_ratio = db.Column(db.Float)
    Rmax = db.Column(db.Float)
    micro_var = db.Column(db.Float)
    micro_type = db.Column(db.String(64))
    #炼焦过程参数
    oven_type = db.Column(db.String(64))
    coking_style = db.Column(db.String(64))
    dry_quality = db.Column(db.Float)
    heap_density = db.Column(db.Float)
    oven_moi = db.Column(db.Float)
    up_temper = db.Column(db.Float)
    down_number = db.Column(db.Integer)
    hot_coke_qulity = db.Column(db.Float)
    hot_ratio_coke = db.Column(db.Float)
    quench_coke_weight = db.Column(db.Float)
    coke_moi = db.Column(db.Float)
    ratio_coke = db.Column(db.Float)
    #炼焦温度参数
    coking_date = db.Column(db.String(64))
    coking_process_time = db.Column(db.String(64))
    coking_start_time = db.Column(db.String(64))
    center_100_time = db.Column(db.String(64))
    center_500_time = db.Column(db.String(64))
    center_900_time = db.Column(db.String(64))
    coking_end_time = db.Column(db.String(64))
    coking_end_temp = db.Column(db.String(64))
    #焦炭工业分析
    coke_mad = db.Column(db.Float)
    coke_ad = db.Column(db.Float)
    coke_vdaf = db.Column(db.Float)
    coke_fcd = db.Column(db.Float)
    coke_vd = db.Column(db.Float)
    coke_aad = db.Column(db.Float)
    coke_vad = db.Column(db.Float)
    coke_fcad = db.Column(db.Float)
    coke_std = db.Column(db.Float)
    #焦炭筛分组成
    coke_80mm = db.Column(db.Float)
    coke_80_60mm = db.Column(db.Float)
    coke_60_40mm = db.Column(db.Float)
    coke_40_25mm = db.Column(db.Float)
    coke_25_20mm = db.Column(db.Float)
    coke_20_10mm = db.Column(db.Float)
    coke_10mm = db.Column(db.Float)
    coke_5mm = db.Column(db.Float)
    coke_sum = db.Column(db.Float)
    coke_60mm = db.Column(db.Float)
    coke_fineness = db.Column(db.Float)
    #机械强度
    coke_M40 = db.Column(db.Float)
    coke_M25 = db.Column(db.Float)
    coke_M10 = db.Column(db.Float)
    #热性质
    coke_CRI = db.Column(db.Float)
    coke_CSR = db.Column(db.Float)
    #焦炭灰熔点
    coke_DT = db.Column(db.Float)
    coke_ST = db.Column(db.Float)
    coke_HT = db.Column(db.Float)
    coke_FT = db.Column(db.Float)
    #粉焦反应性
    coke_750 = db.Column(db.Float)
    coke_800 = db.Column(db.Float)
    coke_850 = db.Column(db.Float)
    coke_900 = db.Column(db.Float)
    coke_950 = db.Column(db.Float)
    coke_1000 = db.Column(db.Float)
    coke_1050 = db.Column(db.Float)
    coke_1100 = db.Column(db.Float)
    coke_1150 = db.Column(db.Float)
    coke_1200 = db.Column(db.Float)
    #气孔率
    coke_apparent_porosity = db.Column(db.Float)
    coke_real_density = db.Column(db.Float)
    coke_fake_density = db.Column(db.Float)
    coke_total_ratio = db.Column(db.Float)
    predicted_CRI = db.Column(db.Float)
    predicted_CSR = db.Column(db.Float)
    predicted_M10 = db.Column(db.Float)
    predicted_M25 = db.Column(db.Float)
    predicted_CRI_expert = db.Column(db.Float)
    predicted_CSR_expert = db.Column(db.Float)
    predicted_M10_expert = db.Column(db.Float)
    predicted_M25_expert = db.Column(db.Float)
    predicted_CRI_error = db.Column(db.Float)
    predicted_CSR_error = db.Column(db.Float)
    predicted_M10_error = db.Column(db.Float)
    predicted_M25_error = db.Column(db.Float)

    def response(self, CoalData=None):
        if not CoalData:
            return 'Error0101, the CoalData is None'
        res = []

        for item in CoalData:
            if item.predicted_CSR_expert and item.predicted_CSR: #专家系统和人工智能算法预测的焦炭质量误差
                predicted_CSR_error = round(abs(item.predicted_CSR_expert-item.predicted_CSR),2) #取小数
            else:
                predicted_CSR_error = ''
            res.append({
            #煤基本索引信息
            'id':item.id, 'coal_name': item.coal_name, 'coal_belong': item.coal_belong, 'coal_type': item.coal_type,
            'coal_price':item.coal_price, 
            #原始试验煤样筛选组分
            'ori_coal_13mm':item.ori_coal_13mm, 'ori_coal_13_10mm':item.ori_coal_13_10mm,
            'ori_coal_10_8mm':item.ori_coal_10_8mm,'ori_coal_8_6mm':item.ori_coal_8_6mm,'ori_coal_6_5mm':item.ori_coal_6_5mm,
            'ori_coal_5_4mm':item.ori_coal_5_4mm,'ori_coal_4_3mm':item.ori_coal_4_3mm,'ori_coal_3_2mm':item.ori_coal_3_2mm,
            'ori_coal_2_1mm':item.ori_coal_2_1mm,'ori_coal_1_05mm':item.ori_coal_1_05mm,'ori_coal_05mm':item.ori_coal_05mm,
            'ori_coal_total':item.ori_coal_total,'ori_coal_fineness':item.ori_coal_fineness,
            #粉碎后筛选组分
            'sma_coal_moi':item.sma_coal_moi,'sma__coal_6mm':item.sma__coal_6mm,'sma__coal_6_5mm':item.sma__coal_6_5mm,
            'sma__coal_5_4mm':item.sma__coal_5_4mm,'sma__coal_4_3mm':item.sma__coal_4_3mm,'sma__coal_3_2mm':item.sma__coal_3_2mm,
            'sma__coal_2_1mm':item.sma__coal_2_1mm,'sma__coal_1_05mm':item.sma__coal_1_05mm,'sma__coal_total':item.sma__coal_total,
            'sma_coal_fineness':item.sma_coal_fineness,
            #煤样工业分析
            'coal_mad':item.coal_mad,'coal_ad':item.coal_ad,'coal_vdaf':item.coal_vdaf,'coal_fcd':item.coal_fcd,
            'coal_vd':item.coal_vd,'coal_ada':item.coal_ada,'coal_vad':item.coal_vad,'coal_fcad':item.coal_fcad,
            'coal_std':item.coal_std,
            #元素分析(分析基)
            'coal_ana_had':item.coal_ana_had,'coal_ana_cad':item.coal_ana_cad,'coal_ana_nad':item.coal_ana_nad,
            'coal_ana_oad':item.coal_ana_oad,
            #元素分析(干基)
            'coal_dry_hd':item.coal_dry_hd,'coal_dry_cd':item.coal_dry_cd,'coal_dry_nd':item.coal_dry_nd,
            'coal_dry_od':item.coal_dry_od,
            #元素分析(干燥无灰基)
            'coal_drynoash_hdaf':item.coal_drynoash_hdaf,'coal_drynoash_cdaf':item.coal_drynoash_cdaf,'coal_drynoash_ndaf':item.coal_drynoash_ndaf,
            'coal_drynoash_odaf':item.coal_drynoash_odaf,
            #粘结指数
            'G':item.G,
            #胶质层指数
            'X':item.X,
            'Y':item.Y,
            #奥亚膨胀度
            'T1':item.T1,
            'T2':item.T2,
            'T3':item.T3,
            'a':item.a,
            'b':item.b,
            #基氏流动度
            'Tp':item.Tp,
            'Tmax':item.Tmax,
            'Tk':item.Tk,
            'amax':item.amax,
            'Tk_Tp':item.Tk_Tp,
             #煤灰熔点
            'DT':item.DT,
            'ST':item.ST,
            'HT':item.HT,
            'FT':item.FT,
            #灰成分
            'SiO2':item.SiO2,
            'Al2O3':item.Al2O3,
            'Fe2O3':item.Fe2O3,
            'CaO':item.CaO,
            'MgO':item.MgO,
            'P2O5':item.P2O5,
            'Na2O':item.Na2O,
            'K2O':item.K2O,
            'TiO2':item.TiO2,
            'SO3':item.SO3,
            'ash_total':item.ash_total,
            #煤样显微组分分析
            'V':item.V,
            'I':item.I,
            'E':item.E,
            'M':item.M,
            'live_idle_ratio':item.live_idle_ratio,
            'Rmax':item.Rmax,
            'micro_var':item.micro_var,
            'micro_type':item.micro_type,
            #炼焦过程参数
            'oven_type':item.oven_type,
            'coking_style':item.coking_style,
            'dry_quality':item.dry_quality,
            'heap_density':item.heap_density,
            'oven_moi':item.oven_moi,
            'up_temper':item.up_temper,
            'down_number':item.down_number,
            'hot_coke_qulity':item.hot_coke_qulity,
            'hot_ratio_coke':item.hot_ratio_coke,
            'quench_coke_weight':item.quench_coke_weight,
            'coke_moi':item.coke_moi,
            'ratio_coke':item.ratio_coke,
            #炼焦温度参数
            'coking_date':item.coking_date,
            'coking_process_time':item.coking_process_time,
            'coking_start_time':item.coking_start_time,
            'center_100_time':item.center_100_time,
            'center_500_time':item.center_500_time,
            'center_900_time':item.center_900_time,
            'coking_end_time':item.coking_end_time,
            'coking_end_temp':item.coking_end_temp,
            #焦炭工业分析
            'coke_mad':item.coke_mad,
            'coke_ad':item.coke_ad,
            'coke_vdaf':item.coke_vdaf,
            'coke_fcd':item.coke_fcd,
            'coke_vd':item.coke_vd,
            'coke_aad':item.coke_aad,
            'coke_vad':item.coke_vad,
            'coke_fcad':item.coke_fcad,
            'coke_std':item.coke_std,
            #焦炭筛分组成
            'coke_80mm':item.coke_80mm,
            'coke_80_60mm':item.coke_80_60mm,
            'coke_60_40mm':item.coke_60_40mm,
            'coke_40_25mm':item.coke_40_25mm,
            'coke_25_20mm':item.coke_25_20mm,
            'coke_20_10mm':item.coke_20_10mm,
            'coke_10mm':item.coke_10mm,
            'coke_5mm':item.coke_5mm,
            'coke_60mm':item.coke_60mm,
            'coke_fineness':item.coke_fineness,
            #机械强度
            'coke_M40':item.coke_M40,
            'coke_M25':item.coke_M25,
            'coke_M10':item.coke_M10,
            #热性质
            'coke_CRI':item.coke_CRI,
            'coke_CSR':item.coke_CSR,
            #焦炭灰熔点
            'coke_DT':item.coke_DT,
            'coke_ST':item.coke_ST,
            'coke_HT':item.coke_HT,
            'coke_FT':item.coke_FT,
            #粉焦反应性
            'coke_750':item.coke_750,
            'coke_800':item.coke_800,
            'coke_850':item.coke_850,
            'coke_900':item.coke_900,
            'coke_950':item.coke_950,
            'coke_1000':item.coke_1000,
            'coke_1050':item.coke_1050,
            'coke_1100':item.coke_1100,
            'coke_1150':item.coke_1150,
            'coke_1200':item.coke_1200,
            #气孔率
            'coke_apparent_porosity':item.coke_apparent_porosity,
            'coke_real_density':item.coke_real_density,
            'coke_fake_density':item.coke_fake_density,
            'coke_total_ratio':item.coke_total_ratio,
            #预测的焦炭质量参数
            'predicted_CRI':item.predicted_CRI,
            'predicted_CSR':item.predicted_CSR,
            'predicted_M10':item.predicted_M10,
            'predicted_M25':item.predicted_M25,
            'predicted_CRI_expert':item.predicted_CRI_expert,
            'predicted_CSR_expert':item.predicted_CSR_expert,
            'predicted_M10_expert':item.predicted_M10_expert,
            'predicted_M25_expert':item.predicted_M25_expert,
            'predicted_CRI_error':item.predicted_CRI_error,
            'predicted_CSR_error':predicted_CSR_error,
            'predicted_M10_error':item.predicted_CRI_error,
            'predicted_M25_error':item.predicted_CRI_error
            })
        return res

    def response_pie(self, CoalData=None):
        if not CoalData:
            return 'Error0101, the CoalData is None'
        res = []
        for item in CoalData:
            res.append({
            'coal_type': item.coal_type})
        return res
    
    def response_bar(self, CoalData=None):
        if not CoalData:
            return 'Error0101, the CoalData is None'
        res = []
        for item in CoalData:
            res.append({
            'coal_name': item.coal_name,
            'coal_price': item.coal_price})
        return res

# 构建blendcoal表数据，存储配煤的方案
class BlendCoalDataStoringGeneration(db.Model):
    __tablename__ = 'blendcoaldata_table' #列表名
    id = db.Column(db.Integer, primary_key=True) #数据类型+是否是主键
    #煤基本索引信息
    first_coal = db.Column(db.String(64))
    first_ratio = db.Column(db.Float)
    second_coal = db.Column(db.String(64))
    second_ratio = db.Column(db.Float)
    third_coal = db.Column(db.String(64))
    third_ratio = db.Column(db.Float)
    fourth_coal = db.Column(db.String(64))
    fourth_ratio = db.Column(db.Float)
    fifth_coal = db.Column(db.String(64))
    fifth_ratio = db.Column(db.Float)
    sixth_coal = db.Column(db.String(64))
    sixth_ratio = db.Column(db.Float)
    seventh_coal = db.Column(db.String(64))
    seventh_ratio = db.Column(db.Float)
    eighth_coal = db.Column(db.String(64))
    eighth_ratio = db.Column(db.Float)
    ninth_coal = db.Column(db.String(64))
    ninth_ratio = db.Column(db.Float)
    tenth_coal = db.Column(db.String(64))
    tenth_ratio = db.Column(db.Float)
    predicted_CRI = db.Column(db.String(64))
    predicted_CSR = db.Column(db.String(64))
    predicted_M10 = db.Column(db.String(64))
    predicted_M25 = db.Column(db.String(64))
    predicted_M40 = db.Column(db.String(64))
    price = db.Column(db.Float)

    def response(self, CoalData=None):
        if not CoalData:
            return 'Error0101, the BlendCoalData is None'
        res = []   
        for item in CoalData:
            res.append({
                'id':item.id,
                'first_coal':item.first_coal,'first_ratio':item.first_ratio,
                'second_coal':item.second_coal,'second_ratio':item.second_ratio,
                'third_coal':item.third_coal,'third_ratio':item.third_ratio,
                'fourth_coal':item.fourth_coal,'fourth_ratio':item.fourth_ratio,
                'fifth_coal':item.fourth_coal,'fifth_ratio':item.fourth_ratio,
                'sixth_coal':item.fourth_coal,'sixth_ratio':item.fourth_ratio,
                'seventh_coal':item.fourth_coal,'seventh_ratio':item.fourth_ratio,
                'eighth_coal':item.fourth_coal,'eighth_ratio':item.fourth_ratio,
                'ninth_coal':item.fourth_coal,'ninth_ratio':item.fourth_ratio,
                'tenth_coal':item.fourth_coal,'tenth_ratio':item.fourth_ratio,
                'predicted_CRI':item.predicted_CRI,'predicted_CSR':item.predicted_CSR,
                'predicted_M10':item.predicted_M10,'predicted_M25':item.predicted_M25,
                'predicted_M40':item.predicted_M40,
                'price':item.price
            })
        return res
#if __name__ == '__main__':     
    #db.create_all() 
    #不执行，不然会重新创建表格