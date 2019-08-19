// pages/ballFriend/ballFriend.js
const APP= getApp();
const ROOT_URL = APP.globalData.ROOT_URL;
const OPENID = wx.getStorageSync('openid');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    myid:wx.getStorageSync("myid"),
    list:"",
    isuser: true,
    checkIsShow: APP.globalData.checkIsShow
  },

  friendDetail:function(e){
    if(wx.getStorageSync("id")===1){
      let user = this.data.list[e.currentTarget.id]
      wx.setStorageSync("fuser", user)
      wx.navigateTo({
        url: '/pages/friendDetail/friendDetail',
      })
    }else{
      let user = this.data.list[e.currentTarget.id].member_b_id
      wx.setStorageSync("group", this.data.list[e.currentTarget.id].group)
      wx.setStorageSync("fuser", user)
      wx.navigateTo({
        url: '/pages/friendDetail/friendDetail',
      })
    }
  },
  friendDetailUser: function (e) {
    if (wx.getStorageSync("id") == "1") {
      let user = this.data.list[e.currentTarget.id]
      wx.setStorageSync("fuser", user)
      wx.navigateTo({
        url: '/pages/friendDetail/friendDetail',
      })
    } else {
      let user = this.data.list[e.currentTarget.id].member_b_id
      wx.setStorageSync("group", this.data.list[e.currentTarget.id].group)
      wx.setStorageSync("fuser", user)
      wx.navigateTo({
        url: '/pages/friendDetail/friendDetail',
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    if (options.id){
      wx.setStorageSync("id", options.id)
    }
    let id = wx.getStorageSync("id")
    if (id==1){
      that.setData({
        isuser: false,
      })
      wx.request({
        url: `${APP.globalData.ROOT_URL}actor_activity/user/`,
        methodl:'GET',
        data:{
          openid: OPENID,
        },
        success(res){
          console.log(res)
          for (var i=0; i<res.data.data.length; i++){
            var e = res.data.data[i].avatar;
            var x = e.split('://');
            if (x.length > 1) {
              res.data.data[i].avatar =  e;
            } else {
              
              res.data.data[i].avatar =  ROOT_URL + e;
            }
          }
          
          that.setData({
            list: res.data.data,
          })

        }
      })

    }else{
      wx.setStorageSync("id", 0)
      that.setData({
        isuser: true,
      })
    wx.request({
      url: `${APP.globalData.ROOT_URL}group/myGroup/`,
      method:"GET",
      data:{
        member_a:that.data.myid
      },
      success(res){
        console.log(res)
        let lists = res.data.data;
        function avatarUrl(e) {

          var x = e.split('://');
          if (x.length > 1) {
            return e;
          } else {
            return ROOT_URL + e;
          }
        }
        for (var i in lists){
          lists[i].member_b_id.avatar = avatarUrl(lists[i].member_b_id.avatar);
        }
        
        that.setData({
          list:lists
        })
      }
    })
    }
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
    let id={"id":wx.getStorageSync("id")}
    this.onLoad(id)
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