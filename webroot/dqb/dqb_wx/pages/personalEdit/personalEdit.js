// pages/personalEdit/personalEdit.js
const APP=getApp();
const openid = wx.getStorageSync('openid')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    img:'',//头像src
    media_id:'',//头像地址
    nickname:'', //昵称
    age:"",//年龄
    is_age:true,
    profession:"",
    is_profession:true,//行业
    tel:"",//手机号
    array:['10','11','12','13','14','15','16','17','18','19','20'],//年龄
    hy_array:['行业1','行业2','行业3'],//行业内容
    index:'',//年龄数组下标
    hy_index:''  //行业数组下标
  },
  //手机号是否正确验证函数
  
  //年龄选择
  bindPickerChange:function(res){
    this.setData({
      index: res.detail.value,
      is_age:false
    })
  },
  //行业选择
  hyPickerChange:function(res){
    this.setData({
      hy_index: res.detail.value,
      is_profession:false
    })
  },
  //上传头像
  Uploadimg: function (e) {
    var that = this;
    wx.chooseImage({
      count: 1,  //最多可以选择的图片总数  
      sizeType: ['original', 'compressed'],// 可以指定是原图还是压缩图，默认二者都有 
      success: function (res) {
        console.log(res)
        wx.showLoading({
          title: '',
          icon: 'none'
        })
         that.setData({
           img:res.tempFilePaths[0]
         })
        that.imgupload(res.tempFilePaths,0)
        setTimeout(function () {
          wx.hideLoading();
        },1000);
      }
    })
  },
  imgupload: function (tempFilePaths,i) {
      var that = this;
      var tmppath = tempFilePaths[i];
      wx.uploadFile({
        url: `${APP.globalData.ROOT_URL}activity/file/`,
        filePath: tmppath,
        name: 'img',
        formData: {
        },
        success: function (res) {
           var datas = JSON.parse(res.data);
           that.setData({
             media_id:datas.data.path_list[0]
           })
            console.log(datas)

        }
      })
    },
  
  //空值判断
  isempty:function(res,name){
    if(res==''){
      wx.showToast({
        title: name+"不能为空！",
        icon:'none'
      })
      return false;
    }
  },
  //提交表单事件
  sumbit: function (res) {
    var that = this;
    that.setData({    
      tel: res.detail.value.tel,
      age: that.data.array[that.data.index],
      profession: that.data.hy_array[that.data.hy_index]
    })
    let user = wx.getStorageSync("userInfo")
    let openid=wx.getStorageSync("openid");
    // let age = that.data.array[that.data.index]
    // let profession = that.data.hy_array[that.data.hy_index]
    if(that.data.index==""){
      that.setData({
        age:user.age
      })
    }
    if(that.data.hy_index==""){
      that.setData({
        profession: user.profession
      }) 
    }
    if (res.detail.value.tel==""){
      wx.showToast({
        title: '请填写手机号！',
        icon:"none"
      })
      return false;
    }
     function istel(tel) {
      if (!tel == /^1[34578]\d{9}$/.test(tel)) {
        wx.showToast({
          title: '输入手机号格式不正确！',
          icon: "none"
        })
        return 1;
      }
    }
    let ist=istel(res.detail.value.tel);
    if(ist=="1"){
      return false;
    }
    wx.request({
      url: `${APP.globalData.ROOT_URL}member/changeMemberInfo/`,
      method:'POST',
      data:{
        openid:openid,
        avatar:that.data.media_id,
        age:that.data.age,
        profession: that.data.profession,
        phonenum:that.data.tel
      },
      success(e){
        console.log(e)
        wx.switchTab({
          url: '/pages/mine/mine',
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    var userInfo = wx.getStorageSync('userInfo');
    if(userInfo.age="null"){
      userInfo.age=""
    }
    that.setData({
      img: userInfo.avatar,
      nickname:userInfo.nickname,
      age:userInfo.age,
      profession:userInfo.profession,
      tel:userInfo.phonenum
    })
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