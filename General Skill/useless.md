# useless
## AUTHOR: LOIC SHEMA

### Description:
There's an interesting script in the user's home directory
Additional details will be available after launching your challenge instance.

#### 1. Solution
**Connect:**
```sh
ssh -p <port> picoplayer@saturn.picoctf.net
```

You can check the file and read code to identify bugs.

**Check user:**
```sh
whoami
```
$\to$ picoplayer

**Check code:**
```sh
cat useless
```
Result:
```sh
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
	if [[ "$1" == "add" ]]
	then
	  sum=$(( $2 + $3 ))
	  echo "The Sum is: $sum"

	elif [[ "$1" == "sub" ]]
	then
	  sub=$(( $2 - $3 ))
	  echo "The Substract is: $sub"

	elif [[ "$1" == "div" ]]
	then
	  div=$(( $2 / $3 ))
	  echo "The quotient is: $div"

	elif [[ "$1" == "mul" ]]
	then
	  mul=$(( $2 * $3 ))
	  echo "The product is: $mul"

	else
	  echo "Read the manual"
	fi
fi
```

Hmm, the code doesn't have any  bugs, it is simply a calculator with the operators + - * /.

I see ```"Read the manual"```, try this:
```sh
man useless
```
Opp~, flag  :slightly_smiling_face:

<p align="center">
  <img src="https://media.giphy.com/media/kd9BlRovbPOykLBMqX/giphy.gif"/>
</p>

---

minhchi
