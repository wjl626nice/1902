// pages/login/login.js
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    
    
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


  },

  getUserInfo:function(e){
    var that = this
    if (e.detail.userInfo) {
      wx.login({
        success: res => {
          // 发送 res.code 到后台换取 openId, sessionKey, unionId
          wx.request({
            url: `https://rimetleague.com/member/userGetOpenID/`,
            data: {
              code: res['code']
            },
            method: 'POST',
            success: res => {
              wx.setStorageSync('openid', res.data.data.openid);
              wx.getUserInfo({
                withCredentials: true,
                success: function (res_user) {
                  // console.log(res_user)
                  wx.setStorageSync('userInfo', res_user.userInfo);
                  wx.request({
                    url: `https://rimetleague.com/member/member/`,
                    method: 'GET',
                    data: {
                      openid: res.data.data.openid,
                      nickname: res_user.userInfo.nickName,
                      avatar: res_user.userInfo.avatarUrl,
                    },
                    header: {
                      'content-type': 'json'
                    },
                    success: function (datas) {
                      // console.log(datas)
                      wx.setStorageSync('myid', datas.data.data.id)
                      wx.switchTab({
                         url: '/pages/home/home',
                      })
                    }
                  });
                       
                }
              })
              
            
            }
          })
        }
      })
      
    } else {
      wx.showToast({
        title: "为了您更好的体验,请先同意授权",
        icon: 'none',
        duration: 2000
      });
    }

  }
})