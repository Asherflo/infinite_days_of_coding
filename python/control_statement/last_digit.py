number = eval(input("Enter any number"))
last_number = number % 10
if last_number % 3 == 0:
    print("the last number is divisible by 3")
else:
    print("the last number is not divisible by 3")