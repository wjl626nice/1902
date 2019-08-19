// pages/friendDetail/friendDetail.js
var util = require('../../utils/util.js');
var moment = require('../../utils/moment.js');  
const APP = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user:'',
    together:'',//共同球友
    toball:'',//一起踢过球
    football:'',//踢球总次数
    friend:"",//球友总数
    group:"",
    isShow:false,
    xgroup:"",
    isgroup:true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (e) {
    console.log(wx.getStorageSync("fuser"))
    this.setData({
      user:wx.getStorageSync("fuser"),
      group:wx.getStorageSync("group")
    })
    this.data.user.age = String(Number(util.formatTime(new Date()).substring(0, 4))-this.data.user.age).substr(2,1)+"0";
    this.setData({
      user: this.data.user,
    })
    if(this.data.group==""){
      this.setData({
        isgroup: false
      })
    }
    //共同球友
    wx.request({
      url: `${APP.globalData.ROOT_URL}/group/common/`,
      method:"GET",
      data:{
        member:wx.getStorageSync("myid"),
        friend:this.data.user.id
      },
      success:(res)=>{
        this.setData({
          together: res.data.data.length
        })
      }
    })
    //一起踢过球数
    wx.request({
      url: `${APP.globalData.ROOT_URL}actor_activity/together_ball/`,
      method: "GET",
      data: {
        openid: wx.getStorageSync("openid"),
        id: this.data.user.id
      },
      success: (res) => {
        this.setData({
          toball: res.data.data.sum
        })
      }
    })
    //踢球总次数
    wx.request({
      url: `${APP.globalData.ROOT_URL}actor_activity/sum/`,
      method: "GET",
      data: {
        id: this.data.user.id
      },
      success: (res) => {
        this.setData({
          football: res.data.data.sum
        })
      }
    })
    //球友总数
    wx.request({
      url: `${APP.globalData.ROOT_URL}/group/myGroup/`,
      method: "GET",
      data: {
        member_a: this.data.user.id
      },
      success: (res) => {
        console.log(res)
        this.setData({
          friend: res.data.data.length
        })
      }
    })
    console.log(this.data.isgroup)
  },
  //修改标签
  tipEdit:function(e){
    this.setData({
      isShow:true
    })
  },
  changeInputVal:function(e){
    let group=e.detail.value
    let length = group.length
    console.log(e.detail.value)
    console.log(e.detail.length)
    if(length>6){
      wx.showToast({
        title: '分组名称不得超过6个字！',
        icon:"none"
      })
      this.setData({
        xgroup:""
      })
      return ""
    }
    this.setData({
      xgroup: e.detail.value
    })
  },
  //确认
  confirmButton:function(){
    if(this.data.xgroup==""){
      wx.showToast({
        title: '分组名不能为空！',
        icon:"none"
      })
    }else{
      wx.request({
        url: `${APP.globalData.ROOT_URL}/group/up/`,
        method:"POST",
        data:{
          member_a_id:wx.getStorageSync("myid"),
          member_b_id:wx.getStorageSync("fuser").id,
          group:this.data.xgroup
        },
        success:(res)=>{
          if(res["data"]["code"]==0){
            wx.showToast({
              title: '更改成功！',
            })
            wx.setStorageSync("group", this.data.xgroup)
            this.setData({
              isShow: false,
              xgroup:""
            })
            this.onLoad();
          }else{
            wx.showToast({
              title: res.data.msg,
              icon:"none"
            })
          }
        }        
      })
    }
  },
  //取消
  cancelButton:function(){
    this.setData({
      isShow: false,
      xgroup: ""
    })
  },

  deleteFriend:function(){
    wx.request({
      url: `${APP.globalData.ROOT_URL}/group/delete/`,
      method: "POST",
      data: {
        member_a_id: wx.getStorageSync("myid"),
        member_b_id: wx.getStorageSync("fuser").id,
      },
      success: (res) => {
        if (res["data"]["code"] == 0) {
          wx.showToast({
            title: '删除好友成功',
          })
          wx.setStorageSync("fuser", "")

          setTimeout(() => {
            
          
          wx.switchTab({
            url: '/pages/friendIndex/friendIndex',
          })
          },500)
          
        } else {
          wx.showToast({
            title: res.data.msg,
            icon: "none"
          })
        }
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