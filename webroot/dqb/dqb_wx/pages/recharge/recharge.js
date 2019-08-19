const APP = getApp();
const ROOT_URL = APP.globalData.ROOT_URL;
// pages/recharge/recharge.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    activeIndex: -1,//默认选中第一个
    numArray: [10, 20, 30, 50, 100, 200],
    price: '',
  },
  activethis: function (event) {//点击选中事件
    const index = event.currentTarget.dataset.index;//当前index
    this.setData({
      activeIndex: index,
      price: this.data.numArray[index]
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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
  inputeidt: function (e) {
    let val = e.detail.value;
    // 先把非数字的都替换掉，除了数字和.
    val = val.replace(/[^\d.]/g, '');
    // 必须保证第一个为数字而不是.
    val = val.replace(/^\./g, '');
    // 保证只有出现一个.而没有多个.
    val = val.replace(/\.{2,}/g, '.');
    // 保证.只出现一次，而不能出现两次以上
    val = val.replace('.', '$#$').replace(/\./g, '').replace('$#$', '.');
    // 保证.只后面只能出现两位有效数字
    val = val.replace(/([0-9]+\.[0-9]{2})[0-9]*/, '$1');
   this.setData({
     price : val,
     activeIndex:-1,
   })
  },
  recharge: function() {
    console.log(this.data.price)
    if(this.data.price>3000){
      wx.showToast({
        title: '单笔不能超过3000元！',
        icon:"none"
      })
      return false
    }
    wx.request({
      url: `${APP.globalData.ROOT_URL}recharge/rechargePay/`,
      method: 'POST',
      data: {
        openid: wx.getStorageSync("openid"),
        price: Number(this.data.price),
      },
      success: (res) => {
        if(res['data']['code'] === 0 ){
          const payData = res['data']['data'];
          wx.requestPayment({
            timeStamp: payData['timeStamp'],
            nonceStr: payData['nonceStr'],
            package: payData['package'],
            signType: 'MD5',
            paySign: payData['paySign'],
            success:  (res) => { 
              console.log(res);
            },
            fail:  (res) =>  { console.log(res)},
            complete: (res) =>  {console.log(res) }
          })
        }
          // console.log(res);
      }
    })
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