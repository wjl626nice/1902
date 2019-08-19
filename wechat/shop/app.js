//app.js
App({
    onLaunch: function() {
        // 通过接口获取后台的配置来设置 小程序导航
        this.getRoutineStyle();
    },
    globalData: {
        url: 'http://www.xuxin.com:5000',
        routineStyle: '#000',
        // 登录成功的用户id
        uid: '',
        // 登录成功以后 跳转的地址
        openPages: ''
    },
    // 设置导航样式
    setBarColor: function() {
        var that = this;
        // 更新小程序导航栏样式
        wx.setNavigationBarColor({
            frontColor: '#ffffff',
            backgroundColor: that.globalData.routineStyle,
        })
    },
    // 通过接口获取后台的设置导航栏样式
    getRoutineStyle: function() {
        var that = this;
        wx.request({
            url: that.globalData.url + '/routine/get_routine_style',
            method: 'post',
            dataType  : 'json',
            success: function(res) {
                // 把后台获取的样式设置全局样式中
                that.globalData.routineStyle = res.data.data.routine_style;
                that.setBarColor();
            }
        })
    },
    // 检测是否已经登录
    check_login: function() {
        if (this.globalData.uid == null) { //是否存在用户信息，如果不存在跳转到首页
            wx.showToast({
                title: '用户信息获取失败',
                icon: 'none',
                duration: 1500,
            })
            setTimeout(function() {
                wx.navigateTo({
                    url: '/pages/load/load',
                })
            }, 1500)
        }
    },
})