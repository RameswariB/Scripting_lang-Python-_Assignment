a = 5
for i in range(a):
    if (i == 0) or (i == (a-1)):
        print(i*" "+a*"*")
    else:
        print(i*" "+"*"+(a-2)*" "+"*")
