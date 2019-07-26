//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    dd: '冬冬',
    id: 11,
    motto: 'Hello World',
    userInfo: {},
    a:1,
    b:5,
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    students: [
      {name:'冬冬',age:25},
      {name:'书园', age: 16}
    ]
  },
  changeDD: function () {
    this.setData({
      dd: '王冬冬'
    })
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    console.log('页面正在被初始化')
  },
  onShow: function () {
    console.log('页面正在展示')
  },
  onReady: function () {
    console.log('页面正在渲染')
  },
  onHide: function () {
    console.log("页面被隐藏了")
  },
  onUnload: function () {
    console.log('页面被销毁了！')
  }
})
