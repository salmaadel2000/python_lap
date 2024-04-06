def generateArr(start_arr, len_arr):
    arr = list(range(start_arr, start_arr + len_arr))
    print(arr)

start = int(input(" array start"))
len = int(input(" array length "))
generateArr(start, len)
