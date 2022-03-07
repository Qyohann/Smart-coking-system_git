<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>煤化工国家标准</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <pl-table :row-style="tableRowClassName" ref='CoalTable' row-height="40" use-virtual border :data='tableData' :header-cell-style="{background:'white',color:'#494949',textAlign:'center', border:'1px solid #BFBFBF',fontSize: '14px'}" big-data-checkbox highlight-current-row :cell-style="{padding:'0px',fontSize: '14px'}" fixedColumnsRoll :height="height">
                <pl-table-column align="center" fixed label='序号' prop='id' key="1" width='100'></pl-table-column>
                <pl-table-column align="left" fixed label='文件名称' prop='name' key="1"></pl-table-column>
                <!-- 下载文件区 -->
                <pl-table-column
                fixed="right"
                label="操作"
                width="125"
                align='center'>
                <template slot-scope="scope">
                    <el-button type="text" size="small" @click="showStanard(scope.row.id)">查看文件</el-button>
                </template>
                </pl-table-column>
            </pl-table>
        </el-card>
        <el-dialog :lock-scroll="false" destroy-on-close='true' class='abow_dialog' top='7vh' center :close-on-click-modal="false" :visible.sync="editCoalDetailVisible" :append-to-body="true" width="75%" height='40%'>
          <el-button class='Exitbutton' plain icon="el-icon-arrow-left" @click="editCoalDetailVisible=false"></el-button>
          <img :src='document' style="width:100%">
        </el-dialog>
    </div>
</template>

<script>
export default {
  created() {
    this.height = window.screen.height > 850 ? window.screen.height * 0.657 : window.screen.height * 0.50 // 设置表格在不同分辨率电脑的展示大小
  },
  data() {
    return {
      tableData: [{
        id: 1,
        name: 'GBT 212-2008 煤的工业分析方法',
        position: require('../../assets/pdfimg/GBT212-2008煤的工业分析方法.png') // 用require可以实现
      }, {
        id: 2,
        name: 'GBT 479-2016 烟煤胶质层指数测定方法',
        position: require('../../assets/pdfimg/GBT479-2016烟煤胶质层指数测定方法.png')
      }, {
        id: 3,
        name: 'GBT 1341-2007 煤的格金低温干馏试验方法',
        position: require('../../assets/pdfimg/GBT1341-2007煤的格金低温干馏试验方法.png')
      }, {
        id: 4,
        name: 'GBT 1572-2018 煤的结渣性测定方法',
        position: require('../../assets/pdfimg/GBT1572-2018煤的结渣性测定方法.png')
      }, {
        id: 5,
        name: 'GBT 1996-2017 冶金焦炭',
        position: require('../../assets/pdfimg/GBT1996-2017 冶金焦炭.png')
      }, {
        id: 6,
        name: 'GBT 2565-2014 煤的可磨性指数测定方法 哈德格罗夫法',
        position: require('../../assets/pdfimg/GBT2565-2014煤的可磨性指数测定方法 哈德格罗夫法.png')
      }, {
        id: 7,
        name: 'GBT 3715-2007 煤质及煤分析有关术语标准',
        position: require('../../assets/pdfimg/GBT3715-2007煤质及煤分析有关术语标准.png')
      }, {
        id: 8,
        name: 'GBT 5447-2014 烟煤黏结指数测定方法',
        position: require('../../assets/pdfimg/GBT5447-2014烟煤黏结指数测定方法.png')
      }, {
        id: 9,
        name: 'GBT 5450-2014 烟煤奥阿膨胀计试验',
        position: require('../../assets/pdfimg/GBT5450-2014烟煤奥阿膨胀计试验.png')
      }, {
        id: 10,
        name: 'GBT 5751-2009 中国煤炭分类',
        position: require('../../assets/pdfimg/GBT5751-2009中国煤炭分类.png')
      }, {
        id: 11,
        name: 'GBT 6948-2008 煤的镜质体反射率显微镜测定方法',
        position: require('../../assets/pdfimg/GBT6948-2008煤的镜质体反射率显微镜测定方法.png')
      }, {
        id: 12,
        name: 'GBT 7186-2008 选煤术语',
        position: require('../../assets/pdfimg/GBT7186-2008 选煤术语.png')
      }, {
        id: 13,
        name: 'GBT 15224.1-2018 煤炭质量分级 第1部分：灰分',
        position: require('../../assets/pdfimg/GBT15224.1-2018煤炭质量分级 第1部分：灰分.png')
      }, {
        id: 14,
        name: 'GBT 15224.2-2010 煤炭质量分级 第2部分：硫分',
        position: require('../../assets/pdfimg/GBT15224.2-2010煤炭质量分级 第2部分：硫分.png')
      }, {
        id: 15,
        name: 'GBT 15224.3-2010 煤炭质量分级 第3部分：发热量',
        position: require('../../assets/pdfimg/GBT15224.3-2010煤炭质量分级 第3部分：发热量.png')
      }, {
        id: 16,
        name: 'GBT 15588-2013 烟煤显微组分分类',
        position: require('../../assets/pdfimg/GBT15588-2013烟煤显微组分分类.png')
      }, {
        id: 17,
        name: 'GBT 16417-2011 煤炭可选性评定方法',
        position: require('../../assets/pdfimg/GBT16417-2011煤炭可选性评定方法.png')
      }, {
        id: 18,
        name: 'GBT 17607-1998 中国煤层煤分类',
        position: require('../../assets/pdfimg/GBT17607-1998中国煤层煤分类.png')
      }, {
        id: 19,
        name: 'GBT 18023-2000 烟煤的宏观煤岩类型分类',
        position: require('../../assets/pdfimg/GBT18023-2000烟煤的宏观煤岩类型分类.png')
      }, {
        id: 20,
        name: 'GBT 16417-2011 煤炭可选性评定方法',
        position: require('../../assets/pdfimg/GBT16417-2011煤炭可选性评定方法.png')
      }, {
        id: 21,
        name: 'GBT 18510-2001 煤和焦炭试验可替代方法确认准则',
        position: require('../../assets/pdfimg/GBT18510-2001煤和焦炭试验可替代方法确认准则.png')
      }, {
        id: 22,
        name: 'GBT 31391-2015 煤的元素分析',
        position: require('../../assets/pdfimg/GBT31391-2015煤的元素分析.png')
      }, {
        id: 23,
        name: 'GBT 31428-2015 煤化工术语',
        position: require('../../assets/pdfimg/GBT31428-2015煤化工术语.png')
      }, {
        id: 24,
        name: 'GBT 33969-2017 高炉富氧喷煤技术规范',
        position: require('../../assets/pdfimg/GBT33969-2017高炉富氧喷煤技术规范.png')
      }
      ],
      url: '/GBT.pdf',
      editCoalDetailVisible: false,
      // 展示显示的煤标准文件
      document: ''
    }
  },
  methods: {
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex % 2 === 0) {
        return 'background-color:#E8E8E8;'
      }
    },
    // 展示在线预览pdf
    showStanard(id) {
      this.editCoalDetailVisible = true
      if (id === 1) {
        this.document = this.tableData[0].position
      } else if (id === 2) {
        this.document = this.tableData[1].position
      } else if (id === 3) {
        this.document = this.tableData[2].position
      } else if (id === 4) {
        this.document = this.tableData[3].position
      } else if (id === 5) {
        this.document = this.tableData[4].position
      } else if (id === 6) {
        this.document = this.tableData[5].position
      } else if (id === 7) {
        this.document = this.tableData[6].position
      } else if (id === 8) {
        this.document = this.tableData[7].position
      } else if (id === 9) {
        this.document = this.tableData[8].position
      } else if (id === 10) {
        this.document = this.tableData[9].position
      } else if (id === 11) {
        this.document = this.tableData[10].position
      } else if (id === 12) {
        this.document = this.tableData[11].position
      } else if (id === 13) {
        this.document = this.tableData[12].position
      } else if (id === 14) {
        this.document = this.tableData[13].position
      } else if (id === 15) {
        this.document = this.tableData[14].position
      } else if (id === 16) {
        this.document = this.tableData[15].position
      } else if (id === 17) {
        this.document = this.tableData[16].position
      } else if (id === 18) {
        this.document = this.tableData[17].position
      } else if (id === 19) {
        this.document = this.tableData[18].position
      } else if (id === 20) {
        this.document = this.tableData[19].position
      } else if (id === 21) {
        this.document = this.tableData[20].position
      } else if (id === 22) {
        this.document = this.tableData[21].position
      } else if (id === 23) {
        this.document = this.tableData[22].position
      } else if (id === 24) {
        this.document = this.tableData[23].position
      }
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
}

.Exitbutton{
  position:fixed;
  margin:auto;
  left:0;
  top:0;
  bottom:0;
  width: 2%;
  padding: 0;
  border-radius: 0;
  background-color: white;
  opacity: 0.70;
  border-color: none;
}

</style>
