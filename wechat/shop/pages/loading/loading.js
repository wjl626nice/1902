// pages/loading/loading.js
var app = getApp();

Page({

    /**
     * 页面的初始数据
     */
    data: {

    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function(options) {
        // 设置导航栏样式
        app.setBarColor();
        // 访问小程序 检测之前是否已经授权过
        this.setSetting();
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function() {

    },
    setSetting: function() {
        var that = this;
        // 检测之前是否已经授权过
        wx.getSetting({
            // wx.getSetting 执行成功回调  success，  res中包含执行的结果（wx.getSetting执行的结果）
            success(res) {
                // 结果是否之前已经授权过 获取用户信息
                if (!res.authSetting['scope.userInfo']) {
                    // 跳转到对应页面
                    wx.navigateTo({
                        url: '/pages/load/load',
                    })
                } else {
                    that.getUserInfo();
                }
            }
        })
    },
    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function() {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function() {

    },
    // 当用户授权以后回调  获取用户信息
    getUserInfo: function() {
        var that = this;
        wx.getUserInfo({
            // 获取的用户信息用中文标识
            lang: 'zh_CN',
            // 当 wx.getUserInfo 执行成功以后 回调success方法
            success: function(res) {
                // 用户信息 昵称 头像
                var userInfo = res.userInfo
                    // 获取code 通过code获取openid
                wx.login({
                    success: function(res) {
                        if (res.code) {
                            userInfo.code = res.code;
                            // 发起网络请求
                            wx.request({
                                url: app.globalData.url + '/routine/login',
                                method: 'post',
                                dataType  : 'json',
                                data: {
                                    info: userInfo
                                },
                                success: function(res) {
                                    app.globalData.uid = res.data.data.uid;
                                    if (app.globalData.openPages != '' && app.globalData.openPages != undefined) { //跳转到指定页面
                                        wx.navigateTo({
                                            url: app.globalData.openPages
                                        })
                                    } else { //跳转到首页
                                        wx.reLaunch({
                                            url: '/pages/index/index'
                                        })
                                    }
                                },
                            })
                        } else {
                            console.log('登录失败！' + res.errMsg)
                        }
                    },
                    fail: function() {},
                })
            },
            fail: function() {},
        })
    },
})