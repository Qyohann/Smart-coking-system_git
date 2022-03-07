<template> <!--html代码的模板, App.vue是主组件，定义的所有组件都是在其下进行切换 -->
  <div id="app">
    <!--<vue-particles color="#dedede"></vue-particles>-->
    <!-- 路由占位符 -->
    <router-view></router-view> <!-- 渲染路由匹配到的组件，为全局注册 -->
  </div>
</template>

<script>

export default {
  name: 'app'
}
</script>

<style>
  html,body{
    padding:0;
    background-color: #3C3C3C;
    width: 100%;
    height: 100%;
    overflow-y:hidden; /*隐藏滚动条*/
    padding-right: 0 !important
  }
</style>
