import string

LOWERCASE_OFFSET = ord("a") # 97
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		# convert to binary
		binary = "{0:08b}".format(ord(c))

		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET	# 97
	t2 = ord(k) - LOWERCASE_OFFSET	# 97
	return ALPHABET[(t1 + t2) % 16]

flag = "testing"
key = "testing"
assert all([k in ALPHABET for k in key]) # key in ALPHABET
assert len(key) == 1 # key is a charater

b16 = b16_encode(flag)

enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)]) # key[i % len(key)] = key[i % 1] = key

ciphertext = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"

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

print(decryption(ciphertext,key))