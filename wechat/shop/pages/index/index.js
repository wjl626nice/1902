//index.js
//获取应用实例
const app = getApp()

Page({
    data: {
        indicatorDots: true, //是否显示面板指示点;
        autoplay: true, //是否自动播放;
        interval: 3000, //动画间隔的时间;
        duration: 500, //动画播放的时长;
        indicatorColor: "rgba(51, 51, 51, .3)",
        indicatorActivecolor: "#ffffff",
        imgUrls: [],
    },
    //事件处理函数
    bindViewTap: function() {
        wx.navigateTo({
            url: '../logs/logs'
        })
    },
    onLoad: function() {
        // 当访问小程序首页时 ，检测是否登录，没有登录跳转到 授权登录页
        app.check_login();
        // 获取小程序首页 需要的数据
        this.getIndexInfo();
    },
    getIndexInfo: function() {
        var header = {
            'content-type': 'application/x-www-form-urlencoded',
        };
        var that = this;
        wx.request({
            url: app.globalData.url + '/routine/index?uid=' + app.globalData.uid,
            method: 'POST',
            header: header,
            success: function(res) {
                that.setData({
                    imgUrls: res.data.data.banner,
                    // recommendLsit: res.data.data.best,
                    // newList: res.data.data.new,
                    // lovely: res.data.data.lovely,
                    // menus: res.data.data.menus,
                    // likeList: res.data.data.hot
                })
            }
        })
    },
})