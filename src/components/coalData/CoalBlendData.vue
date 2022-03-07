<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>配煤历史数据查看</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <pl-table @selection-change="handleSelectionChange" :row-style="tableRowClassName" ref='CoalTable' :data='coalList' big-data-checkbox highlight-current-row :row-height="40" use-virtual border :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" :height="height" :key='Math.random()' :default-sort="{prop: 'id', order: 'ascending'}" size='mini' :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll>
            </pl-table>
            <!-- 展示煤分类结果的对话框 -->
        </el-card>
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
