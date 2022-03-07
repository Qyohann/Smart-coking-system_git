import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import '../assets/css/global.css'
import Home from '../components/Home.vue' // 导入路由组件
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

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
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

export default router
