// pages/myWallet/myWallet.js
const APP = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userBalance: 0,//账户余额
    isShow: false,
    isbank:'1',//账户是否绑定银行卡，1绑定，0未绑定,
    cardholder: '', //持卡人
    bank_card_number:'',
    ID_number: '',
    withdraw: '',
  },
  myWallet:function(){
    var that=this
    if(that.data.isbank==1){
      that.setData({
        isShow: true
      })
    }else{
      wx.navigateTo({
        url: '/pages/bindCard/bindCard',
      })
    }
    
  },

  //充值
  recharge:function(){
    wx.navigateTo({
      url: '/pages/recharge/recharge',
    })
  },
  changeInputVal(e) {
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
    // 只能输入数字
    this.setData({
      withdraw: val
    })
  },
  //获取用户银行卡信息
  getUserBankInfo: function () {
  
  wx.request({
    url: APP.globalData.ROOT_URL + '/put_forward/getInfo/',
    method: 'POST',
    data: {
      openid: wx.getStorageSync('openid'),
    },
    success: (res) => {
      if(res['data']['code'] === 0){
        const bankData = res['data']['data'];
        this.setData({
          ID_number: bankData.ID_number.replace(/(\d{4})(\d{10})(\d{4})/, '$1**********$3'),
          cardholder: bankData.cardholder,
          bank_card_number: bankData.bank_card_number.slice(-4, 18),
        })
      }
    }
    
  })
  },
  //交易明细
  tradeDetail:function(){
    wx.navigateTo({
      url: '/pages/tradeDetail/tradeDetail',
    })
  },
  //取消事件
  cancelButton:function(){
    var that=this;
    that.setData({
      isShow:false
    })
  },
  //确认事件
  confirmButton:function(){
    var that = this;
    that.setData({
      isShow:false
    })
    wx.request({
      url: APP.globalData.ROOT_URL + '/put_forward/createPutForward/',
      method: 'POST',
      data: {
        openid: wx.getStorageSync('openid'),
        pay_amount: this.data.withdraw,
        pay_state: 2,
      },
      success: (res) => {
          if(res['data']['code']===0){
            wx.showToast({
              title: '提现申请已提交',
              icon: 'none'
            })
          }else {
            wx.showToast({
              title: res['data']['msg'],
              icon: 'none'
            })
          }
      },
      error: (err) => {
        
          wx.showToast({
            title: '网络错误,请检查网络',
            icon: 'none'
          })
      },
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // wx.request({
    //   url: `${APP.gloabData.ROOT_URL}`,
    // })
    let user = wx.getStorageSync("userInfo");
    this.getUserBankInfo()
    this.setData({
      userBalance:user.balance,
    })
    if(user.opening_bank==''){
      this.setData({
        isbank: 0
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