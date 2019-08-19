
const APP = getApp();
const ROOT_URL = APP.globalData.ROOT_URL;
const OPENID = wx.getStorageSync('openid');
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  avatarUrl: function (e) {
    var x = e.split('://');
    if (x.length > 1) {
      return e;
    } else {
      return ROOT_URL + e;
    }

  },
  getActiveList: function () {
    var that = this;
    wx.request({
      url: `${ROOT_URL}actor_activity/activity_my_list/`,
      method: 'GET',
      data: {
        openid: OPENID,
      },
      success(res) {
        console.log(res)
        for (var i = 0; i < res.data.data.length; i++) {
          res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
        }
        that.setData({
          mylist: res.data.data,
        })
      }
    })

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    let openid = wx.getStorageSync("openid");
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    setTimeout(function () {
      that.getActiveList();
      wx.hideLoading()
    }, 1500)

  },
  activeDetail: function (e) {
    var id = e.currentTarget.id;
    wx.navigateTo({
      url: '/pages/activeDetail/activeDetail?id=' + id,
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