order_price = int(input('Please enter your order\'s total price:'))

payment_price = order_price

if order_price > 50000:
    payment_price = order_price - int(order_price * (20 / 100))
elif 20000 <= order_price <= 50000:
    payment_price = order_price - int(order_price * (10 / 100))


print(payment_price)