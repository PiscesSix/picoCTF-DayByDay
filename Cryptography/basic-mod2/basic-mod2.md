# basic-mod2
## AUTHOR: WILL HONG

### Description:
A new modular challenge!

Download the message [here](https://artifacts.picoctf.net/c/179/message.txt).

Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## 1. Knowledge
If you want to learn about modular inverses, this page will be helpful for you: [cp-algorithms.com](https://cp-algorithms.com/algebra/module-inverse.html).

```
egcd(a,m) = (gcd(a,m), x, y) = ax + my = gcd(a,m)
```
If ```gcd(a.m) = 1```, then we have modular inverses.

The resulting ```x``` from the extended Euclidean algorithm (egcd(a,m)) may be negative so we should do this:
```
x = (x % m + m) % m
```
## 2. Solution:
```py
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
```

<p align="center">
  <img src="https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif" />
</p>

---

minhchi
