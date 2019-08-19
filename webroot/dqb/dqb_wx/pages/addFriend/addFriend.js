// pages/addFriend/addFriend.js
const APP = getApp();
const ROOT_URL = APP.globalData.ROOT_URL;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    status:false,
    list:"",
    iss:"",
    length:[],
  },
  //图片格式化
  avatarUrl: function (e) {
    var x = e.split('://');
    if (x.length > 1) {
      return e;
    } else {
      return ROOT_URL + e;
    }
  },

  changestatus: function (options) {
    console.log(options)
    if (this.data.length[options.currentTarget.id]==true){
      return false
    }
    wx.request({
      url: `${ROOT_URL}group/create/`,
      method:"POST",
      data:{
        id:options.currentTarget.dataset.sqid,
        new_state:1
      },
      success:(res)=>{
        console.log(res)
        if(res.data.code==1008){
          wx.showToast({
            title: '已经互为球友！',
            icon: "none"
          })
          return false;
        }  
        let datas = this.data.length
        datas[options.currentTarget.id] = true
        this.setData({
          length: datas,
        })
        wx.showLoading({
          title: '加载中',
          mask: true
        })
        setTimeout(function () {
          wx.hideLoading()
        }, 500)
      }
    })   
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (e) {
    console.log(e.id)
    if (e.id !== undefined && e.id!=wx.getStorageSync("myid")){
      let content="请求添加好友"
      wx.request({
        url: `${ROOT_URL}news/create/`,
        method:"POST",
        data:{
          applicant_openid:wx.getStorageSync("openid"),
          respondent_id:e.id,
          content:content
        },
        success:(res)=>{
          console.log(res)
        }
      })
    }
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    setTimeout(function () {
      wx.hideLoading()
    }, 1000)
    wx.request({
      url: `${ROOT_URL}news/application/`,
      method: "GET",
      data: {
        respondent_openid: wx.getStorageSync("openid"),
        page:1
      },
      success:(e)=>{
        console.log(e)
        var count=[]
        for (let i = 0; i <e.data.data.length;i++){
          if(e.data.data[i].new_state==1){
            count[i] = true
          }else{
            count[i] = false
          }
        }

        console.log(e.data.data)
        for(let i in e.data.data){
          e.data.data[i].applicant.avatar = this.avatarUrl(e.data.data[i].applicant.avatar);
        }
        this.setData({
          list: e.data.data,
          length: count
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