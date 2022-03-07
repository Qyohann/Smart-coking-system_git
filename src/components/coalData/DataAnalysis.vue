<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据处理</el-breadcrumb-item>
            <el-breadcrumb-item>煤数据统计分析</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
        <!-- 表格用来占位置 -->
          <ChartPie ref="chart_pie_one"/>
          <Chartbar ref="chart_bar_one"/>
        </el-card>
    </div>
</template>

<script>
import ChartPie from './Diagram(type_pie)'
import Chartbar from './Diagram(price_bar)'

export default {
  components: {
    ChartPie,
    Chartbar
  },
  data() {
    return {
      name: '张雪',
      arr1: [], // 用于展示pie数据
      arr2: [], // 用于展示bar数据
      arr2_name: [], // 用于展示bar xaix label
      coalList: [], // pie数据
      coalList_2: [], // bar数据
      numberCoalType: [] // 计数不同煤种类的个数
    }
  },
  mounted () {
  },
  created() {
    this.getCoalList()
    this.getCoalList2()
  },
  methods: {
    async getCoalList() {
      await this.$http.get('getFanData').then(ret => {
        this.coalList = ret.data.msg // 取具体的数值
        var obj = {}
        var k = 0
        for (var i = 0, len = this.coalList.length; i < len; i++) {
          k = this.coalList[i].coal_type
          if (obj[k]) {
            obj[k]++
          } else {
            obj[k] = 1
          }
        }
        for (var o in obj) {
          if (o !== '' && o !== 'null') { // 去除空值和未知煤名称
            this.arr1.push({ name: o, value: obj[o] }) // 位置不要搞乱
          }
        }
        const { name, arr1 } = this
        this.$refs.chart_pie_one.initChart(name, arr1)
      }
      )
    },
    async getCoalList2() { // 要分开渲染
      await this.$http.get('getPriceData').then(ret => {
        this.coalList_2 = ret.data.msg
        var obj2 = {}
        var k2 = 0
        for (var j = 0, len = this.coalList_2.length; j < len; j++) {
          k2 = this.coalList_2[j].coal_name
          obj2[k2] = this.coalList_2[j].coal_price
        }
        for (var o in obj2) {
          if (o !== '' && o !== 'null' && obj2[o] !== null) { // 去除空值和未知煤名称
            this.arr2.push({ name: o, value: obj2[o] }) // 位置不要搞乱
            this.arr2_name.push(o)
          }
        }
        const { arr2 } = this
        this.$refs.chart_bar_one.initChart(this.arr2_name, arr2)
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

.box-card{
    position: absolute;
    margin-left: 1.3%;
    border-width: 2px;
    padding:0;
    width: 97%;
    height: 88%;
}

</style>
