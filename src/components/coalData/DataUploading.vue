<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right" >
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据上传与查看</el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 卡片视图区域 -->
        <el-card class="box-card">
            <!-- 搜索与添加区域 -->
            <el-row gutter="20"><!--分栏-->
                <el-col :span="7">
                    <div>
                        <input class='input_query' placeholder=" 请输入查找的煤种" v-model.lazy="queryInfo.query"> <!-- 用原始input+lazy属性不会造成卡顿 -->
                            <el-button class='query_button' slot="append" icon="el-icon-search" @click="getCoalList"></el-button>
                    </div>
                </el-col>
                <!-- 添加煤数据按钮 -->
                <el-col :span="2">
                    <el-button class='addButton' type="primary" @click='adddialogVisible=true'>添加煤数据</el-button>
                </el-col>
                <el-col :span="7" class='selectShow'> <!-- 记得注册组件 -->
                    <el-select class='select_show' collapse-tags v-model="chooseData" multiple placeholder="请选择" @change='selectAll'>
                        <el-option
                        v-for="item in selectOptions"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </el-col>
                <el-col :span="3" class='showName'><p class='showPra'>选择显示的参数:</p></el-col>
            </el-row>
            <!--煤数据列表区,header-cell-style修改列名表颜色-->
            <!-- 在table这增加 key！！十分重要，重新渲染该组件, -->
            <CoalDataShow ref='child1' :editCoalDetailVisible='editCoalDetailVisible' :show_1='show_1' :show_2='show_2' :show_3='show_3' :show_4='show_4' :show_5='show_5' :show_6='show_6' :show_7='show_7' :show_8='show_8' :show_9='show_9' :show_10='show_10' :show_11='show_11' :show_12='show_12' :show_13='show_13' :show_14='show_14' :show_15='show_15' :show_16='show_16' :show_17='show_17' :show_18='show_18' :queryInfo_get='queryInfo'></CoalDataShow>
        </el-card>
        <!-- 添加煤数据的对话框 -->
        <el-dialog
          title="煤数据导入"
          :visible.sync="adddialogVisible"
          width="100%"
          height='100%'
          :append-to-body="true"> <!-- 使对话框不会被蒙版遮住 -->
          <!-- 内容主体区 -->
          <el-button  @click="click_showCoalInformation" style="margin-left:10px">煤样基本信息</el-button>
          <el-button  @click="click_showOriginalCoalScreen">原始试验煤样筛分组成</el-button>
          <el-button  @click="click_showCrushCoalScreen">粉碎后筛分组成</el-button>
          <el-button  @click="click_showIndustrialCoal">煤样工业分析</el-button>
          <el-button  @click="click_showElementCoal">煤样元素分析</el-button>
          <el-button  @click="click_showGXYCoal">煤样粘结指数和胶质层指数</el-button>
          <el-button  @click="click_showInflationCoal">奥亚膨胀度</el-button>
          <el-button  @click="click_showFluidCoal">基氏流动度</el-button>
          <el-button  @click="click_showMeltCoal">煤灰熔点</el-button>
          <el-button  @click="click_showAshCoal">灰成分</el-button>
          <el-button  @click="click_showMicroCoal">煤样显微组分分析</el-button>
          <el-button  @click="click_showProcessCoal">炼焦过程参数</el-button>
          <el-button  @click="click_showTempCoal">炼焦温度参数</el-button>
          <el-button  @click="click_showIndustrialCoke">焦炭工业分析</el-button>
          <el-button  @click="click_showCokeScreen">焦炭筛分组成</el-button>
          <el-button  @click="click_showStrengthHot">机械强度与热性质</el-button>
          <el-button  @click="click_showMeltCoke">焦炭灰熔点</el-button>
          <el-button  @click="click_showReactCoke">煤焦反应性</el-button>
          <el-button  @click="click_showPoreCoke">气孔率</el-button>
          <p></p>
          <!-- 煤的基本信息 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showCoalInformation">
            <el-form-item label="煤样名称">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 原始试验煤样筛分组成 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showOriginalCoalScreen">
            <el-form-item label=">13mm">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 粉碎后筛分组成 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showCrushCoalScreen">
            <el-form-item label="粉碎后水分">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 煤样工业分析 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showIndustrialCoal">
            <el-form-item label="水分">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 煤样元素分析 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showElementCoal">
            <el-form-item label="氢(Had)">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 煤样粘结指数和胶质层指数 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showGXYCoal">
            <el-form-item label="粘结指数(G)">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 奥亚膨胀度 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showInflationCoal">
            <el-form-item label="T1/℃">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 基氏流动度 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showFluidCoal">
            <el-form-item label="Tp/℃">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 煤灰熔点 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showMeltCoal">
            <el-form-item label="变形温度(DT)">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 灰成分 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showAshCoal">
            <el-form-item label="SiO2">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 煤样显微组分分析 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showMicroCoal">
            <el-form-item label="镜质组(V)">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 炼焦过程参数 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showProcessCoal">
            <el-form-item label="炉型">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 炼焦温度参数 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showTempCoal">
            <el-form-item label="炼焦日期">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 焦炭工业分析 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showIndustrialCoke">
            <el-form-item label="水分(Mad)">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 焦炭筛分组成 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showCokeScreen">
            <el-form-item label=">80mm">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 机械强度与热性质 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showStrengthHot">
            <el-form-item label="M40">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 焦炭灰熔点 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showMeltCoke">
            <el-form-item label="变形温度(DT)">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 煤焦反应性 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showReactCoke">
            <el-form-item label="750">
              <el-input></el-input>
            </el-form-item>
          </el-form>
          <!-- 气孔率 -->
          <el-form ref="addform" :model="addform" label-width="80px" v-if="showPoreCoke">
            <el-form-item label="显气孔率">
              <el-input></el-input>
            </el-form-item>
          </el-form>
        </el-dialog>
    </div>
</template>

<script>
import CoalDataShow from './CoalDataShow' // 引入组件
export default {
  components: { // 引入组件
    CoalDataShow
  },
  data() {
    return {
      // 获取煤数据参数对象
      queryInfo: {
        query: ''
      },
      coalList: [],
      height: 250,
      selectOptions: [{
        value: 'ALL_SELECT',
        label: '选中所有'
      }, {
        value: '选项1',
        label: '原始试验煤样筛分组成'
      }, {
        value: '选项2',
        label: '粉碎后筛分组成'
      }, {
        value: '选项3',
        label: '煤样工业分析'
      }, {
        value: '选项4',
        label: '煤样元素分析'
      }, {
        value: '选项5',
        label: '粘结指数与胶质层指数'
      }, {
        value: '选项6',
        label: '奥亚膨胀度'
      }, {
        value: '选项7',
        label: '基氏流动度'
      }, {
        value: '选项8',
        label: '煤灰熔点/℃'
      }, {
        value: '选项9',
        label: '灰成分'
      }, {
        value: '选项10',
        label: '煤样显微组分分析'
      }, {
        value: '选项11',
        label: '炼焦过程参数'
      }, {
        value: '选项12',
        label: '炼焦温度参数'
      }, {
        value: '选项13',
        label: '焦炭工业分析'
      }, {
        value: '选项14',
        label: '焦炭筛分组成'
      }, {
        value: '选项15',
        label: '焦炭机械强度与热性质'
      }, {
        value: '选项16',
        label: '焦炭灰熔点'
      }, {
        value: '选项17',
        label: '粉焦反应性'
      }, {
        value: '选项18',
        label: '气孔率'
      }],
      oldChooseData: [],
      chooseData: [],

      // 变量判断显示的列
      show_1: false,
      show_2: false,
      show_3: true,
      show_4: true,
      show_5: true,
      show_6: false,
      show_7: false,
      show_8: false,
      show_9: false,
      show_10: true, // 显微组分分析
      show_11: false,
      show_12: false,
      show_13: false,
      show_14: false,
      show_15: false,
      show_16: false,
      show_17: false,
      show_18: false,
      // 显示添加煤数据的对话框
      adddialogVisible: false,
      // 显示对话框展示的元素
      showCoalInformation: false,
      showOriginalCoalScreen: false,
      showCrushCoalScreen: false,
      showIndustrialCoal: false,
      showElementCoal: false,
      showGXYCoal: false,
      showInflationCoal: false,
      showFluidCoal: false,
      showMeltCoal: false,
      showAshCoal: false,
      showMicroCoal: false,
      showProcessCoal: false,
      showTempCoal: false,
      showIndustrialCoke: false,
      showCokeScreen: false,
      showStrengthHot: false,
      showMeltCoke: false,
      showReactCoke: false,
      showPoreCoke: false,

      editCoalDetailVisible: false
    }
  },
  created() {
    this.height = window.screen.height > 850 ? window.screen.height * 0.57 : window.screen.height * 0.45 // 设置表格在不同分辨率电脑的展示大小
    const allValues = this.selectOptions.map(item => {
      return item.value
    })
    console.log(allValues)
    var showDataFirst = []// 刚登陆进行默认展示的数据选项
    showDataFirst.push(allValues[3])
    showDataFirst.push(allValues[4])
    showDataFirst.push(allValues[5])
    showDataFirst.push(allValues[10])
    this.chooseData = showDataFirst // 记住2个都要赋值，才可以默认选中取消，否则需要点击2次
    this.oldChooseData = showDataFirst
  },
  methods: {
    getCoalList() {
      this.$refs.child1.getCoalList() // 调用子组件方法，按键索引指定数据
    },
    selectAll (val) {
      this.editCoalDetailVisible = false
      // 根据点击的值改变显示的列
      const allValues = this.selectOptions.map(item => {
        return item.value
      })

      // 用来储存上一次选择的值，可进行对比
      const oldVal = this.oldChooseData.length > 0 ? this.oldChooseData : []

      // 若选择全部
      if (val.includes('ALL_SELECT')) {
        this.chooseData = allValues
      }
      // 取消全部选中， 上次有， 当前没有， 表示取消全选
      if (oldVal.includes('ALL_SELECT') && !val.includes('ALL_SELECT')) {
        this.chooseData = []
      }
      // 点击非全部选中，需要排除全部选中 以及 当前点击的选项
      // 新老数据都有全部选中
      if (oldVal.includes('ALL_SELECT') && val.includes('ALL_SELECT')) {
        const index = val.indexOf('ALL_SELECT')
        val.splice(index, 1) // 排除全选选项
        this.chooseData = val
      }
      // 全选未选，但是其他选项都全部选上了，则全选选上
      if (!oldVal.includes('ALL_SELECT') && !val.includes('ALL_SELECT')) {
        if (val.length === allValues.length - 1) {
          this.chooseData = ['ALL_SELECT'].concat(val)
        }
      }
      // 储存当前选择的最后结果 作为下次的老数据
      this.oldChooseData = this.chooseData

      var result0 = val.includes('ALL_SELECT') // 记得是索引val 不是 chooseData

      var result1 = val.includes('选项1') // 记得是索引val 不是 chooseData
      if (result1) {
        this.show_1 = true
      } else {
        this.show_1 = false
      }

      var result2 = val.includes('选项2')
      if (result2 || result0) {
        this.show_2 = true
      } else {
        this.show_2 = false
      }

      var result3 = val.includes('选项3')
      if (result3 || result0) {
        this.show_3 = true
      } else {
        this.show_3 = false
      }

      var result4 = val.includes('选项4')
      if (result4 || result0) {
        this.show_4 = true
      } else {
        this.show_4 = false
      }

      var result5 = val.includes('选项5')
      if (result5 || result0) {
        this.show_5 = true
      } else {
        this.show_5 = false
      }

      var result6 = val.includes('选项6')
      if (result6 || result0) {
        this.show_6 = true
      } else {
        this.show_6 = false
      }

      var result7 = val.includes('选项7')
      if (result7 || result0) {
        this.show_7 = true
      } else {
        this.show_7 = false
      }

      var result8 = val.includes('选项8')
      if (result8 || result0) {
        this.show_8 = true
      } else {
        this.show_8 = false
      }

      var result9 = val.includes('选项9')
      if (result9 || result0) {
        this.show_9 = true
      } else {
        this.show_9 = false
      }

      var result10 = val.includes('选项10')
      if (result10 || result0) {
        this.show_10 = true
      } else {
        this.show_10 = false
      }

      var result11 = val.includes('选项11')
      if (result11 || result0) {
        this.show_11 = true
      } else {
        this.show_11 = false
      }

      var result12 = val.includes('选项12')
      if (result12 || result0) {
        this.show_12 = true
      } else {
        this.show_12 = false
      }

      var result13 = val.includes('选项13')
      if (result13 || result0) {
        this.show_13 = true
      } else {
        this.show_13 = false
      }

      var result14 = val.includes('选项14')
      if (result14 || result0) {
        this.show_14 = true
      } else {
        this.show_14 = false
      }

      var result15 = val.includes('选项15')
      if (result15 || result0) {
        this.show_15 = true
      } else {
        this.show_15 = false
      }

      var result16 = val.includes('选项16')
      if (result16 || result0) {
        this.show_16 = true
      } else {
        this.show_16 = false
      }

      var result17 = val.includes('选项17')
      if (result17 || result0) {
        this.show_17 = true
      } else {
        this.show_17 = false
      }

      var result18 = val.includes('选项18')
      if (result18 || result0) {
        this.show_18 = true
      } else {
        this.show_18 = false
      }
      if (this.chooseData.length === 0) { // 注意是chooseData而不是val输入值
        this.editCoalDetailVisible = false
        this.show_1 = false
        this.show_2 = false
        this.show_3 = false
        this.show_4 = false
        this.show_5 = false
        this.show_6 = false
        this.show_7 = false
        this.show_8 = false
        this.show_9 = false
        this.show_10 = false
        this.show_11 = false
        this.show_12 = false
        this.show_13 = false
        this.show_14 = false
        this.show_15 = false
        this.show_16 = false
        this.show_17 = false
        this.show_18 = false
      }
      if (this.chooseData.length === 19 && this.chooseData.includes('ALL_SELECT')) {
        this.editCoalDetailVisible = false
        this.show_1 = true
        this.show_2 = true
        this.show_3 = true
        this.show_4 = true
        this.show_5 = true
        this.show_6 = true
        this.show_7 = true
        this.show_8 = true
        this.show_9 = true
        this.show_10 = true
        this.show_11 = true
        this.show_12 = true
        this.show_13 = true
        this.show_14 = true
        this.show_15 = true
        this.show_16 = true
        this.show_17 = true
        this.show_18 = true
      }
    },
    reload() {
      this.$forceUpdate()
    },
    // 根据ID删除对应的用户信息
    removeCoalById(id) {
      this.$confirm('此操作将永久删除该条数据, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 显示对话框展示的元素
    click_showCoalInformation() {
      this.showCoalInformation = true
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showOriginalCoalScreen() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = true
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showCrushCoalScreen() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = true
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showIndustrialCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = true
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showElementCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = true
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showGXYCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = true
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showInflationCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = true
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showFluidCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = true
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showMeltCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = true
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showAshCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = true
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showMicroCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = true
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showProcessCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = true
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showTempCoal() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = true
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showIndustrialCoke() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = true
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showCokeScreen() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = true
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showStrengthHot() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = true
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showMeltCoke() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = true
      this.showReactCoke = false
      this.showPoreCoke = false
    },
    click_showReactCoke() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = true
      this.showPoreCoke = false
    },
    click_showPoreCoke() {
      this.showCoalInformation = false
      this.showOriginalCoalScreen = false
      this.showCrushCoalScreen = false
      this.showIndustrialCoal = false
      this.showElementCoal = false
      this.showGXYCoal = false
      this.showInflationCoal = false
      this.showFluidCoal = false
      this.showMeltCoal = false
      this.showAshCoal = false
      this.showMicroCoal = false
      this.showProcessCoal = false
      this.showTempCoal = false
      this.showIndustrialCoke = false
      this.showCokeScreen = false
      this.showStrengthHot = false
      this.showMeltCoke = false
      this.showReactCoke = false
      this.showPoreCoke = true
    }
  }
}
</script>

<style lang="less" scoped>

.el-breadcrumb  /deep/  .el-breadcrumb__inner {
    font-size: 15px;
    color: white;
}

.el-breadcrumb{
    padding-left: 20px;
    padding-top: 20px;
    margin-bottom: 18px;
}

.box-card{
    position: absolute;
    margin-left: 1.3%;
    margin-right: 20px;
    border-width: 2px;
    padding:0;
    width: 97%;
    height: 88%;
}

.pl-table{
    margin-top: 20px;
}

/* 解决fixed column下滚轮无法拖动问题 */
/deep/.pl-table--scrollable-x .pl-table__body-wrapper {
    z-index : 1;
}

.selectShow{
    float:right;
    margin-left: -5%;
    width: 260px
}

.showName{
  float: right;
  margin-right: 3.5%;
  font-family: 'Microsoft YaHei';
  text-align: center;
}

.showPra{
  margin-top:10px;
  color:gray;
  font-weight: bold;
}

.input_query{
  outline-style: none;
  border: 1.4px solid #4DA4FF;
  border-radius: 3px;
  padding: 11px 0px;
  width: 80%
}

.el-button{
  margin:3px;
}

.addButton{
  margin-top:0px;
  margin-right: 0px;
  margin-bottom: 0px;
  margin-left:-15%;
}

.query_button{
  margin:0px
}

.el-button span{
  margin:0px;
  padding:0
}

.DataClassify{
    overflow-y:hidden; /*隐藏滚动条*/
    position: relative;
    height: 100%;
    width: 100%;
}
</style>
