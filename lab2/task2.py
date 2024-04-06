def checknum(num):
    if num % 3 == 0 and num % 5 == 0:  
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return "not fizzbuzz"

num = input("enter number ")
try:
    num = int(num)
    print(f"Word: {checknum(num)}")
except ValueError:
    print("valid integer")
