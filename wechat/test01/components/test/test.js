// components/test/test.js
Component({
  options: {
    multipleSlots: true   //开启多插槽支持
  },
  /**
   * 组件的属性列表
   * 接收外部传递的数据
   * 可写可读
   */
  properties: {
    number: {
      type: Number,  // 数据类型
      value: 0      // 默认值
    },
    // 简写方式
    name: String,    // 默认值空
    newName: String,
  },
  // js中数据类型：String、Array、Object、Boolean、Number、null、NaN、undefined
  // type可以写的类型：String、Array、Object、Boolean、Number、null（不推荐 不限制类型）

  /**
   * 组件的初始数据
   * 设置组件的私有属性
   */
  data: {
      count: 0,
      price: 10.20,
      totalPrice: 0.00
  },

  /**
   * 组件的方法列表
   */
  methods: {
    changeNum: function(){
      // 组件中data属性获取方式
      // console.log(this.data.count)
      var count = this.data.count + 1
      var number = this.properties.number + 2
      this.setData({
        count: count,
        number: number
      })
    },
    triggerMyevent: function(){
      //triggerEvent 触发事件
      this.triggerEvent('myevent',{aa:11, bb: 22})
    }
  },
  observers: {
    'number': function(newNumber){
      console.log(newNumber)
    }
  }
})
