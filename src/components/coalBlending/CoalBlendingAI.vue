<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>配煤方案辅助决策</el-breadcrumb-item>
            <el-breadcrumb-item>人工智能算法</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <pl-table @selection-change="handleSelectionChange" :row-style="tableRowClassName" ref='CoalTable' :data='coalList' big-data-checkbox highlight-current-row :row-height="40" use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :height="height" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
                <pl-table-column type="selection" width="55" align="center"></pl-table-column>
                <pl-table-column align="center" label='序号' width="80px" prop='id' fixed ></pl-table-column>
                <pl-table-column align="center" label='煤样名称' width="140px" prop='coal_name' fixed></pl-table-column>
                <pl-table-column align="center" label='煤种' prop='coal_type' fixed></pl-table-column>
                <pl-table-column align="center" label='价格' key="5" prop='coal_price' fixed></pl-table-column>
                <pl-table-column align="center" label='水分(Mad)' width="110px" prop='coal_mad' ></pl-table-column>
                <pl-table-column align="center" label='灰分(Ad)' width="120px" prop='coal_ad' ></pl-table-column>
                <pl-table-column align="center" label='挥发分(Vdaf)' width="110px" prop='coal_vdaf' ></pl-table-column>
                <pl-table-column align="center" label='全硫(St,d)' width="110px" prop='coal_std' ></pl-table-column>
                <pl-table-column align="center" label='G' width="110px" prop='G' ></pl-table-column>
                <pl-table-column align="center" label='X' width="110px" prop='X' ></pl-table-column>
                <pl-table-column align="center" label='Y' width="110px" prop='Y' ></pl-table-column>
                <pl-table-column align="center" label='CRI' width="110px" prop='coke_CRI' ></pl-table-column>
                <pl-table-column align="center" label='CSR' width="110px" prop='coke_CSR' ></pl-table-column>
                <pl-table-column align="center" label='M10' width="110px" prop='coke_M10' ></pl-table-column>
                <pl-table-column align="center" label='M25' width="110px" prop='coke_M25' ></pl-table-column>
            </pl-table>
        <el-button class='Blendingbutton' type="primary" @click="sendBlendingData">配煤决策</el-button>
        </el-card>
        <!-- 待配合的单煤数据及其对应的配比 -->
        <el-dialog :lock-scroll='true' class='abow_dialog' top='7vh' title="配煤辅助决策(人工智能算法)" custom-class="userDig" center :show-close='false' :closeOnPressEscape='false' :close-on-click-modal="false" :visible.sync="editCoalDetailVisible" :append-to-body="true" width="75%" height='40%'>
            <el-form :model="modifyParametersForm">
                <el-row v-for='(item, index) in modifyParametersForm.params' label="煤样名称:" :key="item.key"> <!-- // for循环将选择的煤显示在对话框里 -->
                    <el-col span=6>
                      <el-form-item :label="`煤样名称：`">
                          <span style="font-weight:bold">{{item.paramName}}</span> <!-- {{}} 是v-text，操作纯文本 -->
                      </el-form-item>
                    </el-col>
                    <el-col span=6>
                      <el-form-item :label="`煤种类型：`">
                          <span style="font-weight:bold">{{item.paramType}}</span>
                      </el-form-item>
                    </el-col>
                    <el-col span=5>
                      <el-form-item :label="`价格：`">
                          <span style="font-weight:bold">{{item.paramPrice}}</span>
                      </el-form-item>
                    </el-col>
                    <el-col span=6>
                        配煤比：<el-input style="font-weight:bold; width:70px" v-model="coalRatio[index]"></el-input> %
                    </el-col>
                </el-row>
                <el-row>
                  <el-col span=5>
                      总配煤比：{{totalRatio}} %
                  </el-col>
                </el-row>
            </el-form>
            <span slot="footer" class='dialog-footer'>
                <el-button type="primary" @click="predictBlendCoal"> 混合煤性质预测 </el-button>
                <el-button type="primary" @click="predictBestRatio"> 最优配煤比预测 </el-button>
                <el-button @click="cancelDialog"> 取消 </el-button>
            </span>
        </el-dialog>
        <!-- 混合煤性质预测结果 -->
        <el-dialog :lock-scroll='true' class='abow_dialog' top='7vh' title="混合煤性质预测结果" custom-class="userDig" center :show-close='true' :closeOnPressEscape='true' :close-on-click-modal="true" :visible.sync="editBlendCoalVisible" :append-to-body="true" width="75%" height='40%'>
          <pl-table :data-changes-scroll-top='false' ref='CoalTable' big-data-checkbox highlight-current-row :row-height="33" :data = blendCoalProperty use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
            <pl-table-column align="center" label='混合煤性质' key="21">
              <pl-table-column align="center" label='水分' prop='blendCoal_mad' key="21"></pl-table-column>
              <pl-table-column align="center" label='灰分' prop='blendCoal_ad' key="21"></pl-table-column>
              <pl-table-column align="center" label='挥发分'  prop='blendCoal_vdaf' key="21"></pl-table-column>
              <pl-table-column align="center" label='粘结指数G'  prop='blendCoal_G' key="21"></pl-table-column>
              <pl-table-column align="center" label='X'  prop='blendCoal_X' key="21"></pl-table-column>
              <pl-table-column align="center" label='Y' prop='blendCoal_Y' key="21"></pl-table-column>
            </pl-table-column>
          </pl-table>
            <span slot="footer" class='dialog-footer'>
                <el-button type="primary"> 上传至数据库 </el-button>
                <el-button @click="editBlendCoalVisible = false"> 取消 </el-button>
            </span>
        </el-dialog>
        <!-- 最优配煤比推荐的界面 -->
        <el-dialog :lock-scroll='true' class='abow_dialog' top='7vh' title="最优配煤比预测" custom-class="userDig" center :show-close='true' :closeOnPressEscape='true' :close-on-click-modal="true" :visible.sync="editRatioCoalVisible" :append-to-body="true" width="75%" height='40%'>
        <el-form>
          <el-row>
            <el-col span=6>
              <el-form-item style="font-weight:bold" :label="`优化目标：`">
                  <span style="font-weight:normal">成本价格</span>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <p style="font-weight:bold">限制条件</p>
            <el-col span=10>
                CRI范围：最小值 <el-input style="font-weight:bold; width:60px" v-model="paraRange[0]"></el-input> ~~  最大值
                <el-input style="font-weight:bold; width:60px" v-model="paraRange[1]"></el-input>
            </el-col>
            <el-col span=10>
                CSR范围：最小值 <el-input style="font-weight:bold; width:60px" v-model="paraRange[2]"></el-input> ~~  最大值
                <el-input style="font-weight:bold; width:60px" v-model="paraRange[3]"></el-input>
            </el-col>
          </el-row>
          <p style="margin:30px"></p>
          <el-row>
            <el-col span=10>
                M10范围：最小值 <el-input style="font-weight:bold; width:60px" v-model="paraRange[4]"></el-input> ~~  最大值
                <el-input style="font-weight:bold; width:60px" v-model="paraRange[5]"></el-input>
            </el-col>
            <el-col span=10>
                M25范围：最小值 <el-input style="font-weight:bold; width:60px" v-model="paraRange[6]"></el-input> ~~  最大值
                <el-input style="font-weight:bold; width:60px" v-model="paraRange[7]"></el-input>
            </el-col>
          </el-row>
          <el-row>
            <p style="font-weight:bold">预测结果</p>
            <el-col span=10>
              <span style="font-weight:normal">最优成本价格：{{returnPrice}} 元</span>
            </el-col>
          </el-row>
          <el-row>
            <p> </p>
            <el-col span=16>
              <span style="font-weight:normal">最优配煤比：{{returnRatio}}</span>
            </el-col>
          </el-row>
          <el-row>
          </el-row>
          </el-form>
          <span slot="footer" class='dialog-footer'>
              <el-button type="primary" @click="predictRatio"> 开始预测 </el-button>
              <el-button @click="editRatioCoalVisible = false"> 取消 </el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
export default {
  created() {
    this.getCoalList()
    this.height = window.screen.height > 850 ? window.screen.height * 0.62 : window.screen.height * 0.481 // 设置表格在不同分辨率电脑的展示大小
  },
  data() {
    return {
      coalList: [],
      blendCoalProperty: [], // 存贮返回来的混合煤性质数据
      queryInfo_get: '',
      editCoalDetailVisible: false, // 控制显示单煤信息及配煤比的界面
      editBlendCoalVisible: false, // 控制显示配合煤性质预测的界面
      editRatioCoalVisible: false, // 控制最优配煤比推荐的界面
      multipleSelectionData: [], // 存储多选框选择的煤数据
      arr: 10,
      modifyParametersForm: {
        params: [
          {
            paramName: '',
            paramType: '',
            paramPrice: ''
          }
        ]
      },
      coalRatio: [], // 存储煤比例
      preparedTotalResult: [], // 发送给后端的所有待分析煤数据(混合煤性质预测)
      objective: '成本价格', // 优化目标
      paraRange: [], // 存储CRI、CSR、M10、M25的参数范围
      preparedDataforRatio: [], // 发送给后端的煤比例(最优配煤比推荐)
      returnRatio: '', // 返回的ratio
      returnPrice: '', // 返回的价格
      newRatio: [], // 存储预测的比例并替代旧的
      totalRatio: 0, // 总配煤比
      returnTotalRatio: 0, // 因为四舍五入，返回的比例可能不到100%或超过100%，需要修改
      max: 0 // 因为四舍五入，返回的比例可能不到100%或超过100%，需要修改
    }
  },
  watch: {
    multipleSelectionData (val) {
      this.arr = this.multipleSelectionData.length
    },
    preparedDataforRatio (val) {
      console.log(val)
    }
  },
  methods: {
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex % 2 === 0) {
        return 'background-color:#E8E8E8;'
      }
    },
    async getCoalList() {
      await this.$http.get('coalBlendingData').then(ret => {
        this.coalList = ret.data.msg
        this.coalList.reverse()
      }
      )
    },
    sendBlendingData() {
      this.modifyParametersForm = { params: [] }
      this.editCoalDetailVisible = true // 展示混煤选择的对话框
      for (var i = 0; i < this.multipleSelectionData.length; i++) { // for循环将选择的煤显示在对话框里
        this.modifyParametersForm.params.push({
          paramName: this.multipleSelectionData[i].coal_name,
          paramType: this.multipleSelectionData[i].coal_type,
          paramPrice: this.multipleSelectionData[i].coal_price
        })
      }
    },
    handleSelectionChange(val) { // 读取多选框选择的数据
      this.multipleSelectionData = val
    },
    predictBlendCoal() { // 发送待预测的不同煤数据，并得到预测好的混合煤性质数据
      this.totalRatio = 0
      if (this.coalRatio.length === 0) { // 如果不输入配煤比则报错
        this.$confirm('配煤比例总和须为100%', '提示', {
          confirmButtonText: '确定',
          type: 'warning',
          showCancelButton: false
        })
      } else { // 通过验证才显示数据窗口
        for (var j = 0; j < this.coalRatio.length; j++) {
          this.totalRatio += Number(this.coalRatio[j])
          console.log(this.totalRatio)
        }
        if (this.totalRatio === 100) { // 如果配煤比为100才传送数据并预测
          this.editBlendCoalVisible = true
          for (var i = 0; i < this.multipleSelectionData.length; i++) {
            this.preparedTotalResult.push({ id: this.multipleSelectionData[i].id, coalRatio: this.coalRatio[i], coal_mad: this.multipleSelectionData[i].coal_mad, coal_ad: this.multipleSelectionData[i].coal_ad, coal_vdaf: this.multipleSelectionData[i].coal_vdaf, coal_std: this.multipleSelectionData[i].coal_std, G: this.multipleSelectionData[i].G, X: this.multipleSelectionData[i].X, Y: this.multipleSelectionData[i].Y })
          }
          const result = this.$http.post('predictBlendCoalQuality', this.preparedTotalResult)
          result.then(res => {
            this.blendCoalProperty = res.data
            console.log(this.blendCoalProperty)
          }
          )
          this.preparedTotalResult = []
        } else { // 如果配煤比不为100则提示
          this.$confirm('配煤比例总和须为100%', '提示', {
            confirmButtonText: '确定',
            type: 'warning',
            showCancelButton: false
          })
        }
      }
    },
    cancelDialog() {
      this.editCoalDetailVisible = false
      this.coalRatio = []
      this.totalRatio = 0
    },
    predictBestRatio() { // 显示最优配煤比预测界面
      this.editRatioCoalVisible = true
    },
    predictRatio() { // 传递数据并运行配煤最优比遗传算法
      for (var i = 0; i < this.multipleSelectionData.length; i++) {
        this.preparedDataforRatio.push({ coal_price: this.multipleSelectionData[i].coal_price, coke_CSR: this.multipleSelectionData[i].coke_CSR, coke_CRI: this.multipleSelectionData[i].coke_CRI, coke_M10: this.multipleSelectionData[i].coke_M10, coke_M25: this.multipleSelectionData[i].coke_M25 })
      }
      this.newRatio = []
      this.preparedDataforRatio.push(this.paraRange)
      const result = this.$http.post('predictBestRatio', this.preparedDataforRatio)
      result.then(res => {
        if (res.data[0] === 'Error') {
          this.$confirm('未能从设定范围空间中寻找到最优配煤比，请重新设置或扩大参数范围', '提示', {
            confirmButtonText: '确定',
            type: 'warning',
            showCancelButton: false
          })
        } else {
          this.returnPrice = res.data['1'][0][0].toFixed(2) // 获取最低成本价格
          // --------------------因为四舍五入，返回的比例可能不到100%或超过100%，需要修改------------------
          this.returnTotalRatio = 0
          this.max = res.data['0'][0][0]
          for (var j = 0; j < this.multipleSelectionData.length; j++) {
            if (res.data['0'][0][j] > this.max) {
              this.max = j
            }
            this.returnTotalRatio += (res.data['0'][0][j] * 100)
          }
          console.log(this.returnTotalRatio)
          if (this.returnTotalRatio < 100) {
            res.data['0'][0][this.max] += (100 - this.returnTotalRatio)
          } else if (this.returnTotalRatio > 100) {
            res.data['0'][0][this.max] -= (this.returnTotalRatio - 100)
          }
          // -----------------------------------------------------------------------------------------
          for (var i = 0; i < this.multipleSelectionData.length; i++) {
            this.returnRatio += (res.data['0'][0][i] * 100).toFixed(2).toString()
            this.returnRatio += '%'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.returnRatio += '\xa0'
            this.newRatio.push((res.data['0'][0][i] * 100).toFixed(2))
          }
        }
      })
      this.preparedDataforRatio = []
      this.returnRatio = ''
      this.coalRatio = this.newRatio
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

.DataClassify{
    overflow-y:hidden; /*隐藏滚动条*/
    position: relative;
    height: 100%;
    width: 100%;
}

.box-card{
    position: absolute;
    margin-left: 1.3%;
    border-width: 2px;
    padding:0;
    width: 97%;
    height: 88%;
    overflow-y:auto;
}

.Blendingbutton{
    float: right;
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
