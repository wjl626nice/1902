// pages/home/home.js
const APP = getApp();
const ROOT_URL = APP.globalData.ROOT_URL;
const OPENID = wx.getStorageSync('openid');
let Pages = 1;
Page({
  /**
   * 页面的初始数据
   */
  data: {
    person_info: {
      avatar: "",
      nickname: ""
    },
    // 赛制0: 待定, 1: 5人制, 2: 6人制, 3: 7人制, 4: 8人制, 5: 9人制, 6: 10人制, 7: 11人制
    race_format: ['待定', '5人制', '6人制', '7人制', '8人制', '9人制', '10人制', '11人制'],
    checkIsShow: wx.getStorageSync('checkIsShow'),
    mylist: '',
    active_num: '',
    address: '', //区域
    history_num: '',
    myheight: '',
    active_time: '',
    sort_rule: '',
    lent: '',
    isshow: true,
    fetchlist: '',
    fetchlent: '',
    fetchheight: '',
    footballnum: '',
    formater: ''
  },

  avatarUrl: function (e) {
    var x = e.split('://');
    if (x.length > 1) {
      return e;
    } else {
      return ROOT_URL + e;
    }

  },
// 选择时间 调用函数
  dateChange(event) {
    this.setData({
      active_time: event.detail.value,
    })
    this.timeSort();
  },
  bindPickerChange(event) {
    this.setData({
      formater: event.detail.value
    })
    this.typeSort();
  },
  //获取活动列表请求
  getActiveList: function () {
    var that = this
    let openid = wx.getStorageSync('openid');
    //我的活动
    wx.request({
      url: `${ROOT_URL}actor_activity/my_participating/`,
      data: {
        openid: openid,
        page: 1
      },
      success: (res) => {
        console.log(res)
        if (res.data.data.length == 0) {
          that.setData({
            myheight: 0,
            isshow: false
          })
        } else {
          that.setData({
            myheight: 220 * res.data.data.length + 20,
            lent: res.data.data.length,

          })
          if (that.data.myheight < 220 * 5) {
            let height = 220 * res.data.data.length + 20
            that.setData({
              myheight: height
            })
          } else {
            let height = 220 * 5 + 20
            that.setData({
              myheight: height
            })

          }

        }
        for (var i = 0; i < res.data.data.length; i++) {
          res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
        }
        that.setData({
          mylist: res.data.data,
          lent: res.data.data.length

        })
      }
    })
    //我组织的活动
    wx.request({
      url: `${ROOT_URL}activity/org_sum/`,
      method: 'GET',
      data: {
        openid: openid,
      },
      success(res) {
        // console.log(res)
        that.setData({
          active_num: res.data.data.sum
        })
      }
    })
    //历史活动
    wx.request({
      url: `${ROOT_URL}actor_activity/sum/`,
      method: 'GET',
      data: {
        id: wx.getStorageSync("myid"),
      },
      success(res) {
        // console.log(res)
        that.setData({
          history_num: res.data.data.sum
        })
      }
    })
    //获取历史活动
    wx.request({
      url: `${ROOT_URL}actor_activity/historical/`,
      method: 'GET',
      data: {
        openid: openid,
      },
      success(res) {
        console.log(res)
        wx.setStorageSync("history", res.data)
      }
    })
    //踢过球的人数
    wx.request({
      url: `${ROOT_URL}actor_activity/user_sum/`,
      method: 'GET',
      data: {
        openid: openid,
      },
      success(res) {
        that.setData({
          footballnum: res.data.data.sum
        })
      }
    })
  },
  // initData: function() {
  //   const { getActiveList, fetchActivityList } = this;
  //   // 请求活动列表
  //   getActiveList();
  //   fetchActivityList(1,1,0);
  //   wx.hideLoading()
  // },
  //  跳转 历史活动页面
  active_history: function () {
    wx.navigateTo({
      url: '/pages/historyActive/historyActive',
    })
  },
  //跳转推荐活动页面
  active_recommend: function () {
    wx.navigateTo({
      url: '/pages/recommendActive/recommendActive',
    })
  },
  //查看更多 我的活动
  lookMoreMineActive: function () {
    let that = this
    let openid = wx.getStorageSync("openid")
    if (that.data.myheight == 220 * 5 + 20) {
      let height = 220 * that.data.lent + 20
      that.setData({
        myheight: height,
      })
      if (that.data.lent == 5) {
        let height = 220 * that.data.lent + 20
        wx.showToast({
          title: '已无更多活动',
          icon: "none"
        })
        that.setData({
          myheight: height,
          isshow: false
        })
      }
    } else {
      Pages = Pages + 1,
        wx.request({
          url: `${ROOT_URL}actor_activity/my_participating/`,
          method: "GET",
          data: {
            openid: openid,
            page: Pages
          },
          success(res) {
            let len = res.data.data.length
            if (res.data.data == '') {
              that.setData({
                isshow: false
              })
              wx.showToast({
                title: '已无更多活动',
                icon: "none"
              })
              return false
            } else {
              let data = that.data.mylist
              let data2 = res.data.data
              data = data.concat(data2)
              console.log(data)
              let height = 220 * len + that.data.myheight
              for (var i = 0; i < res.data.data.length; i++) {
                res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
              }
              that.setData({
                myheight: height,
                mylist: data
              })
            }

          }
        })

    }
  },
  //跳转活动详情页面
  activeDetail: function (e) {
    var id = e.currentTarget.id;
    wx.navigateTo({
      url: '/pages/activeDetail/activeDetail?id=' + id,
    })
  },
  //设置信息
  setInfo: function (userInfo, openid) {
    var that = this
    var data = that.data.person_info
    wx.request({
      url: ROOT_URL + 'member/getMemberInfo/',
      method: "GET",
      data: {
        openid: openid
      },
      success(res) {
        // console.log(res.data.data.avatar)
        // userInfo.avatarUrl = res.data.data.avatar,
        // 判断用户头像是否为原微信头像
        function avatarUrl(e) {
          var x = e.split('://');
          if (x.length > 1) {
            return e;
          } else {
            return ROOT_URL + e;
          }
        }
        userInfo.nickName = res.data.data.nickname
        data.avatar = avatarUrl(res.data.data.avatar)
        userInfo.avatarUrl = avatarUrl(res.data.data.avatar),
          wx.setStorageSync('userInfo', userInfo)
        data.nickname = userInfo.nickName
        that.setData({
          person_info: data
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   * 只加载一次
   * 既然页面是动态更新的 就不要写在这里
   */
  onLoad: function (options) {
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },
  /**
   * 生命周期函数--监听页面显示
   * 每次进入页面都要重新加载
   */
  onShow: function () {
    let openid = wx.getStorageSync("openid");
    let userInfo = wx.getStorageSync('userInfo');
    Pages = 1
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    this.getActiveList()
    this.setInfo(userInfo, openid)
    wx.hideLoading()
    // that.fetchActivityList(1, 1, 0);
    this.fetchActivityList();
    if (this.data.lent >= 5) {
      this.setData({
        myheight: 220 * 5 + 20,
        isshow: true
      })
    }
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
    let that = this
    if (that.data.fetchheight == 220 * 5 + 20) {
      let height = 220 * that.data.fetchlent + 20
      that.setData({
        fetchheight: height
      })
    } else {
      Pages = Pages + 1;
      const { sort_rule, active_time, formater } = this.data;
      let params = {}
      if (sort_rule === 3) {
        params.activity_time = active_time;
      } else if (sort_rule === 2) {
        params.formater = formater;
      }
      wx.request({
        url: `${ROOT_URL}actor_activity/recommend/`,
        method: "GET",
        data: {
          openid: OPENID,
          sort: that.data.sort_rule,
          page: Pages,
          ...params
        },
        success(res) {
          let len = res.data.data.length
          if (res.data.data == '') {
            wx.showToast({
              title: '已无更多推荐活动',
              icon: "none"
            })
            return false
          } else {
            let data = that.data.fetchlist
            let data2 = res.data.data
            data = data.concat(data2)
            let height = 220 * len + that.data.fetchheight
            for (var i = 0; i < res.data.data.length; i++) {
              res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
            }
            that.setData({
              fetchheight: height,
              fetchlist: data
            })
          }

        }
      })

    }

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  //推荐更多 初始化加载
  fetchActivityList: function () {
    let that = this;
    let OPENID = wx.getStorageSync('openid');
    const params = {};
     switch(that.data.sort_rule) {
       case 1:
         params.activity_time = that.data.active_time;
         break;
         case 2:
         params.formater = that.data.formater;
         break;
         case 3:
         params.address = that.data.address;
         break;
     }
    wx.request({
      url: `${ROOT_URL}actor_activity/recommend/`,
      method: "GET",
      data: {
        openid: OPENID,
        sort: that.data.sort_rule,
        page: 1,
        ...params
      },
      success: (res) => {
        if (res.data.data.length == 0) {
          that.setData({
            fetchheight: 0
          })
        } else {
          that.setData({
            fetchheight: 220 * res.data.data.length + 20,
            fetchlent: res.data.data.length,
          })

          if (that.data.fetchheight < 220 * 5) {
            let height = 220 * res.data.data.length + 20
            that.setData({
              fetchheight: height
            })
          } else {
            let height = 220 * 5 + 20;
            that.setData({
              fetchheight: height
            })

          }
        }
        for (var i = 0; i < res.data.data.length; i++) {
          res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
        }
        that.setData({
          fetchlist: res.data.data,
          fetchlent: res.data.data.length

        })
      }

    })
  },

  listMyActivity: function (e) {
    wx.navigateTo({
      url: '/pages/myActivity/myActivity',
    })

  },
  listMyballFriends: function (e) {
    wx.navigateTo({
      url: '/pages/ballFriend/ballFriend?id=1',
      success() {
        wx.setStorageSync("group", "")
      }
    })
  },
  listMyParticipant: function (e) {

  },
  activityMyList: function (e) {
    wx.navigateTo({
      url: '/pages/activityMyList/activityMyList',
    })

  },
  //删除活动
  deleteActivity: function (e) {
    let that = this;
    wx.request({
      url: ROOT_URL + 'activity/delete/',
      method: "POST",
      data: {
        pk: e.currentTarget.id,
      },
      success(res) {
        wx.showToast({
          title: '删除活动成功',
        })
        setTimeout(function () {
          that.onLoad();
        }, 1000)
      }
    })

  },
  //智能排序
  autoSort: function (e) {
    let that = this;
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    this.setData({
      sort_rule: 4,
      formater: '',
    })
    setTimeout(function () {
      let openid = wx.getStorageSync('openid');
      wx.request({
        url: `${ROOT_URL}actor_activity/recommend/`,
        data: {
          openid: openid,
          page: 1
        },
        success: (res) => {
          console.log(res)
          if (res.data.data.length == 0) {
            that.setData({
              fetchheight: 0,
              // isshow: false
            })
          } else {
            that.setData({
              fetchheight: 220 * res.data.data.length + 20,
              fetchlent: res.data.data.length,
              // isshow: true
            })
            if (that.data.fetchheight < 220 * 5) {
              let height = 220 * res.data.data.length + 20
              that.setData({
                fetchheight: height,
                // isshow: true
              })
            } else {
              let height = 220 * 5 + 20
              that.setData({
                fetchheight: height,
                // isshow: true
              })

            }

          }
          for (var i = 0; i < res.data.data.length; i++) {
            res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
          }
          that.setData({
            fetchlist: res.data.data,
            fetchlent: res.data.data.length

          })
        }
      })
      wx.hideLoading()
    }, 2000)

  },
  //按区域排序
  splaceSort: function (e) {
    let that = this;
    let openid = wx.getStorageSync('openid');
    let address = "";
    wx.getLocation({
      type: 'gcj02',
      success: function (res) {
        wx.chooseLocation({
          success: function (res) {
            address = res.name;
            that.setData({
              sort_rule: 3,
              formater: '',
              address,
            })
            //console.log(address)
            wx.showLoading({
              title: '加载中',
              mask: true
            })
            setTimeout(function () {
              console.log(address)

              wx.request({
                url: `${ROOT_URL}actor_activity/recommend/`,
                data: {
                  openid: openid,
                  sort: 3,
                  address: address,
                  page: 1
                },
                success: (res) => {
                  console.log(res)
                  if (res.data.data.length == 0) {
                    that.setData({
                      fetchheight: 0,
                    })
                    // that.setData({
                    //   myheight: 0,
                    //   isshow: false
                    // })
                  } else {
                    that.setData({
                      fetchheight: 220 * res.data.data.length + 20,
                      fetchlent: res.data.data.length,
                      // isshow: true
                    })
                    if (that.data.fetchheight < 220 * 5) {
                      let height = 220 * res.data.data.length + 20
                      that.setData({
                        fetchheight: height,
                        // isshow: true
                      })
                    } else {
                      let height = 220 * 5 + 20
                      that.setData({
                        fetchheight: height,
                        // isshow: true
                      })

                    }

                  }
                  for (var i = 0; i < res.data.data.length; i++) {
                    res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
                  }
                  that.setData({
                    fetchlist: res.data.data,
                    fetchlent: res.data.data.length

                  })
                }
              })
              wx.hideLoading()
            }, 2000)
          },

        })
      }
    })


  },
  //赛制排序
  typeSort: function (e) {
    let that = this;
    let openid = wx.getStorageSync('openid');
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    this.setData({
      sort_rule: 2,
    })
    setTimeout(function () {
      wx.request({
        url: `${ROOT_URL}actor_activity/recommend/`,
        data: {
          openid: openid,
          sort: 2,
          page: 1,
          formater: that.data.formater
        },
        success: (res) => {
          console.log(res)

          if (res.data.data.length == 0) {
            that.setData({
              fetchheight: 0,
              // isshow: false
            })
          } else {
            that.setData({
              fetchheight: 220 * res.data.data.length + 20,
              fetchlent: res.data.data.length,
              // isshow: true
            })
            if (that.data.fetchheight < 220 * 5) {
              let height = 220 * res.data.data.length + 20
              that.setData({
                fetchheight: height,
                // isshow: true
              })
            } else {
              let height = 220 * 5 + 20
              that.setData({
                fetchheight: height,
                // isshow: true
              })

            }

          }
          for (var i = 0; i < res.data.data.length; i++) {
            res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
          }
          that.setData({
            fetchlist: res.data.data,
            fetchlent: res.data.data.length

          })
        }
      })
      wx.hideLoading()
    }, 2000)
  },
  //按时间排序
  timeSort: function () {
    let that = this;
    let openid = wx.getStorageSync('openid');
    //我的活动
    wx.showLoading({
      title: '加载中',
      mask: true
    })
    this.setData({
      sort_rule: 1,
      formater: ''
    })
    setTimeout(function () {
      wx.request({
        url: `${ROOT_URL}actor_activity/recommend/`,
        data: {
          openid: openid,
          sort: 1,
          page: 1,
          active_time: that.data.active_time
        },
        success: (res) => {
          console.log(res)
          if (res.data.data.length == 0) {
            that.setData({
              fetchheight: 0,
              //  isshow: false
            })
          } else {
            that.setData({
              fetchheight: 220 * res.data.data.length + 20,
              fetchlent: res.data.data.length,
              //  isshow: true
            })
            if (that.data.fetchheight < 220 * 5) {
              let height = 220 * res.data.data.length + 20
              that.setData({
                fetchheight: height,
                //  isshow: true
              })
            } else {
              let height = 220 * 5 + 20
              that.setData({
                fetchheight: height,
                //  isshow: true
              })

            }

          }
          for (var i = 0; i < res.data.data.length; i++) {
            res.data.data[i].originator_id.avatar = that.avatarUrl(res.data.data[i].originator_id.avatar);
          }
          that.setData({
            fetchlist: res.data.data,
            fetchlent: res.data.data.length

          })
        }
      })
      wx.hideLoading()
    }, 2000)

  },
})