# basic-mod
## AUTHOR: WILL HONG

### Description:
We found this weird message being passed around on the servers, we think we have a working decryption scheme.

Download the message [here]("https://artifacts.picoctf.net/c/129/message.txt").

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### 2. Solution:
```py
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
```
Hmm, i'm learning clean code :>

<p align="center">
  <img src="https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif" />
</p>

---

minhchi
