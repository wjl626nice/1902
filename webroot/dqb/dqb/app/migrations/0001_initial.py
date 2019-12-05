# Generated by Django 2.1.1 on 2018-11-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QyActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField(blank=True, verbose_name='公告')),
                ('activity_time', models.CharField(blank=True, max_length=20, verbose_name='活动时间')),
                ('address_province', models.CharField(blank=True, max_length=20, verbose_name='省份')),
                ('address_city', models.CharField(blank=True, max_length=20, verbose_name='城市')),
                ('address_area', models.CharField(blank=True, max_length=20, verbose_name='区/县')),
                ('address_detailed', models.CharField(blank=True, max_length=256, verbose_name='详细地点')),
                ('formater', models.IntegerField(choices=[(0, '待定'), (1, '5人制'), (2, '6人制'), (3, '7人制'), (4, '8人制'), (5, '9人制'), (6, '10人制'), (7, '11人制')], default=0, verbose_name='赛制')),
                ('type', models.IntegerField(choices=[(0, '散踢'), (1, '队内活动'), (2, '球队比赛')], default=0, verbose_name='类型')),
                ('upper_limit', models.IntegerField(blank=True, verbose_name='人数上限')),
                ('lower_limit', models.IntegerField(blank=True, verbose_name='人数下限')),
                ('is_limit', models.IntegerField(choices=[(0, '不限时'), (1, '限时')], default=0, verbose_name='是否设置限时报名')),
                ('limit_time', models.CharField(blank=True, max_length=20, verbose_name='报名截止时间')),
                ('price', models.CharField(default='0.00', max_length=16, verbose_name='报名费用')),
                ('activity_img', models.TextField(blank=True, max_length=255, verbose_name='活动图片')),
                ('originator_id', models.IntegerField(verbose_name='发起人')),
                ('activity_state', models.IntegerField(choices=[(0, '已取消'), (1, '可参加'), (2, '已过期')], default=1, verbose_name='活动状态')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
                ('is_irres', models.IntegerField(choices=[(0, '不限时'), (1, '限时')], default=0, verbose_name='是否限时无责')),
                ('irres_time', models.CharField(blank=True, max_length=20, verbose_name='无责时间')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
                'db_table': 'qy_activity',
            },
        ),
        migrations.CreateModel(
            name='QyActor_activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.IntegerField()),
                ('member_id', models.IntegerField()),
                ('reg_state', models.IntegerField(choices=[(1, '报名'), (2, '待定'), (3, '请假')], default=0, verbose_name='参加人员状态')),
                ('free_state', models.IntegerField(choices=[(0, '付费'), (1, '免费')], default=0, verbose_name='是否付费')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户-活动中间表',
                'verbose_name_plural': '用户-活动中间表',
                'db_table': 'qy_actor_activities',
            },
        ),
        migrations.CreateModel(
            name='QyFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField(blank=True, verbose_name='用户id')),
                ('content', models.TextField(blank=True, verbose_name='反馈的意见内容')),
                ('Feedback_state', models.IntegerField(choices=[(0, '未查看'), (1, '已查看')], default=0, verbose_name='是否已查看')),
                ('add_time', models.CharField(blank=True, max_length=20, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'qy_Feedback',
            },
        ),
        migrations.CreateModel(
            name='QyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_a_id', models.IntegerField(verbose_name='用户')),
                ('member_b_id', models.IntegerField(verbose_name='被打标签用户')),
                ('group', models.CharField(default='我的球友', max_length=32, verbose_name='分组')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'qy_group',
            },
        ),
        migrations.CreateModel(
            name='QyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(blank=True, max_length=30, verbose_name='openid')),
                ('unionid', models.CharField(blank=True, max_length=30, verbose_name='unionid')),
                ('avatar', models.TextField(blank=True, max_length=255, verbose_name='头像')),
                ('age', models.IntegerField(blank=True, verbose_name='年龄')),
                ('nickname', models.CharField(blank=True, max_length=56, verbose_name='昵称')),
                ('profession', models.CharField(blank=True, max_length=255, verbose_name='职业')),
                ('phonenum', models.BigIntegerField(blank=True, verbose_name='电话')),
                ('balance', models.CharField(blank=True, max_length=20, verbose_name='余额')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
                ('cardholder', models.CharField(blank=True, max_length=56, verbose_name='持卡人')),
                ('ID_number', models.CharField(blank=True, max_length=20, verbose_name='身份证号')),
                ('opening_bank', models.CharField(blank=True, max_length=36, verbose_name='开户行')),
                ('bank_card_number', models.CharField(blank=True, max_length=22, verbose_name='银行卡号')),
                ('reserved_phone_number', models.BigIntegerField(blank=True, verbose_name='银行预留手机号')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'qy_member',
            },
        ),
        migrations.CreateModel(
            name='QyMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.IntegerField(verbose_name='相关活动ID')),
                ('member_id', models.IntegerField(verbose_name='留言人')),
                ('message_img', models.TextField(blank=True, max_length=255, verbose_name='留言图片')),
                ('message_content', models.TextField(blank=True, verbose_name='留言内容')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
                'db_table': 'qy_message',
            },
        ),
        migrations.CreateModel(
            name='QyNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_id', models.IntegerField(verbose_name='申请人')),
                ('respondent_id', models.IntegerField(verbose_name='被申请人')),
                ('content', models.TextField(blank=True, verbose_name='消息内容')),
                ('apply_time', models.CharField(max_length=20, verbose_name='申请时间')),
                ('new_state', models.IntegerField(choices=[(0, '拒绝'), (1, '同意'), (2, '待处理')], default=2, verbose_name='消息状态')),
            ],
            options={
                'verbose_name': '消息',
                'verbose_name_plural': '消息',
                'db_table': 'qy_news',
            },
        ),
        migrations.CreateModel(
            name='QyPut_forward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField(verbose_name='提现人ID')),
                ('amount_of_cash', models.CharField(blank=True, max_length=20, verbose_name='提现金额')),
                ('put_forward_state', models.IntegerField(choices=[(0, '准备中'), (1, '提现失败'), (2, '提现中'), (3, '提现成功')], default=0, verbose_name='提现状态')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '提现',
                'verbose_name_plural': '提现',
                'db_table': 'qy_put_forward',
            },
        ),
        migrations.CreateModel(
            name='QyRecharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField(verbose_name='充值人ID')),
                ('recharge_amount', models.CharField(blank=True, max_length=20, verbose_name='充值金额')),
                ('recharge_state', models.IntegerField(choices=[(0, '准备中'), (1, '充值失败'), (2, '充值中'), (3, '充值成功')], default=0, verbose_name='充值状态')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '充值',
                'verbose_name_plural': '充值',
                'db_table': 'qy_recharge',
            },
        ),
        migrations.CreateModel(
            name='QyReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.IntegerField(verbose_name='关联的留言ID')),
                ('reply_member', models.IntegerField(verbose_name='回复人')),
                ('to_reply_member', models.IntegerField(verbose_name='被回复者')),
                ('reply_content', models.TextField(blank=True, verbose_name='回复内容')),
                ('add_time', models.CharField(max_length=20, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'qy_replay',
            },
        ),
    ]