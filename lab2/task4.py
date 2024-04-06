def check_email():
    pass
def main():
    name = input("please enter your name: ")
    email = input("enter your email: ")
    if name.isalpha():
        print(f"name: {name}, email: {email}")
    else:
        print("not correct")

main()  
