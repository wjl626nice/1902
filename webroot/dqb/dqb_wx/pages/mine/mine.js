// pages/mine/mine.js
const APP = getApp();
const ROOT_URL = APP.globalData.ROOT_URL;

Page({

  /**
   * 页面的初始数据
   */
  data: {
    headimg:'',
    nickname:'',
    checkIsShow: wx.getStorageSync('checkIsShow'),
  },
  bindEdit:function(){
    wx.navigateTo({
      url: '/pages/personalEdit/personalEdit',
    })
  },
  myWallet:function(){
    wx.navigateTo({
      url: '/pages/myWallet/myWallet',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    var userInfo = wx.getStorageSync('userInfo');
    that.setData({
      headimg: userInfo.avatar,
      nickname: userInfo.nickName
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    let userinfo= wx.getStorageSync("userInfo")
    wx.request({
      url: `${APP.globalData.ROOT_URL}member/getMemberInfo/`,
      method:"GET",
      data:{
        openid:wx.getStorageSync("openid")
      },
      success:(res)=>{
        function avatarUrl(e) {
          var x = e.split('://');
          if (x.length > 1) {
            return e;
          } else {
            return ROOT_URL + e;
          }
        }

        res.data.data.avatar = avatarUrl(res.data.data.avatar)
        wx.setStorageSync('userInfo', res.data.data)
        this.setData({
          headimg: res.data.data.avatar,
          nickname: res.data.data.nickname
        })
      }
    })
  },
  feedback:function(e){
    wx.navigateTo({
      url: '/pages/feedback/feedback',
    })

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})