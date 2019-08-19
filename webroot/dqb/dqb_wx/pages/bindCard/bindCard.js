// pages/bindCard/bindCard.js
const APP = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
  //是否为空
  isempty: function (res, name) {
    if (res == '') {
      wx.showToast({
        title: name + "不能为空！",
        icon: 'none'
      })
      return 1;
    }
  },
  //手机号合格
  istel:function (tel) {
    if(!tel == /^1[34578]\d{9}$/.test(tel)) {
      wx.showToast({
        title: '输入手机号格式不正确！',
        icon: "none"
      })
      return 1;
    }
  },

  //验证身份证是否合法
  idCardValid: function (idcard) {
    var city = { 11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古", 21: "辽宁", 22: "吉林", 23: "黑龙江 ", 31: "上海", 32: "江苏", 33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南", 42: "湖北 ", 43: "湖南", 44: "广东", 45: "广西", 46: "海南", 50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏 ", 61: "陕西", 62: "甘肃", 63: "青海", 64: "宁夏", 65: "新疆", 71: "台湾", 81: "香港", 82: "澳门", 91: "国外 " }
    if (!idcard == /^\d{6}(19|20)?\d{2}(0[1-9]|1[12])(0[1-9]|[12]\d|3[01])\d{3}(\d|X)$/i.test(idcard)) {
      wx.showToast({
        title: '身份证号格式错误！',
        icon: 'none'
      });
      return 1;
    } else if (!city[idcard.substr(0, 2)]) {
      wx.showToast({
        title: '地址编码错误',
        icon: 'none'
      })
      return 1;
    }
  },
  bindButton:function(e){
    // e.detail.value.cardName,
    if(
    this.isempty(e.detail.value.cardName,"持卡人")==1||
      this.isempty(e.detail.value.idCard, "身份证")==1||
      this.isempty(e.detail.value.cardNumber, "银行卡号") == 1 ||
      this.isempty(e.detail.value.pretel, "银行预留手机号") == 1 ||
      this.isempty(e.detail.value.cardBank, "开户行") == 1||
    this.istel(e.detail.value.pretel)==1||
    this.idCardValid(e.detail.value.idCard)==1
    ){return false}
    wx.request({
      url: `${APP.globalData.ROOT_URL}/put_forward/get_bank/`,
      method: "POST",
      data: {
        cardNo: e.detail.value.cardNumber
      },
      success: (res_b) => {
        if (res_b["data"]["code"]==0){
          wx.request({
            url: `${APP.globalData.ROOT_URL}/put_forward/getInfo/`,
            method: "POST",
            data: {
              openid: wx.getStorageSync("openid"),
              cardholder: e.detail.value.cardName,//持卡人
              ID_number: e.detail.value.idCard,//身份证
              bank_card_number: e.detail.value.cardNumber,//银行卡号
              reserved_phone_number: e.detail.value.pretel,//银行预留手机号 
              opening_bank: e.detail.value.cardBank//开户行
            },
            success: (res) => {
              console.log(res)
              if(res["data"]["code"]==0){
                wx.showToast({
                  title: "成功！",
                  icon: 'none',
                })
                let pages = getCurrentPages();
                let prevPage = pages[pages.length - 2];
                prevPage.setData({
                  isbank: 1
                })
                wx.navigateBack({
                  delta: 1
                })
              }else{
                wx.showToast({
                  title: `${res.data.msg}`,
                  icon:'none'
                })
              }
            }
          })
        }else{
          wx.showToast({
            title: `${res_b.data.msg}`,
            icon:"none"
          })
        }
      }
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