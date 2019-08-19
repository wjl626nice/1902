// pages/load/load.js
var app = getApp();

Page({

    /**
     * 页面的初始数据
     */
    data: {
        logo: '',
        name: ''
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function(options) {
        this.getEnterLogo();
        app.setBarColor();
    },
    // 获取小程序的logo和名字
    getEnterLogo: function() {
        var that = this;
        wx.request({
            url: app.globalData.url + '/routine/get_site_info',
            method: 'post',
            dataType  : 'json',
            success: function(res) {
                that.setData({
                    logo: res.data.data.logo,
                    name: res.data.data.name
                })
            }
        })
    },
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function() {

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
                                    // 把用户id设置到全局data中
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