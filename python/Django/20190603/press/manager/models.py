from django.db import models

# Create your models here.
#  models.Model 系统模型，自定义模型继承了它，拥有了该模型的所有方法
# 出版社表
class Press(models.Model):
    id = models.AutoField(primary_key=True)
    press_name = models.CharField(max_length=35, null=False, unique=True)

    def __str__(self):
        # 当对象被作为字符串打印时，会自动调用
        # return "<press: press_name-{}>" % (self.press_name,)
        return "<press: press_name-{}>".format(self.press_name)

# 书表
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    books_name = models.CharField(max_length=25, null=False)
    # 咱们自己逻辑上的关系
    #press_id = models.IntegerField(null=False)

    # 通过ForeignKey 可以让数据库帮咱们维护两个表之间的关系。
    # 添加外键   ForeignKey外键。设置跟对应的模型关联。
    # to="Press"  让 Books 和 Press模型之间产生关联。相当于表与表之间产生关联。
    # on_delete 两个表之间有关系了。那么其中一个表中的数据删除了 另外一个表怎么办呢
    # DO_NOTHING 什么事也不做
    press = models.ForeignKey(to="Press", on_delete=models.DO_NOTHING, default=1)
