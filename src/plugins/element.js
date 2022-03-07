import Vue from 'vue'
// 导入Element Ui 组件
import { Button, Form, FormItem, Input, Message, Container, Header, Aside, Main, Menu, Submenu, MenuItemGroup, MenuItem, Breadcrumb, BreadcrumbItem, Card, Row, Col, Table, TableColumn, Select, Option, MessageBox, Dialog, Pagination } from 'element-ui'
import '../../node_modules/element-ui/lib/theme-chalk/base.css' // 引入动画 淡入淡出 fadein fade
// Vue.use注册为全局组件
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItemGroup)
Vue.use(MenuItem)
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)
Vue.use(Card)
Vue.use(Row)
Vue.use(Col)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Select)
Vue.use(Option)
Vue.use(Dialog)
Vue.use(Pagination)
Vue.prototype.$message = Message // message需要全局挂载
Vue.prototype.$confirm = MessageBox.confirm // MessageBox需要全局挂载,不用use
