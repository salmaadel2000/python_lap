elements = []
n = int(input("enter the size "))
for i in range(0, n):
    nums = int(input("enter the elements "))
    elements.append(nums)

elements.sort()
print(elements)
