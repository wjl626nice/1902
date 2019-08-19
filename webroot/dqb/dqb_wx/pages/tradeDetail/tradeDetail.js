const APP = getApp();
const ROOT_URL = APP.globalData.ROOT_URL;
const moment = require('../../utils/moment.js');
// pages/transDetail/transDetail.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
   currentPage: 1,
   listData: [],
   canPull: true,
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.initData();
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },
  //  处理时间函数
  formatTimeFun: function(val){
 
    return moment(val*1000).format('YYYY-MM-DD HH:mm')
  },
  initData: function (sign) {
    let data = [];
    wx.request({
      url: `${APP.globalData.ROOT_URL}member/transactionDetails`,
      method: 'GET',
      data: {
        openid: wx.getStorageSync("openid"),
        page: this.data.currentPage
      },
      success: res => {
        console.log(res);
        if(res['data']['code'] === 0 ){
           data = res['data']['data'];
           data.forEach((item) => {
             item.deal_add_time = this.formatTimeFun(item.add_time)
           })
           if(sign) {
             this.setData({
               listData: this.data.listData.concat(data)
             })

           }else {
             this.setData({
               listData: data
             })
           }
          if(data.length==10){
            this.setData({
              canPull: true
            })
          }else {
            this.setData({
              canPull: false
            })
          }
        }else {
          wx.showToast({
            title: res['data']['msg'],
            icon: "none"
          })
        }
      },
      error: err => {
        wx.showToast({
          title: '网络开小差~,请检查网络',
          icon: "none"
        })
      }
    })
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
    if(this.data.canPull){
      this.data.currentPage++;
      this.initData('pull')
    }
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})