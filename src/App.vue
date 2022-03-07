<template>
  <div id="app">
    <!--<vue-particles color="#dedede"></vue-particles>-->
    <!-- 路由占位符 -->
    <router-view></router-view>
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
