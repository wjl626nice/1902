//app.js
App({
  // 小程序初始化时执行
  onLaunch: function () {
    console.log('小程序初始化')
  },
  // 小程序呈现时执行
  onShow: function(){
    console.log('展示小程序')
  },
  // 小程序隐藏时执行
  onHide: function(){
    console.log('小程序隐藏')
  },
  globalData: {
    userInfo: null
  },
  aaaa: function(){
    console.log(111)
  }
})