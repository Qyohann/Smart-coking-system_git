<template>
    <el-container class='home-container'>
        <!-- 头部区域，每一个组件的名称就是类名，可以直接使用 -->
        <el-header class='header'>
            <div>
                <!-- <img src="../assets/logo.png" alt='' style="width:50px"> -->
                <span>用于焦炭质量预测与配煤智能化决策的AI辅助专家系统</span>
            </div>
            <img src= '../assets/Monash_Suzhou_Logo.png' alt='Logo' width="12%">
            <!-- <el-button type="info" @click='logout'>退出</el-button> -->
        </el-header>
        <!-- 页面主题区 -->
            <!-- 侧边栏,width记得加冒号-->
                <!-- 侧边栏菜单区 unique opended.左侧菜单栏每次只打开一个,router='true'以index为路由进行跳转-->
                <!-- :default-active要加: -->
                <el-menu
                class="el-menu-vertical-demo"
                background-color="white"
                text-color="#7F7F7F"
                active-text-color="#00133A"
                :unique-opened="true"
                :collapse='isCollapse'
                :collapse-transition= 'true'
                :router='true'
                :default-active= activePath
                mode="horizontal"
                >
                <el-menu-item index="homePage" @click="saveNavState('homePage')">
                  <i class="el-icon-menu"></i>
                  <span slot="title" class='titleColumn'>首页</span>
              </el-menu-item>
                <!-- 一级菜单 -->
                <el-submenu index='coalData'>
                    <template slot="title">
                    <i class="el-icon-s-data"></i>
                    <span class='titleColumn'>煤数据处理</span>
                    </template>
                    <!-- 二级菜单 -->
                    <el-menu-item-group>
                    <el-menu-item index="dataUploading" @click="saveNavState('dataUploading')" class='titleColumn'>煤数据上传与查看</el-menu-item>
                    <el-menu-item index="blendingdata" @click="saveNavState('blendingdata')" class='titleColumn'>配煤历史数据查看</el-menu-item>
                    <el-menu-item index="dataAnalysis" @click="saveNavState('dataAnalysis')" class='titleColumn'>煤数据统计分析</el-menu-item>
                    <el-menu-item index="dataClassify" @click="saveNavState('dataClassify')" class='titleColumn'>煤分类</el-menu-item>
                    <el-menu-item index="CoalStandard" @click="saveNavState('CoalStandard')" class='titleColumn'>煤化工国家标准</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <!-- 一级菜单 -->
                <el-submenu index='cokeQuality'>
                    <template slot="title">
                    <i class="el-icon-s-marketing"></i>
                    <span class='titleColumn'>焦炭质量预测</span>
                    </template>
                    <el-menu-item-group>
                    <el-menu-item index="CokeQualityAI" @click="saveNavState('CokeQualityAI')" class='titleColumn'>人工智能算法</el-menu-item>
                    <el-menu-item index="CokeQualityExpert" @click="saveNavState('CokeQualityExpert')" class='titleColumn'>专家系统算法</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <!-- 一级菜单 -->
                <el-submenu index='coalBlending'>
                    <template slot="title">
                    <i class="el-icon-s-order"></i>
                    <span class='titleColumn'>配煤方案辅助决策</span>
                    </template>
                    <el-menu-item-group>
                    <el-menu-item index="CoalBlendingAI" @click="saveNavState('CoalBlendingAI')" class='titleColumn'>人工智能算法</el-menu-item>
                    <el-menu-item index="CoalBlendingExpert" @click="saveNavState('CoalBlendingExpert')" class='titleColumn'>专家系统算法</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <!-- 一级菜单 -->
                <el-menu-item index="cokeDigitalTwin">
                  <i class="el-icon-s-platform"></i>
                  <span slot="title" class='titleColumn'>数字孪生模拟监测焦化过程</span>
                </el-menu-item>
                <!-- 一级菜单 -->
                <el-submenu index='cokeReduce'>
                    <template slot="title">
                    <i class="el-icon-s-help"></i>
                    <span class='titleColumn'>其它功能</span>
                    </template>
                    <el-menu-item-group>
                      <el-menu-item index="cokingOptimization" class='titleColumn'>焦化过程节能与优化</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-button type="primary" @click='logout'>退出</el-button>
                </el-menu>
            <!-- 右侧内容主体,记得要放路由占位符-->
            <el-container>
            <el-main >
              <div class='mainBackground' :style="{backgroundImage: 'url(' + background.backgroundImg + ')', opacity:0.93, backgroundRepeat:background.backgroundRepeat,backgroundSize:background.backgroundSize}">
                    <router-view></router-view>
              </div>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
export default {
  data () {
    return {
      // 设置particle的背景图像信息
      background: {
        backgroundImg: require('../assets/coal_8.jpg'), // particles显示的图像，需要用require获取，用CSS无法解析路径
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover' // 背景尺寸变化修改这个
      },
      // 是否折腾左侧栏
      isCollapse: false,
      // 被激活的链接地址
      activePath: ''
    }
  },
  created() {
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    // 点击按钮，切换菜单的折叠与展开
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
    },
    logout () {
      this.$router.push('/login')
    },
    saveNavState(activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    }
  }
}
</script>

<style lang="less" scoped>
.el-header{
    background-color: #408ECD;
    color: white;
    justify-content: space-between;
    display: flex;
    padding-left: 0px;
    align-items: center;
    font-family: 'SimHei';
    font-size: 21px;
    > div {
        display: flex;
        align-items: center;
        span {
            margin-left: 25px;
        }
    }
}
.header{
  position: relative;
}

.el-aside{
    background-color: #232323;
    overflow-x: hidden;
}
.el-main{
    background-color: #F9F9F9;
}
.home-container{
    height: 100%;
}

.el-menu{
    width: 100%; // 去除左侧菜单栏留白问题
}

/* .toggle-button{
    background-color: #323232;
    font-size: 18px;
    line-height: 24px;
    color: white;
    text-align: center;
    letter-spacing: 0.2em;
    cursor: pointer;
} */
.el-main{
  padding: 0; //设置的padding是在父元素上，指子元素和父元素的padding大小
}
.mainBackground{
  margin: 0px;
  width: 100%;
  height: 100%;
}

.el-button{
  margin-top: 0.6%;;
  float:right;
  margin-right: 2%
}

.titleColumn{
  font-size: 15.5px;
}
</style>
