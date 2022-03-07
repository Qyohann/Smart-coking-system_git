<template>
  <div>
      <div class="echart" id="echart-pie" :style="{position:'absolute',width: '105%', height: '105%', margin: 'auto', top: '3%', left: '-27%'}"></div>
  </div>
</template>

<script>

export default {
  methods: {
    initChart(name, Data) {
      console.log(Data)
      const getchart = this.$echarts.init(document.getElementById('echart-pie'))
      var option = {
        tooltip: {
          trigger: 'item',
          formatter: '{b}<br/> 数量: {c}'
        },
        legend: {
          orient: 'vertical',
          left: '27%',
          top: '4%',
          data: Data.name
        },
        title: {
          text: '煤种比例分布图',
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
            type: 'pie',
            radius: ['32%', '75%'], // 饼图中饼状部分的大小所占整个父元素的百分比，空心圆
            data: Data,
            label: {
              normal: {
                show: true,
                position: 'inside',
                textStyle: {
                  fontFamily: 'Microsoft YaHei',
                  fontSize: 14, // 文字的字体大小
                  textBorderColor: '#FFFFFF',
                  textBorderWidth: 2,
                  textShadowColor: '(255, 255, 255)'
                },
                formatter: '{d}%'
              }
            }
          },
          {
            name: 'name',
            type: 'pie',
            radius: ['40%', '75%'], // 饼图中饼状部分的大小所占整个父元素的百分比, 空心圆
            data: Data,
            label: {
              normal: {
                show: true,
                textStyle: {
                  fontFamily: 'Microsoft YaHei',
                  fontSize: 14, // 文字的字体大小
                  textBorderColor: '#FFFFFF',
                  textBorderWidth: 2,
                  textShadowBlur: 1,
                  textShadowColor: '(255, 255, 255, 0.2)'
                },
                formatter: '{b}'
              }
            }
          }
        ],
        itemStyle: {
          emphasis: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(30, 144, 255，0.5)'
          }
        },
        color: ['#FFD54F', '#64B5F6', '#FF8A65', '#AED581', '#F06292', '#BA68C8', '#78909C'] // 300配色卡
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
