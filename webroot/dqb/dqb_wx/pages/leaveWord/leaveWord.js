// pages/leaveWord/leaveWord.js
const app = getApp()
const ROOT_URL = app.globalData.ROOT_URL;
const OPENID = wx.getStorageSync('openid');
let activity_id = '';
Page({

  /**
   * 页面的初始数据
   */
  data: {
    num:'0',
    items:'',
    itemsImg:[],
  },

  textInput:function(e){
    var that = this;
    that.setData({
      num: e.detail.cursor
    })
  },
  // 选择本地图片
  Uploadimg: function (e) {
    var that = this;
    wx.chooseImage({
      count: 6,  //最多可以选择的图片总数  
      sizeType: ['original', 'compressed'],// 可以指定是原图还是压缩图，默认二者都有 
      success: function (res) {
        //console.log(res.tempFilePaths);
        that.setData({
          items: res.tempFilePaths
        })
        for (var i = 0; i < that.data.items.length; i++) {
          wx.uploadFile({
            url: `${ROOT_URL}activity/file/`,
            filePath: that.data.items[i],
            name: 'img',
            success: function (res) {
              var data = JSON.parse(res.data);
              that.data.itemsImg.push(data.data.path_list[0]);

            }
          })
        }
      }
    })
  },
  //删除图片
  deleteImg: function (e) {
    let that = this;
    let imgs = that.data.items;
    let imgs1 = that.data.itemsImg;
    imgs.splice(e.currentTarget.dataset.index, 1);
    imgs1.splice(e.currentTarget.dataset.index, 1);
    that.setData({
      items: imgs,
      itemsImg: imgs1,
    })

  },
  //留言
  formSubmit: function (e) {
    if (e.detail.value.text == "") {
      wx.showToast({
        title: '内容不能为空',
        icon: 'none'
      });
      return false;
    }
    let that = this;
    setTimeout(function () {
      let data= {
        activity_id: Number(activity_id),
        openid: OPENID,
        message_content: e.detail.value.text,
         message_img: that.data.itemsImg,
        }
        console.log(data)
      wx.request({
        url: `${app.globalData.ROOT_URL}message/create/`,
        method: 'POST',
        data:data,
        success(res) {
          console.log(res)
          
          wx.redirectTo({
            url: '/pages/activeDetail/activeDetail?id='+activity_id,
          })
        }
      })

    },500)

  },
  

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    activity_id = options.id;
    console.log(activity_id)
    //that.leaveWord(options.id);

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