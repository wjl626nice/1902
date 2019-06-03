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
    # 添加外键
    press = models.ForeignKey(to="Press", on_delete=models.DO_NOTHING)
