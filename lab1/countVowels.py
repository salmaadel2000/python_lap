string = input("enter words here ")
vowel = 0
string = string.lower()  
for i in string:
    if i in 'aeiou': 
        vowel += 1

print("total number is =", vowel)
