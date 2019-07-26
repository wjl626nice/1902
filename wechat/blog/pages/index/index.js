//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    imageList:[
      { id: 1, imageUrl:'/static/images/1.jpg'},
      { id: 2, imageUrl: '/static/images/2.jpg' },
      { id: 3, imageUrl: '/static/images/3.jpg' },
      { id: 4, imageUrl: '/static/images/4.jpg' },
    ],
    category:[
      'Mysql','Python','Django','Css'
    ],
    currentTab: 0,
    // 页面推荐栏目的初始化数据
    all_cate_articles: [
      // mysql的文章
      [
      ],
      // python的文章
      [

      ],
      // Django文章
      [

      ],
      // Css文章
      [

      ]
    ]
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    wx.request({
      url: 'http://www.xuxin.com:8000/get_cate_articles',
      data: {cate_id:1},
      success: (data) =>{
        // 先获取初始化的栏目数据
        var all_cate_articles = this.data.all_cate_articles
        // 修改栏目数据
        all_cate_articles[0] = data.data
        // 更新状态监控模式下的 all_cate_articles
        this.setData({
          all_cate_articles: all_cate_articles
        })
      }
    })
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  // 跳转到详情页（文章页）
  showDetail: function(e){
    console.log(e)
    console.log(e.currentTarget.dataset.id)
    // 获取了文章id
    var id = e.currentTarget.dataset.id
    // 跳转到详情页，展示文章
    wx.redirectTo({
      url: '/pages/show/show?id='+id,
    })
  },
  // 切换选项卡
  changeTab: function(e){
      console.log(e)
      console.log(e.currentTarget.dataset.index)
    // 获取点击的选项卡索引
    var index = e.currentTarget.dataset.index
    this.setData({
      // 改变data中的值，那么视图中调用的地方也要被更改
      currentTab: index 
    });
  },
  searchPage: (e) =>{
    console.log(e)
    // 获取页面输入的关键词
    var kw = e.detail.value
    if(!kw){
      wx.showToast({
        icon: 'none',
        title: '请输入关键词！',
      })
      return;
    }
    // 跳转到详情页，展示文章
    wx.redirectTo({
      url: '/pages/list/list?kw=' + kw,
    })
  }
})
