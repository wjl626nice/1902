  // pages/addActive/addActive.js
var util = require('../../utils/util.js');  
//获取应用实例
const app = getApp()
const ROOT_URL = app.globalData.ROOT_URL;
const OPENID = wx.getStorageSync('openid');
var date = new Date();
var currentHours = date.getHours();
var currentMinute = date.getMinutes();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    num: 0,
    items: '',
    itemsImg:[],
    checkIsShow: wx.getStorageSync('checkIsShow'),
    //display: 'inline-block',
    redisplay: 'none',
    display: [['inline-block', 'none'], ['inline-block', 'none'], ['inline-block', 'none'], ['inline-block', 'none'], ['inline-block', 'none'] ],

    dates: ['',''],
    
    startDate: "",

    multiArray: [[], [], []],
    multiIndex: [0, 0, 0],
    
    //地点
    address:'',
    alladdress:'',
    //活动类型
    arrayType: ['散踢', '队内活动',"球队比赛"],
    //活动规则
    arrayRule: ['待定','5人制', '6人制', '7人制', '8人制', '9人制', '10人制', '11人制'],
    //设置input标签是否禁用
    status1: false,
    status2: false,

    //input内容
    numLow: '',
    numUp: '',
    timeLimitTime:'',
    timeQuitTime:'',
    money:'',
    text: '',

  
  },
  userInput: function (e) {
    this.setData({
      num: e.detail.cursor
    })
  },
  //选择本地图片
  Uploadimg: function (e) {
    var that = this;
    wx.chooseImage({
      count: 6,  //最多可以选择的图片总数  
      sizeType: ['original', 'compressed'],// 可以指定是原图还是压缩图，默认二者都有 
      success: function (res) {
        //console.log(res.tempFilePaths);
        that.setData({
          items: res.tempFilePaths
        })
        for (var i = 0; i < that.data.items.length; i++) {
          wx.uploadFile({
            url: `${ROOT_URL}activity/file/`,
            filePath: that.data.items[i],
            name: 'img',
            success: function (res) {
              var data = JSON.parse(res.data);
              that.data.itemsImg.push(data.data.path_list[0]);
              
            }
          })
        }
      }
    })
  },
  
  //获取地理位置
  getLocation: function (e) {
    var that = this;
    wx.getLocation({
      type: 'gcj02',
          success:function(res){
            wx.chooseLocation({
              success: function(res) {
                console.log(res.address+res.name)
                var endisplay = that.data.display;
                for (var i = 1;i<2;i++) {
                  for (var j = 0; j < 2; j++) {
                    if (j == 0) endisplay[i][j] = 'none';
                    if (j == 1) endisplay[i][j] = 'inline-block';
                  }
                }
                that.setData({
                  address: res.name,
                  alladdress: res.address+res.name,
                  display:endisplay,
                })
              },
          
        })
      },
      fail: function () {
        wx.showModal({
          title: '提示',
          content: '拒绝授权可能会影响部分功能使用，请删除小程序或设置授权',
          confirmText: '去设置',
          success: res => {
            if (res.confirm) {
              wx.openSetting({

              })
            }
          }
        })
      }
    })
  },
  //获取活动类型
  bindPickerType: function (e) {
    var that = this;
    var endisplay = that.data.display;
    for (var i = 2; i < 3; i++) {
      for (var j = 0; j < 2; j++) {
        if (j == 0) endisplay[i][j] = 'none';
        if (j == 1) endisplay[i][j] = 'inline-block';
      }
    }
    that.setData({
      index: e.detail.value,
      display: endisplay,
    })
  },
  //获取赛制 
  bindPickerRule: function (e) {
    var that = this;
    var endisplay = that.data.display;
    for (var i = 3; i < 4; i++) {
      for (var j = 0; j < 2; j++) {
        if (j == 0) endisplay[i][j] = 'none';
        if (j == 1) endisplay[i][j] = 'inline-block';
      }
    }
    that.setData({
      index1: e.detail.value,
      display: endisplay,
    })
  },


  switchChange1: function (e) {
    var that = this;
    that.setData({
      status1: e.detail.value,
    })

  },
  switchChange2: function (e) {
    var that = this;
    
      that.setData({
        status2: e.detail.value,
      })
    
  },


 
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var up = "display[" + 0 + "][[" + 0 + "]";
    var down = "display[" + 0 + "][[" + 1 + "]";
    this.setData({
      up: 'none',
      down: 'inline-block'
    })
    
  },

  //删除图片
  deleteImg: function(e){
    let that = this;
    let imgs = that.data.items;
    let imgs1 = that.data.itemsImg;
    imgs.splice(e.currentTarget.dataset.index,1);
    imgs1.splice(e.currentTarget.dataset.index, 1);
    that.setData({
      items: imgs,
      itemsImg:imgs1,
    })
    
  },

  //空值判断
  isempty: function (res, name) {
    console.log(res+"@");
    if (res == ''||res==null) {
      console.log("1")
      wx.showToast({
        title: name + "不能为空！",
      })
      return;
    }
  },
  //提交表单
  formSubmit: function(e){
    var that = this;
    if (e.detail.value.time == '') {
      wx.showToast({
        title: '请填写活动时间',
      })
      return false;
    }
    if (that.data.alladdress == '') {
      wx.showToast({
        title: '请填写地点',
      })
      return false;
    }
    if (e.detail.value.type == '') {
      wx.showToast({
        title: '请填写活动类型',
      })
      return false;
    }
    if (e.detail.value.rule == '') {
      wx.showToast({
        title: '请填写赛制',
      })
      return false;
    }
    if (e.detail.value.numLow == '') {
      wx.showToast({
        title: '请填写人数下限',
      })
      return false;
    }
    if (Number(e.detail.value.numLow) > 100) {
      wx.showToast({
        title: '超出人数下限',
      })
      return false;
    }
    if (e.detail.value.numUp == '') {
      wx.showToast({
        title: '超出人数上限',
      })
      return false;
    }
    if (Number(e.detail.value.numUp) > 100) {
      wx.showToast({
        title: '超出人数上线',
      })
      return false;
    }
    if (Number(e.detail.value.numUp) < Number(e.detail.value.numLow)) {
      wx.showToast({
        title: '人数上限不合法',
      })
      return false;
    }
    
    if (e.detail.value.timeLimitTime == '' && e.detail.value.timeLimit==true) {
      wx.showToast({
        title: '限时报名时限',
      })
      return false;
    }
    if (e.detail.value.timeQuitTime == '' && e.detail.value.timeQuit==true) {
      wx.showToast({
        title: '限时无责时限',
      })
      return false;
    }
    
   

    var address = that.data.alladdress
    var proIndex = address.indexOf('省')
    var province = address.substring(0,proIndex+1);
    console.log(province)
    var cityIndex = address.indexOf('市')
    var city = address.substring(proIndex+1, cityIndex + 1);
    console.log(city)
    var quIndex = address.indexOf('区')
    if (quIndex == -1)
      quIndex = address.indexOf('县')
    console.log(cityIndex + "@" + quIndex)
    var qu = address.substring(cityIndex + 1, quIndex + 1);
    console.log(qu)
    var detail = address.substring(quIndex + 1);
    console.log(detail)

    //时间转时间戳
    var oldtime = that.data.startDate;
    console.log(oldtime);
    var oldyear = util.formatTime(date).substring(0,4);
    var tt = oldtime.match(/(\w+)/g);
    if (Number(tt[0]) == 1 && Number(tt[1]) < 29 && Number(oldyear)==2018){
      oldyear = (Number(oldyear)+1);
    }
    if (tt[0].length==1){
      tt[0] = "0"+tt[0];
    }
    if (tt[1].length==1) {
      tt[1] = "0" + tt[1];
    }
    var newdate = oldyear + "-" + tt[0] + "-" + tt[1] + " "+tt[2]+":"+tt[3]+":"+"00";
    console.log(newdate);
    var timestamp = new Date(newdate.replace(/-/g, "/")).getTime() / 1000;
    console.log(timestamp);

    //限时报名和限时取消无责 转时间戳
    if (typeof (e.detail.value.timeLimitTime) == "undefined")
      e.detail.value.timeLimitTime = 0;
    if (typeof (e.detail.value.timeQuitTime) == "undefined")
      e.detail.value.timeQuitTime = 0;
    var limit_time = timestamp - 3600 * Number(e.detail.value.timeLimitTime);
    var irres_time = timestamp - 3600 * Number(e.detail.value.timeQuitTime);

    var data=
    {
      activity_time: timestamp,
        openid: OPENID,
          address_province: province,
            address_city: city,
              address_area: qu,
                address_detailed: detail,
                  formater: that.data.index1,
                    'type': that.data.index,
                      'upper_limit': Number(e.detail.value.numUp),
                        'lower_limit': Number(e.detail.value.numLow),
                          'is_limit': Number(e.detail.value.timeLimit),
                            'limit_time': limit_time,
        'price': e.detail.value.money ? Number(e.detail.value.money) : 0,
                                'activity_img': that.data.itemsImg,
                                  'is_irres': Number(e.detail.value.timeQuit),
                                    'irres_time': irres_time,
                                      'notice': e.detail.value.text,
          
      };
      console.log(data)
      
    wx.request({
      url: `${ROOT_URL}activity/create/`,
      method: 'POST',
      data: 
      {
          'activity_time': timestamp,
          "openid": OPENID,
          'address_province': province,
          'address_city': city,
          'address_area': qu,
          'address_detailed': detail,
          'formater': that.data.index1,
          'type': that.data.index,
          'upper_limit': Number(e.detail.value.numUp),
          'lower_limit': Number(e.detail.value.numLow),
          'is_limit': Number(e.detail.value.timeLimit),
          'limit_time': limit_time,
          'price': Number(e.detail.value.money),
          'activity_img': that.data.itemsImg,
          'is_irres': Number(e.detail.value.timeQuit),
          'irres_time': irres_time,
          'notice': e.detail.value.text,
          
      },
      success: (res) => {
        console.log(res)
        wx.showToast({
        title: '提交成功',
      })

      that.setData({
        num: 0,
        items: '',
        itemsImg: [],

        display: 'inline-block',
        redisplay: 'none',
        display: [['inline-block', 'none'], ['inline-block', 'none'], ['inline-block', 'none'], ['inline-block', 'none'], ['inline-block', 'none']],

        dates: ['', ''],

        startDate: "",

        multiArray: [[], [], []],
        multiIndex: [0, 0, 0],

        //地点
        address: '',
        alladdress: '',
        //活动类型
        arrayType: ['散踢', '队内活动', "球队比赛"],
        //活动规则
        arrayRule: ['待定', '5人制', '6人制', '7人制', '8人制', '9人制', '10人制', '11人制'],
        //设置input标签是否禁用
        status1: false,
        status2: false,
        numLow: '',
        numUp: '',
        timeLimitTime: '',
        timeQuitTime: '',
        money: '',
        text: '',
      })
      setTimeout(function () {
      wx.switchTab({
         url: '/pages/home/home',
       })
      }, 1000)
      }
    })

  },
  pickerTap: function () {
    date = new Date();

    var monthDay = ['今天', '明天'];
    var hours = [];
    var minute = [];

    currentHours = date.getHours();
    currentMinute = date.getMinutes();

    // 月-日
    for (var i = 2; i <= 28; i++) {
      var date1 = new Date(date);
      date1.setDate(date.getDate() + i);
      var md = (date1.getMonth() + 1) + "-" + date1.getDate();
      monthDay.push(md);
    }

    var data = {
      multiArray: this.data.multiArray,
      multiIndex: this.data.multiIndex
    };

    if (data.multiIndex[0] === 0) {
      if (data.multiIndex[1] === 0) {
        this.loadData(hours, minute);
      } else {
        this.loadMinute(hours, minute);
      }
    } else {
      this.loadHoursMinute(hours, minute);
    }

    data.multiArray[0] = monthDay;
    data.multiArray[1] = hours;
    data.multiArray[2] = minute;

    this.setData(data);
  },




  bindMultiPickerColumnChange: function (e) {
    date = new Date();

    var that = this;

    var monthDay = ['今天', '明天'];
    var hours = [];
    var minute = [];

    currentHours = date.getHours();
    currentMinute = date.getMinutes();

    var data = {
      multiArray: this.data.multiArray,
      multiIndex: this.data.multiIndex
    };
    // 把选择的对应值赋值给 multiIndex
    data.multiIndex[e.detail.column] = e.detail.value;

    // 然后再判断当前改变的是哪一列,如果是第1列改变
    if (e.detail.column === 0) {
      // 如果第一列滚动到第一行
      if (e.detail.value === 0) {

        that.loadData(hours, minute);

      } else {
        that.loadHoursMinute(hours, minute);
      }

      data.multiIndex[1] = 0;
      data.multiIndex[2] = 0;

      // 如果是第2列改变
    } else if (e.detail.column === 1) {

      // 如果第一列为今天
      if (data.multiIndex[0] === 0) {
        if (e.detail.value === 0) {
          that.loadData(hours, minute);
        } else {
          that.loadMinute(hours, minute);
        }
        // 第一列不为今天
      } else {
        that.loadHoursMinute(hours, minute);
      }
      data.multiIndex[2] = 0;

      // 如果是第3列改变
    } else {
      // 如果第一列为'今天'
      if (data.multiIndex[0] === 0) {

        // 如果第一列为 '今天'并且第二列为当前时间
        if (data.multiIndex[1] === 0) {
          that.loadData(hours, minute);
        } else {
          that.loadMinute(hours, minute);
        }
      } else {
        that.loadHoursMinute(hours, minute);
      }
    }
    data.multiArray[1] = hours;
    data.multiArray[2] = minute;
    this.setData(data);
  },

  loadData: function (hours, minute) {

    var minuteIndex;
    if (currentMinute > 0 && currentMinute <= 10) {
      minuteIndex = 10;
    } else if (currentMinute > 10 && currentMinute <= 20) {
      minuteIndex = 20;
    } else if (currentMinute > 20 && currentMinute <= 30) {
      minuteIndex = 30;
    } else if (currentMinute > 30 && currentMinute <= 40) {
      minuteIndex = 40;
    } else if (currentMinute > 40 && currentMinute <= 50) {
      minuteIndex = 50;
    } else {
      minuteIndex = 60;
    }

    if (minuteIndex == 60) {
      // 时
      for (var i = currentHours + 1; i < 24; i++) {
        hours.push(i);
      }
      // 分
      for (var i = 0; i < 60; i += 10) {
        minute.push(i);
      }
    } else {
      // 时
      for (var i = currentHours; i < 24; i++) {
        hours.push(i);
      }
      // 分
      for (var i = minuteIndex; i < 60; i += 10) {
        minute.push(i);
      }
    }
  },

  loadHoursMinute: function (hours, minute) {
    // 时
    for (var i = 0; i < 24; i++) {
      hours.push(i);
    }
    // 分
    for (var i = 0; i < 60; i += 10) {
      minute.push(i);
    }
  },

  loadMinute: function (hours, minute) {
    var minuteIndex;
    if (currentMinute > 0 && currentMinute <= 10) {
      minuteIndex = 10;
    } else if (currentMinute > 10 && currentMinute <= 20) {
      minuteIndex = 20;
    } else if (currentMinute > 20 && currentMinute <= 30) {
      minuteIndex = 30;
    } else if (currentMinute > 30 && currentMinute <= 40) {
      minuteIndex = 40;
    } else if (currentMinute > 40 && currentMinute <= 50) {
      minuteIndex = 50;
    } else {
      minuteIndex = 60;
    }

    if (minuteIndex == 60) {
      // 时
      for (var i = currentHours + 1; i < 24; i++) {
        hours.push(i);
      }
    } else {
      // 时
      for (var i = currentHours; i < 24; i++) {
        hours.push(i);
      }
    }
    // 分
    for (var i = 0; i < 60; i += 10) {
      minute.push(i);
    }
  },

  bindStartMultiPickerChange: function (e) {
    var that = this;
    var monthDay = that.data.multiArray[0][e.detail.value[0]];
    var hours = that.data.multiArray[1][e.detail.value[1]];
    var minute = that.data.multiArray[2][e.detail.value[2]];

    if (monthDay === "今天") {
      var month = date.getMonth() + 1;
      var day = date.getDate();
      monthDay = month + "月" + day + "日";
    } else if (monthDay === "明天") {
      var date1 = new Date(date);
      date1.setDate(date.getDate() + 1);
      monthDay = (date1.getMonth() + 1) + "月" + date1.getDate() + "日";

    } else {
      var month = monthDay.split("-")[0]; // 返回月
      var day = monthDay.split("-")[1]; // 返回日
      monthDay = month + "月" + day + "日";
    }
    if (hours < 10) {
      hours = '0' + hours;
    }
    if (minute < 10) {
      minute = '0' + minute;
    }
    var startDate = monthDay + " " + hours + ":" + minute;
    var endisplay = that.data.display;
    for (var i = 0; i < 1; i++) {
      for (var j = 0; j < 2; j++) {
        if (j == 0) endisplay[0][0] = 'none';
        if (j == 1) endisplay[0][1] = 'inline-block';
      }
    }
    that.setData({
      startDate: startDate,
      display: endisplay,
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
  
  },
 
}) 