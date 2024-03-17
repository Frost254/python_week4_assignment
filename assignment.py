def calculate_discount(price, discount_price):
    if discount_price < 20:
        return price
    else:
        return price - (price * (discount_price / 100))

price = int(input("Enter the price of the item: "))
discount_price = int(input("Enter the percent discount of the item: "))

print(calculate_discount(price, discount_price))
