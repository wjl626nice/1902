// pages/replyMess/replyMess.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    num: '0',
    id: '',
    reply_id: '',
    openId: wx.getStorageSync('openid'),
    textareaVal: '',
    activity_id:'',

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
    const {id, memberID,activity_id} = options;
    this.setData({
      id,
      reply_id: memberID,
      activity_id:activity_id
    })

  },
  formSubmit: function() {
    if (this.data.textareaVal== "") {
      wx.showToast({
        title: '内容不能为空',
        icon: 'none'
      });
      return false;
    }

    const { id, openId, reply_id, textareaVal}= this.data;
    wx.request({
      url: app.globalData.ROOT_URL + '/reply/create/',
      method: 'POST',
      data: {
        message_id: id,
        reply_openid: openId,
        reply_content: textareaVal,
        to_reply_member: reply_id
      },
      success: (res) => {
        console.log(res)
        if(res['data']['code'] === 0){
          wx.showToast({
            title: '回复成功',
            icon: 'none'
          });
          setTimeout(()=> {
            /*wx.navigateBack({
              delta: 1
            });*/
            wx.redirectTo({
              url: '/pages/activeDetail/activeDetail?id=' + this.data.activity_id,
            })

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