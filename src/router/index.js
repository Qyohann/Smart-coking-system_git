// 该文件用于定义路由，Vue路由是指根据url分配到对应的处理程序；作用就是解析URL，调用对应的控制器（的方法，并传递参数）。Vue路由有助于在浏览器的URL或历史记录与Vue组件之间建立链接，从而允许某些路径渲染与之关联的任何一个视图。
// vue的路由用于对组件显示内容的切换，vue路由是全局注册，自带的组件也是全局胡策，不需要在页面的components中注册就可以使用
// 导入一些要跳转的路由组件
import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import '../assets/css/global.css'
import Home from '../components/Home.vue' // 导入路由组件，路由
import DataUploading from '../components/coalData/DataUploading.vue'
import CoalBlendData from '../components/coalData/CoalBlendData.vue'
import DataAnalysis from '../components/coalData/DataAnalysis.vue'
import DataClassify from '../components/coalData/DataClassify.vue'
import CoalStandard from '../components/coalData/DataStandard.vue'
import homePage from '../components/coalData/Welcome.vue'
import CokeQualityAI from '../components/cokeQuality/CokeQualityAI.vue'
import CokeQualityExpert from '../components/cokeQuality/CokeQualityExpert.vue'
import CoalBlendingAI from '../components/coalBlending/CoalBlendingAI.vue'
import CoalBlendingExpert from '../components/coalBlending/CoalBlendingExpert.vue'
import cokeDigitalTwin from '../components/digitalTwin/cokeDigitalTwin.vue'
import cokingOptimization from '../components/otherFunctions/cokingOptimization.vue'

Vue.use(VueRouter) // 实例化路由

const router = new VueRouter({ // 配置路由
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login }, // 路由跳转的组件
    {
      path: '/home',
      component: Home,
      redirect: '/homePage',
      children: [{ path: '/homePage', component: homePage },
        { path: '/dataUploading', component: DataUploading },
        { path: '/blendingdata', component: CoalBlendData },
        { path: '/dataAnalysis', component: DataAnalysis },
        { path: '/dataClassify', component: DataClassify },
        { path: '/CokeQualityAI', component: CokeQualityAI },
        { path: '/CokeQualityExpert', component: CokeQualityExpert },
        { path: '/CoalBlendingAI', component: CoalBlendingAI },
        { path: '/CoalBlendingExpert', component: CoalBlendingExpert },
        { path: '/CoalStandard', component: CoalStandard },
        { path: '/cokeDigitalTwin', component: cokeDigitalTwin },
        { path: '/cokingOptimization', component: cokingOptimization }]
    }]
})

// 挂载路由导航守卫, 用户直接访问不是login的页面，会强制跳转至登录界面
router.beforeEach((to, from, next) => {
  // to 将要访问的路径
  // from 代表从哪个路径跳转而来
  // next 是一个函数，表示放行

  if (to.path === '/login') return next()
  // 获取token,等之后添加
  // const tokenStr = window.sessionStorage.getItem('token')
  // if (!tokenStr) return next('login')
  next()
})

export default router // 导出路由让其它地方可以导入该路由
