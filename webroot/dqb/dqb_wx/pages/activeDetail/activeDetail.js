// pages/activeDetail/activeDetail.js
var util = require('../../utils/util.js');  
var moment = require('../../utils/moment.js');  
const APP = getApp();
var date = new Date();
const ROOT_URL = APP.globalData.ROOT_URL;
var activity_id = '';
const OPENID = wx.getStorageSync('openid');
var originator_openid = '';
var Options = '';
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgs: [],
    imgUrls: [
      "../../assets/imgs/view1.jpg",
      "../../assets/imgs/view2.jpg",
      "../../assets/imgs/view3.jpg"
    ],
    openId: OPENID,
    activeOpenid: '',
    indicatordots: true,
    autoplay: true,
    interval: 5000,
    duration: 1000,
    circular: true,
    isOriginator:'',   //是否为活动创建者
    checkIsShow: wx.getStorageSync('checkIsShow'),

    //接口传参
    activity_img: '',
    activity_time: '',
    originator: '',
    notice: '',
    limit_time: '',
    irres_time: '',
    detail: '',
    formater: '',

    activityTime:'',

    useravatar:'', //用户头像


    //留言是否存在图片
    messageImg: false,

    //活动状态
    activityStatus: 0,
    endCancel:'',  //标记活动为结束还是取消

    //报名 人数
    allNum: '',
    

    arrayType: ['散踢', '队内活动', "球队比赛"],


    ispay: '',  //付费人员列表
    ispaynum:'',
    participantimgs: [],
    undeterminedimgs:[],
    leaveimgs:[],
    participant: '',//报名人员信息列表
    undetermined: '',//待定人员信息列表
    leave: '', //请假人员列表

    index:'',
    index1:'',

    //已支付人id
    ispayId:'',
    //已报名id
    participantId:'',
    //已请假id
    leaveId:'',
    //待定id
    undeterminedId:'',


    //留言
    leaveword:'',
    

  },
  avatarUrl:function (e) {
    var x = e.split('://');
    if(x.length > 1) {
     return e;
    } else {
     return ROOT_URL + e;
    }
 },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    Options = options;
    var that = this;
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    setTimeout(function () {
      that.init(options);
      that.onloadleaveword();
      wx.hideLoading();
    }, 2000)
    

  },
  init: function (options){
    var that = this;
    console.log(options.id);
    activity_id = options.id;
    wx.request({
      url: ROOT_URL + 'activity/info/',
      method: "GET",
      data: {
        pk: options.id,
      },
      success(res) {
        if (res.data.code==0){
          console.log(res)
        var data = res.data.data;
        var imgs = data.activity_img.replace(/[\[\]\s+\'\"]/g, "").split(',');
        that.setData({
          activity_img: imgs,
          activity_time: data.activity_time,
          originator: data.originator_id,
          originator_openid: data.originator_id.openid,
          activeOpenid: data.originator_id.openid,
          notice: data.notice,
          detail: data.address_detailed+'/',
          limit_time: data.limit_time,
          irres_time: data.irres_time,
          formater: data.formater,
          ispay: data.is_Pay,
          ispaynum: data.is_Pay.length,
          participant: data.participant,
          undetermined: data.undetermined,
          leave: data.leave,
          activityStatus: data.activity_state,

        })

        //判断图片是否为空 为空使用默认图片
        if (that.data.activity_img[0] == "" && that.data.activity_img.length == 1) {
          that.setData({
            imgs: that.data.imgUrls,
          })
        }
        else {
          for (var i = 0; i < that.data.activity_img.length; i++) {
            that.data.activity_img[i] = ROOT_URL + that.data.activity_img[i];
          }
          that.setData({
            imgs: that.data.activity_img,
          })
        }

        //判断赛制规则
        if (that.data.formater == 0) {
          that.setData({
            formater: "待定",
          })
        } else {
          that.setData({
            formater: (that.data.formater + 4) + "人制",
          })
        }

        //时间戳转化为时间
        var olddate = util.formatTime(new Date(that.data.activity_time * 1000));
        console.log(olddate);
        olddate = (olddate.split(" ")[0]).split("/");
        var newdate = '';
        var day = '';
        for (var i = 0; i < olddate.length; i++) {
          if (i == 0)
            day = "年";
          if (i == 1)
            day = "月";
          if (i == 2)
            day = "日";
          newdate = newdate + olddate[i] + day;
        }
        that.setData({
          activityTime: newdate,
        })
        

        //判断公告是否为空
        if (that.data.notice == null) {
          that.setData({
            notice: '暂无公告',
          })

        }

        //判断参赛名额
        if (data.formater == 0) {
          that.setData({
            allNum: "∞",
          })
        } else {
          that.setData({
            allNum: data.formater + 4,
          })
        }

        //加载报名请假待定人头像
        function avatarUrl(e) {
          var x = e.split('://');
          if (x.length > 1) {
            return e;
          } else {
            return ROOT_URL + e;
          }
        }
        var imgs = new Array();
        for (let i = 0; i < data.participant.length; i++){
          let img = avatarUrl(data.participant[i].member_id.avatar);
          imgs.push(img);
        }
        that.setData({
          participantimgs: imgs,
        })
        imgs = new Array();
        for (let i = 0; i < data.undetermined.length; i++) {
          let img = avatarUrl(data.undetermined[i].member_id.avatar);
          imgs.push(img);
        }
        that.setData({
          undeterminedimgs: imgs,
        })
        imgs = new Array();
        for (let i = 0; i < data.leave.length; i++) {
          let img = avatarUrl(data.leave[i].member_id.avatar);
          imgs.push(img);
        }
        that.setData({
          leaveimgs: imgs,
        })

        //格式化用户头像
        that.setData({
          useravatar: wx.getStorageSync("userInfo").avatarUrl,
        }) 

        //判断停止报名和无责时间
        that.setData({
          limit_time: (data.activity_time-data.limit_time)/3600,
          irres_time: (data.activity_time - data.irres_time)/3600,
        })

        //判断是否为活动组织者
        let isOriginator = true;
        if (OPENID == that.data.originator_openid) {
            isOriginator = true;
        }else{
          isOriginator = false;
        }
        that.setData({
          isOriginator: isOriginator,
          })

        //已支付人id
        let ispayId = [];
          //已报名id
        let participantId= [];
            //已请假id
        let leaveId=[];
              //待定id
        let undeterminedId= [];
      for (var i in that.data.ispay){
        ispayId.push(that.data.ispay[i].member_id.id)
      }
        for (var i in that.data.participant) {
          participantId.push(that.data.participant[i].member_id.id)
      }
        for (var i in that.data.leave) {
          leaveId.push(that.data.leave[i].member_id.id)
      }
        for (var i in that.data.undetermined) {
          undeterminedId.push(that.data.undetermined[i].member_id.id)
        }

        that.setData({
          ispayId : ispayId,
          participantId :participantId,
          leaveId: leaveId,
          undeterminedId: undeterminedId,

        })

        } else {
          wx.showToast({
            title: res['data']['msg'],
            icon: "none"
          })

        }
          
      },
      error(err) {
        wx.showToast({
          title: '网络开小差~,请检查网络',
          icon: "none"
        })
      }



    })

    //加载留言
  },
  //加载留言
  onloadleaveword:function(){
    let that = this;
    wx.request({
      url: ROOT_URL + '/message/getAll/',
      method: "GET",
      data: {
        activity: activity_id,
      },
      success(res) {
        if (res.data.code==0){
          console.log(res)
          let leaveword = res.data.data ;
          for (var i in leaveword){
            leaveword[i].add_time = moment(leaveword[i].add_time*1000).format("YYYY-MM-DD HH:mm");
            let imgs = leaveword[i].message_img.replace(/[\[\]\s+\'\"]/g, "");
            if (imgs!=""){
              imgs = imgs.split(',');
            }else{
              imgs=[];
            }
            
            for (var j in imgs){
              imgs[j] = that.avatarUrl(imgs[j]);
            }
            leaveword[i].message_img = imgs;

            leaveword[i].member_id.avatar = that.avatarUrl(leaveword[i].member_id.avatar);
            
          }
          console.log(leaveword)




          that.setData({
            leaveword: leaveword,
          })

        } else {
          wx.showToast({
            title: res['data']['msg'],
            icon: "none"
          })

        }
        
      },
      error(err) {
        wx.showToast({
          title: '网络开小差~,请检查网络',
          icon: "none"
        })
      }
    })

  },

  //留言
  leaveword: function (e) {
    var id = e.currentTarget.id;
    console.log(e)
    wx.navigateTo({
      url: '/pages/leaveWord/leaveWord?id=' + activity_id,
    })

  },

  //加载回复
  loadReply:function(e){
  

  },
 
  replyMess:function(e){
    if (e.target.dataset.memberid==wx.getStorageSync('myid')){
      wx.showToast({
        title: '无法回复本人发起的留言',
        icon: 'none'
      });
      return false;
    }
    wx.navigateTo({
      url: `/pages/replyMess/replyMess?id=${e.currentTarget.id}&memberID=${e.target.dataset.memberid}&activity_id=${activity_id}`,
    })
    // wx.navigateTo({
    //   url: '/pages/putAddActive/putAddActive?id=' + activity_id,
    // })
  },

  onShareAppMessage: function (e) {
    let user = wx.getStorageSync("userInfo")
    if (e.from === 'button') {
      // 来自页面内转发按钮
      return {
        title: user.nickName + "在点球吧请求添加为好友！",
        path: 'pages/activeDetail/activeDetail?pk=' + activity_id,// 用户点击首先进入的当前页面
        imageUrl: user.avatarUrl,
        success: function (res) {
          // 转发成功
          console.log("转发成功:");
        },
        fail: function (res) {
          // 转发失败
          console.log("转发失败:");
        }
      }

    }
  },


  signUp: function(){
    let that = this;
    let myid = wx.getStorageSync("myid");
    if (this.data.checkIsShow) {
      wx.showActionSheet({
        itemList: ['报名', '待定', '请假', '退出活动'],
        itemColor: '#007aff',
        success(e) {
          console.log(e.tapIndex + 1);
          console.log(activity_id);
          if (e.tapIndex == 3) {
            if (that.data.ispayId.indexOf(myid) == -1) {
              wx.showToast({
                title: '您未参加活动',
                icon: "none",
              })
              return false;
            }
            wx.request({
              url: ROOT_URL + 'actor_activity/delete/',
              method: "DELETE",
              data: {
                openid: OPENID,
                activity_id: activity_id,
              },
              success(res) {
                if (res.data.code==0) {
                  console.log(res)
                  wx.showToast({
                    title: '退出活动成功',
                  })
                } else {
                  wx.showToast({
                    title: res['data']['msg'],
                    icon: "none"
                  })

                }
              },
              error(err) {
                wx.showToast({
                  title: '网络开小差~,请检查网络',
                  icon: "none"
                })
              }
            })
          } else {
            if (e.tapIndex == 2 && that.data.participantId.indexOf(myid) == -1) {
              wx.showToast({
                title: '未报名无法请假',
                icon: "none"
              })
              return false;
            }

            if (that.data.participantId.indexOf(myid) != -1 && e.tapIndex == 0) {
              wx.showToast({
                title: '您已在报名列表',
                icon: "none"
              })
              return false;
            }
            if (that.data.undeterminedId.indexOf(myid) != -1 && e.tapIndex == 1) {
              wx.showToast({
                title: '您已在待定列表',
                icon: "none"
              })
              return false;
            }
            if (that.data.leaveId.indexOf(myid) != -1 && e.tapIndex == 2) {
              wx.showToast({
                title: '您已在请假列表',
                icon: "none"
              })
              return false;
            }
            wx.request({
              url: ROOT_URL + 'actor_activity/signup/',
              method: "POST",
              data: {
                openid: OPENID,
                activity_id: activity_id,
                reg_state: e.tapIndex + 1,
              },
              success(res) {
                console.log(res)
                console.log(res["data"]["code"]);


                if (res["data"]["code"] === 0) {
                  if (e.tapIndex == 0) {
                    wx.showToast({
                      title: '报名成功',
                    })

                  } else if (e.tapIndex == 1) {
                    wx.showToast({
                      title: '修改为待定成功',
                    })

                  } else if (e.tapIndex == 2) {
                    wx.showToast({
                      title: '修改为请假成功',
                    })
                  }

                } else if (res["data"]["code"] === 2003) {
                  wx.showToast({
                    title: '钱包余额不足',
                    icon: "none"
                  })
                  return false

                } else {
                  wx.showToast({
                    title: res['data']['msg'],
                    icon: "none"
                  })
                }



              },
              error(err) {
                wx.showToast({
                  title: '网络开小差~,请检查网络',
                  icon: "none"
                })
              }


            })

          }

          that.onLoad(Options);


        }
      }) 
    }else {
      wx.showActionSheet({
        itemList: ['待定', '请假', '退出活动'],
        itemColor: '#007aff',
        success(e) {
          console.log(e.tapIndex + 1);
          console.log(activity_id);
          if (e.tapIndex == 2) {
            if (that.data.ispayId.indexOf(myid) == -1) {
              wx.showToast({
                title: '您未参加活动',
                icon: "none",
              })
              return false;
            }
            wx.request({
              url: ROOT_URL + 'actor_activity/delete/',
              method: "DELETE",
              data: {
                openid: OPENID,
                activity_id: activity_id,
              },
              success(res) {
                if (res.data.code) {
                  console.log(res)
                  wx.showToast({
                    title: '退出活动成功',
                  })
                } else {
                  wx.showToast({
                    title: res['data']['msg'],
                    icon: "none"
                  })

                }
              },
              error(err) {
                wx.showToast({
                  title: '网络开小差~,请检查网络',
                  icon: "none"
                })
              }
            })
          } else {
            if (e.tapIndex == 1 && that.data.participantId.indexOf(myid) == -1) {
              wx.showToast({
                title: '未报名无法请假',
                icon: "none"
              })
              return false;
            }

            // if (that.data.participantId.indexOf(myid) != -1 && e.tapIndex == 0) {
            //   wx.showToast({
            //     title: '您已在报名列表',
            //     icon: "none"
            //   })
            //   return false;
            // }
            if (that.data.undeterminedId.indexOf(myid) != -1 && e.tapIndex == 0) {
              wx.showToast({
                title: '您已在待定列表',
                icon: "none"
              })
              return false;
            }
            if (that.data.leaveId.indexOf(myid) != -1 && e.tapIndex == 1) {
              wx.showToast({
                title: '您已在请假列表',
                icon: "none"
              })
              return false;
            }
            wx.request({
              url: ROOT_URL + 'actor_activity/signup/',
              method: "POST",
              data: {
                openid: OPENID,
                activity_id: activity_id,
                reg_state: e.tapIndex + 1,
              },
              success(res) {
                console.log(res)
                console.log(res["data"]["code"]);


                if (res["data"]["code"] === 0) {
                  // if (e.tapIndex == 0) {
                  //   wx.showToast({
                  //     title: '报名成功',
                  //   })

                  // } else 
                  if (e.tapIndex == 0) {
                    wx.showToast({
                      title: '修改为待定成功',
                    })

                  } else if (e.tapIndex == 1) {
                    wx.showToast({
                      title: '修改为请假成功',
                    })
                  }

                } else if (res["data"]["code"] === 2003) {
                  wx.showToast({
                    title: '钱包余额不足',
                    icon: "none"
                  })
                  return false

                } else {
                  wx.showToast({
                    title: res['data']['msg'],
                    icon: "none"
                  })
                }



              },
              error(err) {
                wx.showToast({
                  title: '网络开小差~,请检查网络',
                  icon: "none"
                })
              }


            })

          }

          that.onLoad(Options);


        }
      }) 
    }
     
    
  },

  //管理活动
  control:function(){
    let that = this;
    wx.showActionSheet({
      itemList: ['编辑活动', '取消活动'],
      itemColor: '#007aff',
      success(res) {
        
        if (res.tapIndex==0){
          wx.navigateTo({
            url: '/pages/putAddActive/putAddActive?id='+activity_id,
          })


        }else if (res.tapIndex==1){
          var data= {
            pk: activity_id,
              activity_state: 0,
            };
            console.log(data)
          wx.request({
            url: ROOT_URL + 'activity/up/',
            method: "PUT",
            data: {
              pk: activity_id,
              activity_state:0,
            },
            success(res){
              if (res.data.code) {
              console.log(res)
              wx.showToast({
                title: '取消活动成功',
              })
              setTimeout(function () {
                wx.switchTab({
                  url: '/pages/home/home',
                })
              }, 1000)
              }else{

              }
            },
            error(err) {
              wx.showToast({
                title: '网络开小差~,请检查网络',
                icon: "none"
              })
            }
          })

        }

      }

    })
    
  },
  gohome: function(){
    wx.switchTab({
      url: '/pages/home/home',
    })
  },

  deleteLeaveWord:function(e){
    let that = this;
    wx.request({
      url: ROOT_URL + '/message/delete/',
      method:'POST',
      data:{
        message: e.currentTarget.id,
      },
      success(res){
        console.log(res)
        if (res.data.code==0){
          wx.showToast({
            title: '删除留言成功',
          })
          setTimeout(function () {
            that.onLoad(Options);
          }, 1000)
        }else{
        wx.showToast({
          title: res['data']['msg'],
          icon: "none"
        })
        }
      },
      error(err) {
        wx.showToast({
          title: '网络开小差~,请检查网络',
          icon: "none"
        })
      }
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
  onShow: function (options) {
    

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