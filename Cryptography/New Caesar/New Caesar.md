# New Caesar
## AUTHOR: MADSTACKS

### Description:
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj [(new_caesar.py)](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Cryptography/New%20Caesar/new_caesar.py)

## 1. Knowledge

Mathematical for decryption:

$$
D_n(x) = (x-n) \\; mod \\; 26
$$

If you check the file ```new_caesar.py```, you will see:

```py
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % 16]
```
You can using the mathematical above to find ```c```.

I have a simple figure to describe that decryption:

![](/images/NewCaesar.PNG)

## 2. Solution:

```py
# select a random key in ALPHABET
def decryption(ciphertext,key):
	binary = ""
	result = ""
	for i in ciphertext:
		text = ALPHABET[(ALPHABET.index(i) - (ord(key)-97)) % 16]
		binary += "{0:04b}".format(ALPHABET.index(text))
		if len(binary) == 8:
			result += chr(int(binary,2))
			binary = ""
	return result

print(decode(ciphertext,key))
```

<p align="center">
  <img src="https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif" />
</p>

---

minhchi
