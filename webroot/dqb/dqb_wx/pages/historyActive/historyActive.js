// pages/historyActive/historyActive.js
var util = require('../../utils/util.js');  
const APP = getApp()
const OPENID = wx.getStorageSync('openid');

Page({

  /**
   * 页面的初始数据
   */
  data: {
    list:'',
    time: '',
  },
  updateImg:function(){
    wx.navigateTo({
      url: '/pages/leaveWord/leaveWord',
    })
  },
  //获取回复
  getreply:function(){
    var that = this
    var data=that.data.list
    console.log(that.data)
    var id = new Array();
    var reply = new Array();
    for(var i in data){
      id.push(data[i].originator_id.id)
    }
    for(var i in id){
      wx.request({
        url: `${APP.globalData.ROOT_URL}message/getAll/`,
        method: 'GET',
        data: {
          activity:id[i], 
        },
        success(res){
          reply.push(res)
          console.log(res)
        }
      })
    }
    console.log(reply)
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    that.setData({
      list: wx.getStorageSync("history").data,
    })
    var count1 = that.data.list.length
    that.setData({
      count: count1
    })

    let lists = that.data.list;
    var actTimes = [];
    for (var i = 0; i < that.data.list.length; i++){
      let time = util.formatTime(new Date(lists[i].activity_time * 1000));
      let times = [];
      //转换年月日
      times.push(time.substr(0,4));
      times.push(time.substr(5,2));
      times.push(time.substr(11,2));
      actTimes.push(times);


      time = time.substring(5, 16);
      lists[i].activity_time = time;
    }
    console.log(actTimes)

    that.setData({
      list:lists,
      time:actTimes,
    })

    console.log(that.data.list)
    that.getreply();
  },
  activeDetail: function (e) {
    var id = e.currentTarget.id;
    console.log(e)
    wx.navigateTo({
      url: '/pages/activeDetail/activeDetail?id=' + id,
    })
  },
  //留言
  leaveword: function(e){
    var id = e.currentTarget.id;
    console.log(e)
    wx.navigateTo({
      url: '/pages/leaveWord/leaveWord?id=' + id,
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