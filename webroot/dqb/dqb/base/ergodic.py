from app.model.PayModel import QyPay

def Pay_ergodic(obj,pay_type,state=''):
    list = []
    if state:
        for a in obj:
            for b in QyPay.objects.filter(member_id=a.id,pay_state=state,pay_type=pay_type).order_by('-id'):
                list.append(b)
    else:
        for a in obj:
            for b in QyPay.objects.filter(member_id=a.id,pay_type=pay_type).order_by('-id'):
                list.append(b)
    return list
