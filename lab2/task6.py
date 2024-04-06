total = 0
count = 0

while True:
    num = input("enter a num :")
    if num.isdigit():
        num = int(num)
        total += num
        count += 1
    elif num == "done":
        break
    else:
        print("Invalid input. Please enter a valid number.")

if count > 0:
    average = total / count
else:
    average = 0
print(f"Count: {count}, Total: {total}, Average: {average}")
