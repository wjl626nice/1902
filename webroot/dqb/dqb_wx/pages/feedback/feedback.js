// pages/replyMess/replyMess.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    num: '0',
    openId: wx.getStorageSync('openid'),
    textareaVal: '',

  },
  textInput: function (e) {
    var that = this;
    that.setData({
      num: e.detail.cursor,
      textareaVal: e.detail.value
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  formSubmit: function() {
    if(this.data.textareaVal==""){
      wx.showToast({
        title: '内容不能为空',
        icon: 'none'
      });
      return false;
    }
    wx.request({
      url: app.globalData.ROOT_URL + '/admin/Feedback/',
      method: 'POST',
      data: {
        openid:this.data.openId,
        content:this.data.textareaVal,

      },
      success: (res) => {
        console.log(res)
        if(res['data']['code'] === 0){
          wx.showToast({
            title: '反馈成功',
            icon: 'none'
          });
          setTimeout(()=> {
            wx.navigateBack({
              delta: 1
            });

          }, 300)
        }else {
          wx.showToast({
            title: res['data']['msg'],
            icon: 'none'
          })
        }
      }
  
    }, err=> {
      wx.showToast({
        title: '网络错误，请检查网络',
        icon: 'none'
      })
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