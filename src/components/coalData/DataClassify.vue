<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>煤分类</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <pl-table @selection-change="handleSelectionChange" :row-style="tableRowClassName" ref='CoalTable' :data='coalList' big-data-checkbox highlight-current-row :row-height="40" use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :height="height" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
               <pl-table-column type="selection" width="55" align="center">
               </pl-table-column>
               <pl-table-column align="center" label='序号' width="80px" prop='id' key="1" ></pl-table-column>
                <pl-table-column align="center" label='煤样名称' prop='coal_name' key="2"></pl-table-column>
                <pl-table-column align="center" label='煤种' prop='coal_type' :key="Math.random()" ></pl-table-column> <!-- 加prop可以直接渲染值 -->
                <pl-table-column align="center" label='价格' key="5" prop='coal_price'></pl-table-column>
                <pl-table-column align="center" label='挥发分(Vdaf)' width="110px" prop='coal_vdaf' key="35"></pl-table-column>
                <pl-table-column align="center" label='氢(Hdaf)' width="110px" prop='coal_drynoash_hdaf' key="43"></pl-table-column>
                <pl-table-column align="center" label='粘结指数(G)' width="110px" prop='G' key="57"></pl-table-column>
                <pl-table-column align="center" label='Y' width="120px" prop='Y' key="60"></pl-table-column>
                <pl-table-column align="center" label='b/%' width="120px" prop='b'></pl-table-column>
            </pl-table>
            <p class='footnote'>*基于中国煤分类标准</p>
            <el-button class='Classifybutton' type="primary" @click="sendClassifyData">开始分类</el-button>
            <!-- 展示煤分类结果的对话框 -->
        </el-card>
        <el-dialog :lock-scroll='true' class='abow_dialog' top='7vh' title="煤分类结果" custom-class="userDig" center :show-close='true' :closeOnPressEscape='true' :close-on-click-modal="true" :visible.sync="editCoalDetailVisible" :append-to-body="true" width="75%" height='40%'>
            <pl-table :row-style="tableRowClassName" ref='CoalTable' :data='coalTypeList' big-data-checkbox highlight-current-row :row-height="33" use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :height="height" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
                <pl-table-column align="center" label='序号' prop='id' key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='煤样名称' prop='name' key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='预测煤类别' prop='predicted_type' key="Math.random()" ></pl-table-column>
            </pl-table>
            <span slot="footer" class='dialog-footer'>
                <el-button type="primary" @click="uoloadClassifyData"> 上传煤分类结果 </el-button>
                <el-button @click="editCoalDetailVisible = false"> 取消 </el-button>
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
      coalTypeList: [], // 存储煤分类结果
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
    sendClassifyData() {
      const result = this.$http.post('getClassifyeResult', this.multipleSelectionData)
      result.then(res => {
        this.editCoalDetailVisible = true // 展示煤分类结果的对话框
        this.coalTypeList = res.data
        console.log(this.coalTypeList)
      }
      )
    },
    uoloadClassifyData() {
      this.editCoalDetailVisible = false
      const result = this.$http.post('uploadClassifyeResult')
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
    border-width: 2px;
    padding:0;
    width: 97%;
    height: 88%;
}

.DataClassify{
    overflow-y:hidden; /*隐藏滚动条*/
    position: relative;
    height: 100%;
    width: 100%;
}
</style>
