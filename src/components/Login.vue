<template>
    <div class='login_container' :style="{backgroundImage: 'url(' + background.backgroundImg + ')'}"> <!-- 修改这里填充满登录背景区域 -->
          <div class="particles">
            <vue-particles color="#dedede" :particlesNumber="150" shapeType="circle" clickMode="repulse" hoverMode="repulse" :style="{backgroundRepeat:background.backgroundRepeat, backgroundSize:background.backgroundSize}"></vue-particles>
          </div>
        <div class='login_box'>
            <!--头像标题区域-->
            <div class='logo'>
              <img src= '../assets/Monash_Suzhou_Logo.png' alt='Logo' width="60%">
            </div>
            <div class='avatar_box'><p class='title'>用于焦炭质量预测与配煤智能化决策的AI辅助专家系统</p></div>
            <!--登录表单区域,ref是表单的引用对象-->
            <el-form ref='loginFormRef' :model="loginForm" :rules='loginFormRules' label-width="0px" class='login_form'>
                <!--用户名-->
                <el-form-item prop='username'>
                    <el-input v-model='loginForm.username' placeholder="请输入用户账号" prefix-icon="el-icon-user-solid"></el-input>
                </el-form-item>
                <!--密码-->
                <el-form-item prop='password'>
                    <el-input v-model='loginForm.password' placeholder="请输入用户密码" prefix-icon="el-icon-s-goods" show-password auto-complete="new-password"></el-input>
                </el-form-item>
                <!--按钮区域-->
                <el-form-item class='btns'>
                    <el-button type="primary" @click='login'>登录</el-button>
                    <el-button type="info" @click="resetLoginForm">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      show_useragreement: true,
      // 设置particle的背景图像信息
      background: {
        backgroundLogo: require('../assets/Monash_Suzhou_Logo.png'),
        backgroundImg: require('../assets/coal_6.jpg'), // particles显示的图像，需要用require获取，用CSS无法解析路径
        backgroundRepeat: 'no-repeat',
        backgroundSize: '100% 100%',
        margin: 0 + 'px',
        padding: 0 + 'px'
      },
      // 这是登录表单的数据绑定对象
      loginForm: {
        username: '',
        password: ''
      },
      // 这是表单的验证规则对象
      loginFormRules: {
        // 验证用户名是否合法
        username: [
          { required: true, message: '请输入登录账号', trigger: 'blur' },
          { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
        ],
        // 验证密码是否合法
        password: [
          { required: true, message: '请输入登录密码', trigger: 'blur' },
          { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 点击重置按钮，重置登录表单
    resetLoginForm() {
      this.$refs.loginFormRef.resetFields()
    },
    login() {
      // valid为true说明预验证成功，满足输入要求，false则是预验证失败
      this.$refs.loginFormRef.validate(async valid => {
        sessionStorage.setItem('showUserAgreement', JSON.stringify(this.show_useragreement)) // seesion存储用户协议对话窗口
        if (!valid) return 0
        const result = this.$http.post('login', this.loginForm) // 将loginForm（账号密码）直接上传至后端，返回的是Promise对象
        result.then(res => { // 获取Promise对象中的具体数据
          if (res.status !== 200) return this.$message.error('登录失败！')
          console.log(res)
          this.$message.success('登录成功！')
          // 保存token，已便于记录用户状态，保存到sessionStorage中
          this.$router.push('/home')
        }
        )
      })
    }
  }
}
</script>

<style lang="less" scoped> //防止
.login_container{
    position: relative;
    left: 50%;
    top: 50%;
    background-color:#367CBA ;
    transform: translate(-50%,-50%);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    height: 100%;
    width: 100%;
    padding: 0px;
}

.title{
  position: absolute;
  top:-8%;
  left: -6%;
}

.login_box{
    width: 450px;
    height: 250px;
    background-color:rgba(0,0,0,0.15);
    border-radius: 10px;
    position: absolute;
    left: 23%;
    top: 58%;
    transform: translate(-50%,-50%);

    .avatar_box{
        height: 200px;
        width: 440px;
        color: white;
        font-family:'SimHei', Times, serif;
        font-size: 200%;
        text-align: left;
        position: absolute;
        left: 55%;
        transform: translate(-50%,-60%);
    }
}

.login_form{
    position: absolute;
    bottom: 10px;
    width: 100%;
    padding:0 20px;
    box-sizing: border-box;
}

.btns{
    display: flex;
    justify-content: flex-end;
}

.logo{
  position:absolute;
  top: -82%;
}

.particles{
  margin: 0;
}
</style>
