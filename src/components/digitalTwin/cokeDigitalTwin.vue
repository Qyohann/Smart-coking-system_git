<template>
    <div class='DataClassify'>
        <!-- 面包屑导航区 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/homePage' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>数字孪生模拟监测焦化过程</el-breadcrumb-item>
        </el-breadcrumb>
      <video class='video' :preload="preload" :height="height" :width="width" align="center" :controls="controls" >
        <source :src="videoSrc" type="video/mp4">
      </video>
      <p class='link' style="color:white">(摘自 https://www.bilibili.com/video/BV1w64y1o7H3)</p>
    </div>
</template>

<script>
export default {
  name: 'Video',
  data () {
    return {
      videoSrc: require('../../assets/digitalTwin.mp4'),
      width: '50%',
      height: '25%',
      preload: 'auto',
      controls: true
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
}

@media screen and (max-width: 1300px){ /* 笔记本 */
  .video{
      padding-left: 25%;
  }
}

@media screen and (min-width: 1300px){  /* 台式 */
  .video{
      padding-left: 22%;
      padding-top: 4%;
  }
}

.link{
    margin-top: 0px;
    text-align:  center;
}
</style>
