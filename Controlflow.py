def calculate_discount(price,dicount_percent):
    p=price
    dp=dicount_percent
    if dp>=0.2:
        p=p-(p*dp)
        print(f"The final price of the product will be: {p}")
    else:
        print(f"The final price of the product will be: {p}")
    
original_price=input("Enter price of item: ")
discount_allowed=input("Enter discount allowed in decimal, 0.01 - 0.9: ")
original_price = float(original_price)
discount_allowed = float(discount_allowed)
calculate_discount(original_price, discount_allowed)
