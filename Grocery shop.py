products = {
    "Water 500Ml" :2,
    "Water 1.5 Leters" :int(5),
    "Milk"  :int (8) ,
    "Chocklate" :int (2) ,
    "Orange Juice" :int (2),
    "Grapes Juice" :int (2) ,
    "Lemon & Mint Juice" :int(2) ,
    "Yogurt" :int (12) ,
    "Pudding" :int (4) ,
}
bill = 0
Cart =[]

while True:
    print(products)
    k = input ("What do you want to buy?")
    if k in products:
        Cart.append(k)
        print(Cart)
        bill += products[k]
    else:
        print("We don't have this product")
        break
print("So your salary will be", bill)