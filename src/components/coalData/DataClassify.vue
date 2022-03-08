<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>煤分类</el-breadcrumb-item>
        </el-breadcrumb>
        <!--handleSelectionChange: 当选择项发生变化时会触发该事件,
        row-stype: 隔行变色，行样式，data:传入表格数据, row-height:行高,
        default-sort:表格序号的默认排列顺序,
        height:表格高度 -->
        <el-card class="box-card">
            <pl-table @selection-change="handleSelectionChange"
            :row-style="tableRowClassName"
            :data='coalList'
            big-data-checkbox
            highlight-current-row
            :row-height="40"
            use-virtual border
            :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}"
            :height="height" :key='Math.random()'
            :default-sort="{prop: 'id', order: 'ascending'}"
            size='mini'
            :cell-style="{padding:'0px',fontSize: '14px'}"
            fixedColumnsRoll>
                <pl-table-column type="selection" width="55" align="center"></pl-table-column> <!--第一列选择栏-->
                <pl-table-column align="center" label='序号' width="80px" prop='id' key="1" ></pl-table-column> <!--prop:传入的参数-->
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
        <!--lock-scroll:是否在 Dialog 出现时将 body 滚动锁定
        show-close:是否显示关闭按钮
        close-on-press-escape:是否可以通过按下 ESC 关闭 Dialog
        close-on-click-modal: 是否可以通过点击关闭 Dialog
        append-to-body: Dialog 自身是否插入至 body 元素上。嵌套的 Dialog 必须指定该属性并赋值为 true-->
        <el-dialog :lock-scroll='true'
        class='abow_dialog'
        top='7vh'
        title="煤分类结果"
        custom-class="userDig"
        center :show-close='true'
        :closeOnPressEscape='true'
        :close-on-click-modal="false"
        :visible.sync="editCoalDetailVisible"
        :append-to-body="true"
        width="75%" height='40%'
        destroy-on-close='true'>
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
  created() { // 在模板渲染成html前调用，通常初始化某些属性值
    this.getCoalList() // 获取煤数据
    this.height = window.screen.height > 850 ? window.screen.height * 0.62 : window.screen.height * 0.43 // 设置表格在不同分辨率电脑的展示大小
  },
  data() {
    return {
      coalList: [],
      coalTypeList: [], // 存储煤分类结果
      multipleSelectionData: [], // 存储多选选到的值
      editCoalDetailVisible: false
    }
  },
  methods: {
    tableRowClassName ({ row, rowIndex }) { // 隔行变色
      if (rowIndex % 2 === 0) {
        return 'background-color:#E8E8E8;'
      }
    },
    async getCoalList() { // 不能和煤数据上传与查看共用一个接口
      await this.$http.get('getClassifyeData').then(ret => { // 获得煤数据
        this.coalList = ret.data.msg // 取具体的数值
        this.coalList.reverse()
        this.total = this.coalList.length
      }
      )
    },
    handleSelectionChange(val) { // 获得多选选择到的值
      this.multipleSelectionData = val
    },
    sendClassifyData() { // 上传选择的煤数据至后台算法，并开始分类，得到结果
      const result = this.$http.post('getClassifyeResult', this.multipleSelectionData)
      result.then(res => {
        this.editCoalDetailVisible = true // 展示煤分类结果的对话框
        this.coalTypeList = res.data
        console.log(this.coalTypeList)
      }
      )
    },
    uoloadClassifyData() { // 将煤分类后的结果上传至数据库中
      this.editCoalDetailVisible = false
      const result = this.$http.post('uploadClassifyeResult')
      result.then(res => { // 上传煤分类数据后，直接刷新页面煤数据
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
