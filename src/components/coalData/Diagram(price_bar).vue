<template>
  <div>
      <div class="echart" id="echart-bar_" :style="{position:'absolute',width: '52%', height: '100%', margin: 'auto', top: '3%', right: '-2%'}"></div>
  </div>
</template>

<script>

export default {
  methods: {
    initChart(Xlabel, Data) {
      console.log(Data)
      console.log(Xlabel)
      const getchart = this.$echarts.init(document.getElementById('echart-bar_'))
      var option = {
        tooltip: {
          trigger: 'axis',
          formatter: '{b} <br/> 价格: {c}'
        },
        xAxis: {
          show: true,
          type: 'category',
          data: Xlabel,
          axisLine: 'none',
          axisLabel: {
            fontSize: 12,
            interval: 0,
            rotate: 60
          },
          axisTick: { // x轴隐藏刻度
            show: false
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            textStyle: {
              fontSize: 12, // 字体大小
              fontWeight: 'bold'
            }
          }
        },
        title: {
          text: '煤样价格直方图(单位/元)',
          left: 'center',
          textStyle: {
            fontSize: 20,
            fontWeight: 'bold',
            color: '#455A64',
            textShadowBlur: 5
          }
        },
        series: [
          {
            name: 'name',
            type: 'bar',
            barWidth: 18,
            data: Data,
            itemStyle: {
              normal: {
                color: '#FF8357'
              }
            }
          }
        ]
      }
      getchart.setOption(option)
      window.addEventListener('resize', () => {
        getchart.resize()
      })
    }
  }
}
</script>

<style lang="less" scoped>
</style>
