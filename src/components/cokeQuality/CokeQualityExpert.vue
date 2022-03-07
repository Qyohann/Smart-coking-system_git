<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>焦炭质量预测</el-breadcrumb-item>
            <el-breadcrumb-item>专家系统算法</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <pl-table @selection-change="handleSelectionChange" :row-style="tableRowClassName" ref='CoalTable' :data='coalList' big-data-checkbox highlight-current-row :row-height="40" use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :height="height" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
               <pl-table-column type="selection" width="55" align="center"></pl-table-column>
               <pl-table-column align="center" label='序号' width="80px" prop='id' key="1" fixed ></pl-table-column>
                <pl-table-column align="center" label='煤样名称' width="140px" prop='coal_name' key="2" fixed></pl-table-column>
                <pl-table-column align="center" label='煤种' prop='coal_type' key="3" fixed></pl-table-column> <!-- 加prop可以直接渲染值 -->
                <pl-table-column align="center" label='价格' key="5" prop='coal_price' fixed></pl-table-column>
                <pl-table-column align="center" label='焦炭质量真实值' prop='predicted_type' key="Math.random()" >
                    <pl-table-column align="center" label='CRI' prop='coke_CRI' key="Math.random()" width="105px"></pl-table-column>
                    <pl-table-column align="center" label='CSR' prop='coke_CSR' key="Math.random()" width="105px"></pl-table-column>
                    <pl-table-column align="center" label='M10' prop='coke_M10' key="Math.random()" width="105px"></pl-table-column>
                    <pl-table-column align="center" label='M25' prop='coke_M25' key="Math.random()" width="105px"></pl-table-column>
                </pl-table-column>
                <pl-table-column align="center" label='焦炭质量预测值(专家系统算法)' prop='predicted_type' key="Math.random()">
                    <pl-table-column align="center" label='CRI' prop='predicted_CRI_expert' key="Math.random()" width="105px"></pl-table-column>
                    <pl-table-column align="center" label='CSR' prop='predicted_CSR_expert' key="Math.random()" width="105px"></pl-table-column>
                    <pl-table-column align="center" label='M10' prop='predicted_M10_expert' key="Math.random()" width="105px"></pl-table-column>
                    <pl-table-column align="center" label='M25' prop='predicted_M25_expert' key="Math.random()" width="105px"></pl-table-column>
                </pl-table-column>
            </pl-table>
            <el-button class='Classifybutton' type="primary" @click="sendPredictedData">开始预测</el-button>
            <!-- 展示煤分类结果的对话框 -->
        </el-card>
        <el-dialog :lock-scroll='true' class='abow_dialog' top='7vh' title="焦炭质量预测结果(专家系统算法)" custom-class="userDig" center :show-close='true' :closeOnPressEscape='true' :close-on-click-modal="true" :visible.sync="editCoalDetailVisible" :append-to-body="true" width="75%" height='40%'>
            <pl-table :row-style="tableRowClassName" ref='CoalTable' :data='coalQualityList' big-data-checkbox highlight-current-row :row-height="33" use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :height="height" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
                <pl-table-column align="center" label='序号' prop='id' key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='煤样名称' prop='coal_name' key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='焦炭质量预测值' prop='predicted_type' key="Math.random()" >
                    <pl-table-column align="center" label='CRI' prop='CRI' key="Math.random()" ></pl-table-column>
                    <pl-table-column align="center" label='CSR' prop='CSR' key="Math.random()" ></pl-table-column>
                    <pl-table-column align="center" label='M10' prop='M10' key="Math.random()" ></pl-table-column>
                    <pl-table-column align="center" label='M25' prop='M25' key="Math.random()" ></pl-table-column>
                </pl-table-column>
            </pl-table>
            <span slot="footer" class='dialog-footer'>
                <el-button type="primary" @click="uploadQualityData"> 上传预测结果 </el-button>
                <el-button @click="editCoalDetailVisible = false"> 取消 </el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
export default {
  created() {
    this.getCoalList()
    this.height = window.screen.height > 850 ? window.screen.height * 0.62 : window.screen.height * 0.44 // 设置表格在不同分辨率电脑的展示大小
  },
  data() {
    return {
      coalList: [],
      coalQualityList: [], // 存储煤质量预测结果
      multipleSelectionData: [],
      editCoalDetailVisible: false
    }
  },
  methods: {
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex % 2 === 0) {
        return 'background-color:#E8E8E8;'
      }
    },
    async getCoalList() { // 不能和煤数据上传与查看共用一个接口
      await this.$http.get('getClassifyeData').then(ret => {
        this.coalList = ret.data.msg // 取具体的数值
        this.coalList.reverse()
        this.total = this.coalList.length
      }
      )
    },
    handleSelectionChange(val) {
      this.multipleSelectionData = val
    },
    sendPredictedData() { // 发送待预测的数据
      const result = this.$http.post('getCokeQualityfyeResultExpertSystem', this.multipleSelectionData)
      result.then(res => {
        this.editCoalDetailVisible = true // 展示煤分类结果的对话框
        this.coalQualityList = res.data
        console.log(this.coalQualityList)
      }
      )
    },
    uploadQualityData() {
      this.editCoalDetailVisible = false
      const result = this.$http.post('uploadQualityResultExpert')
      result.then(res => {
        if (result) {
          this.getCoalList()
        }
      }
      )
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

.Classifybutton{
    float: right;
    margin-top: 10px;
    margin-bottom: 10px;
}

.footnote{
    float: left;
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

.DataClassify{
    overflow-y:hidden; /*隐藏滚动条*/
}
</style>
