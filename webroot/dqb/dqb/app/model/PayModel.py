from django.db import models
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from app.model.MemberModel import QyMember,MemberPayment


# 支付
class QyPay(models.Model):
    types = (
        (0, '默认'),
        (1, '充值'),
        (2, '提现'),
        (3, '退款'),
        (4, '支付'),
        (5, '收款'),
    )
    state = (
        (0, '默认'),
        (1, '支付失败'),
        (2, '支付中'),
        (3, '支付成功')
    )
    member_id = models.IntegerField('支付人ID')
    out_trade_no = models.CharField('订单号',max_length=20)
    pay_type = models.IntegerField('支付类型',
                                   choices=types,
                                   default=0
                                   )
    pay_amount = models.CharField('支付金额',max_length=20)
    pay_state = models.IntegerField('支付状态',
                                        choices=state,
                                        default=2
                                        )
    add_time = models.CharField('创建时间', max_length=20)

    def __str__(self):
        return self.pay_state

    class Meta:
        db_table = 'qy_pay'
        verbose_name = '支付'
        verbose_name_plural = verbose_name


# 实体类
class PaySerializer(ModelSerializer):
    member_id = SerializerMethodField()

    class Meta:
        model = QyPay
        fields = '__all__'

    # 充值人信息
    def get_member_id(self, obj):
        member = QyMember.objects.get(pk=obj.member_id)
        memberS = MemberPayment(member, many=False)
        return memberS.data
