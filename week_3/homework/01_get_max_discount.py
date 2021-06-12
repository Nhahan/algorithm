shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    price = prices
    coupon = coupons
    discounted_price = [0] * len(coupon)
    for i in range(len(coupons)):
        discounted_price[i] = max(price) * (100 - max(coupon)) / 100
        price.remove(max(price))
        coupon.remove(max(coupon))
    answer = sum(price) + sum(discounted_price)
    return answer


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.