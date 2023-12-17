f = open("message.txt", "r")

arrayString = f.read().split(" ")[:-1]
result = [int(i) % 37 for i in arrayString]

flag = ""
for i in result:
    if (i >= 0) and (i <= 25):
        flag += chr(i+65)
    elif (i > 25) and (i <= 35):
        flag += chr(i+22)
    else:
        flag += "_"
print(flag)