<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>配煤历史数据查看</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <pl-table
            :row-style="tableRowClassName"
            ref='CoalTable'
            :data='coalList'
            big-data-checkbox
            highlight-current-row
            :row-height="40"
            use-virtual
            border
            :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}"
            :height="height"
            :key='Math.random()'
            :default-sort="{prop: 'id', order: 'ascending'}"
            size='mini'
            :cell-style="{padding:'0px',fontSize: '14px'}"
            fixedColumnsRoll>
                <pl-table-column align="center" label='序号' prop='id' width="55px" fixed key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='成本价格' prop='price' width="90px" fixed key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='CRI' prop='predicted_CRI' width="90px" fixed key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='CSR' prop='predicted_CSR' width="90px" fixed key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='M10' prop='predicted_M10' width="90px" fixed key="Math.random()" ></pl-table-column>
                <pl-table-column align="center" label='M25' prop='predicted_M25' width="90px" fixed key="Math.random()" ></pl-table-column>
                <pl-table-column label='煤种名称及其预测配煤比'>
                <!-- <pl-table-column align="center" label='M40范围' prop='first_coal' key="Math.random()" ></pl-table-column> -->
                  <pl-table-column align="center" label='煤种1' prop='first_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种1比例' prop='first_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种2' prop='second_coal' width="110px"  key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种2比例' prop='second_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种3' prop='third_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种3比例' prop='third_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种4' prop='fourth_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种4比例' prop='fourth_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种5' prop='fifth_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种5比例' prop='fifth_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种6' prop='sixth_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种6比例' prop='sixth_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种7' prop='seventh_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种7比例' prop='seventh_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种8' prop='eighth_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种8比例' prop='eighth_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种9' prop='ninth_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种9比例' prop='ninth_ratio' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种10' prop='tenth_coal' width="110px" key="Math.random()" ></pl-table-column>
                  <pl-table-column align="center" label='煤种10比例' prop='tenth_ratio' width="110px" key="Math.random()" ></pl-table-column>
                </pl-table-column>
            </pl-table>
            <!-- 展示煤分类结果的对话框 -->
        </el-card>
    </div>
</template>

<script>
export default {
  created() {
    this.getCoalList()
    this.height = window.screen.height > 850 ? window.screen.height * 0.62 : window.screen.height * 0.43 // 设置表格在不同分辨率电脑的展示大小
  },
  data() {
    return {
      coalList: [],
      coalTypeList: [], // 存储煤分类结果
      editCoalDetailVisible: false
    }
  },
  methods: {
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex % 2 === 0) { // 隔行变色
        return 'background-color:#E8E8E8;'
      }
    },
    async getCoalList() { // 获取历史混煤数据库的数据，不能和煤数据上传与查看共用一个接口
      await this.$http.get('getcoalBlendData').then(ret => {
        this.coalList = ret.data.msg // 取具体的数值
        this.coalList.reverse()
        console.log(this.coalList)
        this.total = this.coalList.length
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
