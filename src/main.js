import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import VueParticles from 'vue-particles'
import axios from 'axios'
import plTable from 'pl-table'
import 'pl-table/themes/index.css' // 引入样式（必须引入)，vuecli3.0不需要配置，cli2.0请查看webpack是否配置了url-loader对woff，ttf文件的引用,不配置会报错哦
import * as echarts from 'echarts' // 引入echart
import 'default-passive-events'
import Videojs from 'video.js'
import 'video.js/dist/video-js.css'

axios.defaults.baseURL = 'http://localhost:5000/' // 配置axios请求的根路径,用学校的网络需要修改这个 http://172.16.155.201:5000
Vue.prototype.$http = axios // 每一个组件都可以通过axios访问到http的请求
Vue.prototype.$video = Videojs

Vue.use(VueParticles)
Vue.use(plTable)
Vue.prototype.$echarts = echarts

Vue.config.productionTip = false
// main.js是文件的入口，作用一：实例化Vue，作用二：放置常用到的插件和CSS样式，作用三：存储全局变量
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
