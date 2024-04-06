def rev(word):
    return word[::-1]

word = input("enter string: ")

if word.isalpha():
    print(f"reverse : {rev(word)}")
