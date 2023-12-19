from egcd import egcd

with open("message.txt","r") as file:
    text = file.read()

number = [(egcd(int(num) % 41,41)[1] % 41 + 41)%41 for num in text.split(" ")[:-1]]

flag = ""
for i in number:
    if (i >= 1) and (i <= 26):
        flag += chr(i+96)
    elif (i >= 27) and (i <= 36):
        flag += chr(i+21)
    else:
        flag += "_"
print(flag)