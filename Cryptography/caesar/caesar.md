# caesar
## AUTHOR: SANJAY C/DANIEL TUNITIS

### Description:
Decrypt this [message.
](https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext).

## 1. Knowledge

### What is Caesar Cipher?

- "Shift cipher:"
    - Oldest and Simplest forms of encrypting.

Hmm, like this:

    - Plain text: ABCD
    - Ciphertext (right shift of 1): BCDE

The caesar cipher is the weakest forrms of encryption:

    - The key space is very small (try all 25 shift).

Mathematical for encryption:
$$
    E_n(x) = (x+n) \; mod \; 26
$$

Mathematical for decryption:
$$
    D_n(x) = (x-n) \; mod \; 26
$$

### 2. Solution:
The challenge:
> picoCTF{gvswwmrkxlivyfmgsrhnrisegl}

We can try all the keys in space key with this tool: [cryptii](https://cryptii.com/pipes/caesar-cipher).

Try 0 $-$ 25 to get flag :v

<p align="center">
  <img src="https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif" />
</p>

---

minhchi
