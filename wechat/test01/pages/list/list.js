// pages/list/list.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
      ab: 'abc',
      num: 0,
      some: {"subfiled":1212},
      arr:[1,2,3,4,5,6]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var test_component_obj = this.selectComponent('.test')
    console.log(test_component_obj) 
  },
  changeNum: function(){
    var num = ++this.data.num
    this.setData({
      num: num
    })
  },
  changeAb: function(){
    console.log(this)
    // 获取当前data数据
    console.log(this.data.ab)
    this.setData({
      ab: 'aabb'
    })
    // var aaaa = () => {
    //   console.log(this)
    // }
    // aaaa()
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

  },
  getNumber: function(e){
    console.log('ok')
    console.log(e)
  }
})