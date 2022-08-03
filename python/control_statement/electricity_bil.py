price = 0
user_unit = eval(input("enter your electricity unit"))
if user_unit < 100:
    price = 0
    print("no charge")
elif 100 < user_unit <= 200:
    price = (user_unit - 5) * 5
    print(price)
elif user_unit > 200:
    price = (user_unit - 200) * 10
    print(price)


    