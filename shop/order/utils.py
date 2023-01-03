from discount.models import Coupon
from decimal import Decimal



def check_discount(request,coupon_code:str|None,amount:Decimal)->tuple:
    discount = 0
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code)
            
        except:
            data = { 'msg':'Your coupon does not exist'}
        else:
            if coupon.is_ok(request, amount):
                discount = coupon.apply_discount(amount)
                data = { 'msg':'Your discount coupon has been applied'}
            else:
                data = { 'msg':'Your discount coupon is not valid'}
    else:
        data = {}

    return (discount,data)
