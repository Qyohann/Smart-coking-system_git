<template>
    <div class='welcomeContainer'>
        <div class='img'>
            <div class='title'>
                <span>系统使用介绍</span>
            </div>
            <vue-particles class='particle' linesColor="#B2B2B2" :linesWidth="1" color="#B2B2B2" :particlesNumber="150" shapeType="circle" clickMode="repulse" hoverMode="repulse"></vue-particles>
        </div>
        <div class='cards'>
            <el-card class="box-card1">
                <div class="card-header">
                    <p class='CellTitle'>煤数据处理</p>
                    <el-button type="text" class="button" @click="gotoData">查看使用</el-button> <!-- 按钮链接跳转  -->
                    <p class='data'><strong>数据上传查看:</strong>煤数据展示界面与后台数据库进行绑定并实时更新，其提供强大的数据管理、操作以及可视化功能。</p>
                    <p class='data'><strong>数据统计分析:</strong>以分布图和数值等形式展示给用户当前煤数据库的相关统计特性。</p>
                    <p class='data'><strong>煤种自动分类:</strong>以国家标准为参考对上传的煤数据的煤种类别进行算法自动精细分类。</p>
                    <p><strong>煤化工国家标准查看:</strong>提供了20余份最新相关国家标准文件供用户在线浏览。</p>
                </div>
            </el-card>
            <el-card class="box-card2">
                <div class="card-header">
                    <p class='CellTitle'>焦炭质量预测</p>
                    <el-button type="text" class="button" @click="gotoCokeQuality">查看使用</el-button>
                    <p><strong>人工智能与专家系统算法:</strong>两套不同体系方法的焦炭质量预测，预测质量指标涵盖CSR,CRI,M40,M25以及M10。</p>
                </div>
            </el-card>
            <el-card class="box-card3">
                <div class="card-header">
                    <p class='CellTitle'>配煤方案辅助决策</p>
                    <el-button type="text" class="button" @click="gotoCoalBlending">查看使用</el-button>
                    <p><strong>人工智能与专家系统算法:</strong>两套不同体系方法的配煤方案辅助决策，在保障焦炭质量不下降的前提下，降低原料煤的使用成本。</p>
                </div>
            </el-card>
            <el-card class="box-card4">
                <div class="card-header">
                    <p class='CellTitle'>数字孪生模拟监测</p>
                    <el-button type="text" class="button" @click="gotoVR">查看使用</el-button>
                    <p><strong>数字孪生：</strong>炼焦过程的VR可视化以及参数监控，让传感器数据与服务器之间建立交互并进行炼焦过程的3D动态展示。</p>
                </div>
            </el-card>
            <el-card class="box-card5">
                <div class="card-header">
                    <p class='CellTitle'>其它功能</p>
                    <el-button type="text" class="button" @click="gotoReduce">查看使用</el-button>
                    <p><strong>未来功能：</strong>焦化过程节能与优化、焦油处理等。</p>
                </div>
            </el-card>
        </div>
        <el-dialog
            title="用户使用协议"
            :visible.sync="showuseragreement"
            width="80%"
            :before-close="handleClose"
            :append-to-body='true'
            center
            > <!-- 不用body-append-to-body, dialog内容会与父级body信息重叠-->
            <p>感谢使用'用于焦炭质量预测与配煤智能化决策的AI辅助专家系统'！</p>
            <h3>1. 特别提示</h3>
            <p>1.1 为使用本软件及服务，您应当阅读并遵守《用户使用协议》（以下简称“本协议”）。请您务必审慎阅读、充分理解各条款内容，特别是免除或者限制责任的条款，以及同意或使用某项服务的单独协议，并选择接受或不接受。</p>
            <p>1.2 除非您已阅读并接受本协议所有条款，否则您无权使用本软件及相关服务。</p>
            <p>1.3 蒙纳士苏州科学技术研究院绿色化工和先进材料实验室（以下称“本实验室”）同意按照本协议的规定及其不时发布的操作规则提供基于互联网的相关服务（以下称"本服务"）。</p>
            <h3>2. 协议的范围</h3>
            <p>2.1 协议适用主体范围</p>
            <p>本协议是用户与本实验室之间关于用户访问使用本软件，以及使用本实验室相关服务所订立的协议。</p>
            <p>2.2 协议关系</p>
            <p>本协议内容同时包括本实验室可能不断发布的关于本服务的相关协议、业务规则等内容。上述内容一经正式发布，即为本协议不可分割的组成部分，用户若继续使用本实验室软件及服务同样应当遵守。</p>
            <h3>3. 服务内容与授权使用范围</h3>
            <p>3.1 本软件根据用户实际需求提供服务。本实验室保留随时变更、中断或终止部分或全部服务的权利。</p>
            <p>3.2 软件电脑应用的授权使用范围：</p>
            <p>1) 用户可以在电脑上访问、登录、使用、显示、运行本软件。</p>
            <p>2) 保留权利：未明示授权的其他一切权利均归本实验室所有。</p>
            <h3>4. 知识产权</h3>
            <p>4.1 本实验室是本软件的知识产权权利人。本软件的一切著作权、商标权、专利权、商业秘密等知识产权，以及与本软件相关的所有信息内容均受中华人民共和国法律法规和相应的国际条约保护，本实验室享有上述知识产权，除非事先经本实验室的合法授权，任何人皆不得擅自以任何形式使用，否则本实验室可立即终止向该用户提供产品和服务，并依法追究其法律责任，赔偿本实验室的一切损失</p>
            <p>4.2 用户只有在获得本实验室或其他相关权利人的授权之后才能使用这些内容，而不能擅自复制、再造这些内容、或创造与内容有关的派生产品。
            <h3>5. 隐私保护</h3>
            <p>5.1 保护用户隐私是本软件的一项基本政策，本实验室保证未经用户同意不对外公开或向第三方提供用户申请资料及用户在使用本服务时存储在本软件的个人信息，但下列情况除外：</p>
            <p>1) 事先获得用户的明确授权；</p>
            <p>2) 根据有关的法律法规要求；</p>
            <p>3) 按照相关政府主管部门的要求；</p>
            <p>4) 为维护社会公众的利益；</p>
            <p>5) 为维护本软件手机应用的合法权益。</p>
            <p>5.2 在不透露单个用户隐私资料的前提下，本实验室有权对整个用户数据库进行分析并对用户数据库进行商业上的利用。</p>
            <h3>6. 服务变更、中断或中止</h3>
            <p>6.1 软件更新<p>
            <p>6.1.1 为了改善用户体验、完善服务内容，本实验室将不断努力开发新的服务，并为用户不时提供软件更新（这些更新可能会采取软件替换、修改、功能强化、版本升级等形式）。</p>
            <p>6.1.2 为了保证本软件及服务的安全性和功能的一致性，本实验室有权不经向用户特别通知而对软件进行更新，或者对软件的部分功能效果进行改变或限制。</p>
            <p>6.2 为了软件的正常运行，本实验室需要定期或不定期地对软件进行停机维护，因此类情况而造成的正常服务中断、停止，用户应该予以理解，本实验室应尽力避免服务中断、停止或将中断、停止时间限制在最短时间内。</p>
            <p>6.3 服务中断或终止</p>
            <p>6.3.1 如发生下列任何一种情形，本实验室有权随时中断或终止向用户提供本协议项下的本服务而无需通知用户，对因此而产生的不便或损害，本实验室对用户不承担任何责任：</p>
            <p>1) 定期检查或施工，更新软硬件等，本实验室有权暂停服务，但会尽快完成维护、更新工作；</p>
            <p>2) 服务器遭受损坏，无法正常运作；</p>
            <p>3) 突发性的软硬件设备与电子通信设备故障；</p>
            <p>4) 网络提供商线路或其它故障；</p>
            <p>5) 在紧急情况之下为维护国家安全或其它用户及第三者之人身安全；</p>
            <p>6) 地震等不可抗力及其他第三方原因造成服务瘫痪、中断或丢失。</p>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="showuseragreement = false">接 受</el-button>
                <el-button type="primary" @click="logout">不 接 受</el-button>
            </span>
        </el-dialog>
        <!--
        <div class='introduction'>
            <h4 style='color:#454545'>煤数据处理</h4>
            <p class='content'>该模块功能主要包含煤的数据上传查看、数据统计分析以及煤的分类标准三大部分。针对数据上传查看部分，系统界面中的煤数据与后台数据库进行绑定并实时更新，操作时需要用户根据系统所规定的数据格式进行上传，而煤数据的可视化则以表格的形式呈现，此外该部分还支持用户对煤数据进行删除和筛选查看等操作。针对数据统计分析部分，主要以分布图和数值等形式展示用户所选择的煤数据的相关特性，包含均值、方差等。针对煤分类部分，主要以国家标准为参考对上传的煤数据进行自动精细分类。</p>
            <h4 style='color:#454545'>焦炭质量预测</h4>
            <p class='content'>_</p>
            <h4 style='color:#454545'>配煤方案推荐</h4>
            <p class='content'>_</p>
            <h4 style='color:#454545'>焦化过程VR模拟与预测</h4>
            <p class='content'>_</p>
            <h4 style='color:#454545'>焦化过程节能与优化</h4>
            <p class='content'>_</p>
        </div>
        -->
    </div>
</template>

<script>
export default {
  data () {
    return {
      showuseragreement: false
    }
  },
  mounted () {
    this.CheckUserAgreement()
  },
  methods: {
    gotoData() {
      this.$router.replace('/dataUploading')
    },
    gotoCokeQuality() {
      this.$router.replace('/CokeQualityAI')
    },
    gotoCoalBlending() {
      this.$router.replace('/CoalBlendingAI')
    },
    gotoVR() {
      this.$router.replace('/cokeDigitalTwin')
    },
    gotoReduce() {
      this.$router.replace('/cokingOptimization')
    },
    closeUseragreement() {
      this.show_useragreement = false
    },
    CheckUserAgreement() {
      var item = sessionStorage.getItem('showUserAgreement')
      if (item === 'true') { // 判断cookie状态，如果是true则弹出用户协议，false则不弹出
        this.showuseragreement = true
        console.log(this.showuseragreement)
      }
      sessionStorage.setItem('showUserAgreement', JSON.stringify('false'))
    },
    logout () {
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="less" scoped>

@media screen and (max-width: 1300px){ /*当屏幕尺寸小于1500px时，应用下面的CSS样式, 笔记本电脑为1280*720*/
    .title{ //control the upper title "使用介绍"
        text-align: center;
        margin:0;
        padding-top:2.2%;
        font-size: 25px;
        font-family: 'Microsoft YaHei';
        color: white; // #317EBD
    }
    .box-card1{
        background-color: #3C6CC2;
        color: white;
        text-align:justify;
        background-repeat: no-repeat;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 52%;
        left: 7%;
        bottom: 37%;
        font-size: 85%;
        border-radius: 25px;
        border: 0px;
    }
    .box-card2{
        background-color: #FFA41D;
        color: white;
        text-align:justify;
        background-repeat: no-repeat;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 35%;
        top:11%;
        font-size: 82%;
        border-radius: 25px;
        border: 0px;
    }
    .box-card3{
        background-color: #FF5050;
        color: white;
        text-align:justify;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 35%;
        bottom: 37%;
        font-size: 82%;
        border-radius: 25px;
        border: 0px;
    }

    .box-card4{
        background-color: #009999;
        background-repeat: no-repeat;
        color: white;
        text-align:justify;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 63%;
        top: 11%;
        font-size: 82%;
        border-radius: 25px;
        border: 0px;
    }

    .box-card5{
        background-color: #339933;
        color: white;
        text-align:justify;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 63%;
        bottom: 37%;
        font-size: 82%;
        border-radius: 25px;
        border: 0px;
    }
    .CellTitle{
        font-size: 24px;
        margin-bottom: -10px;
    }
    .button{
        position: relative;
        margin-left: 81%;
        top: -13px;
    }
}

@media screen and (min-width: 1300px){ /*当屏幕尺寸小于600px时，应用下面的CSS样式， 台式电脑为1980*1080 */
    .title{ //control the upper title "使用介绍"
        text-align: center;
        margin:0;
        padding-top:3.5%;
        font-size: 35px;
        font-family: 'Microsoft YaHei';
        color: white; // #317EBD
    }
    .box-card1{
        background-color: #3C6CC2;
        color: white;
        text-align:justify;
        background-repeat: no-repeat;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 52%;
        left: 7%;
        bottom: 33%;
        font-size: 120%;
        border-radius: 25px;
        border: 0px;
    }
    .box-card2{
        background-color: #FFA41D;
        color: white;
        text-align:justify;
        background-repeat: no-repeat;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 35%;
        top:15%;
        font-size: 120%;
        border-radius: 25px;
        border: 0px;
    }
    .box-card3{
        background-color: #FF5050;
        color: white;
        text-align:justify;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 35%;
        bottom: 33%;
        font-size: 120%;
        border-radius: 25px;
        border: 0px;
    }

    .box-card4{
        background-color: #009999;
        background-repeat: no-repeat;
        color: white;
        text-align:justify;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 63%;
        top: 15%;
        font-size: 120%;
        border-radius: 25px;
        border: 0px;
    }

    .box-card5{
        background-color: #339933;
        color: white;
        text-align:justify;
        font-family: Microsoft YaHei;
        position: absolute;
        width: 27%;
        height: 25%;
        left: 63%;
        bottom: 33%;
        font-size: 120%;
        border-radius: 25px;
        border: 0px;
    }
    .CellTitle{
        font-size: 29px;
        margin-bottom: -10px;
    }
    .button{
        position: relative;
        margin-left: 87%;
        top: -21px;

    }
}

.welcomeContainer{
    position: relative;
    width: 100%;
    height: 100%;
    overflow-y:hidden;
}
.particle{
    width: 100%;
    height: 100%;
}

.card-header{
    width: 88%;
    height: 90%;
    position: absolute;
    top: -0.5%;
    left: 6.5%;
    margin: 0 auto;
}

.content {
    margin-top: -12px;
}
h4{
    margin-top: -2px;
    font-family: 'Microsoft YaHei';
}
.el-button{
    margin-top: -20px;
    color: white;
}
/* 父相对定位，两个兄弟绝对定位，可以互相覆盖，z-index大在上面 */
.cards{
    position: absolute;
    height: 99%;
    width: 102%;
    top: 2%;
}

.data{
    margin-bottom: -6px;
}

</style>
