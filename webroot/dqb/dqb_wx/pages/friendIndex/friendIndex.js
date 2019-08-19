// pages/friendIndex/friendIndex.js
const APP = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    ball_num: "",
    checkIsShow: wx.getStorageSync('checkIsShow')
  },

  ballFriend:function(){
    wx.navigateTo({
      url: '/pages/ballFriend/ballFriend?id=0',
    })
  },
  addFriend: function () {
    wx.navigateTo({
      url: '/pages/addFriend/addFriend',
    })
  },
  onShareAppMessage:function(e){
    let user=wx.getStorageSync("userInfo")
    let myid=wx.getStorageSync("myid")
    if (e.from === 'button') {
      // 来自页面内转发按钮
    return {
      title:user.nickName+"在点球吧请求添加为好友！" ,
      path:'/pages/addFriend/addFriend?id='+myid,// 用户点击首先进入的当前页面
      imageUrl: user.avatarUrl,
      success: function (res) {
        // 转发成功
        console.log("转发成功:");
      },
      fail: function (res) {
        // 转发失败
        console.log("转发失败:");
      }
    }
    
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: `${APP.globalData.ROOT_URL}/group/myGroup/`,
      method: 'GET',
      data: {
        member_a: wx.getStorageSync("myid")
      },
      success: (res) => {
        this.setData({
          ball_num: res.data.data.length
        })
      }
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
    wx.request({
      url: `${APP.globalData.ROOT_URL}/group/myGroup/`,
      method: 'GET',
      data: {
        member_a: wx.getStorageSync("myid")
      },
      success: (res) => {
        this.setData({
          ball_num: res.data.data.length
        })
      }
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

})