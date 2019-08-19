//app.js
App({
  onLaunch: function () {
    // 登录
    

    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
         this.setUserInfo();
        }else{
          wx.reLaunch({
            url: '/pages/login/login',
          })
        }
      }
    })
    this.checkIsShowFun();
  },

  setUserInfo:function(){
    var that=this;
      
    if(this.globalData.userInfo==null){
     
    wx.login({
      success: res => {
        console.log(res)
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        wx.request({
          url: `${that.globalData.ROOT_URL}member/userGetOpenID/`,
          data: {
            code: res['code']
          },
          method: 'POST',
          success: res => {
            if (res['statusCode'] === 200) {
              wx.setStorageSync('openid', res.data.data.openid);
              wx.getUserInfo({
                withCredentials: true,
                success: function (res_user) {               
                  wx.setStorageSync('userInfo', res_user.userInfo);
                  // console.log(res_user)
                  wx.request({
                    url: `${that.globalData.ROOT_URL}member/member/`,
                    method: 'GET',
                    data: {
                      openid: res.data.data.openid,
                      avatar: res_user.userInfo.avatarUrl,
                      nickname: res_user.userInfo.nickName
                    },
                    header: {
                      'content-type': 'json'
                    },
                    success: function (datas) {
                      console.log(datas)
                      wx.setStorageSync('myid', datas.data.data.id)
                    }
                  });

                }
              })
            }
          }
        })
      }
    })
    }
  },
  checkIsShowFun: function() {
    const that = this;
    wx.request({
      url: `${this.globalData.ROOT_URL}member/boolean/`,
      method: 'GET',
      success: function (datas) {
        let val = datas.data.data.is_auditing == 0 ? true : false;
        console.log(val,'1111111');
        wx.setStorageSync('checkIsShow', val )

      }
    })
  },
  getMediaId:function(){

  },
  globalData: {
    userInfo: null,

    ROOT_URL: 'https://rimetleague.com/',
  }
  
})