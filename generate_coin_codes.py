import cipher
import random

LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
SYMBOLS = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_")
NUMBERS = list("0123456789")
VALIDATE = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_")

def get_codes():
	codes = []
	with open("allcodes.txt", "r") as f:
		for l in f.readlines():
			line = l.strip()
			if line!="":
				codes.append(line)
	return codes

def get_user(u):
	codes = []
	with open(f"user_{u}.txt", "r") as f:
		for l in f.readlines():
			line = l.strip()
			if line!="":
				codes.append(line)
	return codes

def get_codes2():
	codes = []
	with open("codes.txt", "r") as f:
		for l in f.readlines():
			line = l.strip()
			if line!="":
				codes.append(line)
	return codes

def save_code(c):
	with open("codes.txt", "a") as f:
		f.write(c+"\n")
	with open("allcodes.txt", "a") as f:
		f.write(c+"\n")

def delete_code(c):
	codes = get_codes2()
	codes.pop(codes.index(c))
	with open("codes.txt", "w") as f:
		f.truncate()
		# print(codes)
		text = ""
		for i in codes:
			text += i+"\n"
		f.write(text)

def generate_code():
	while True:
		code = random.choice(NUMBERS) + random.choice(NUMBERS) + random.choice(NUMBERS) + random.choice(SYMBOLS) + random.choice(SYMBOLS) + random.choice(SYMBOLS) + random.choice(LETTERS) + random.choice(LETTERS)
		if code not in get_codes():
			break
	return code

def validate_code(c):
	return (c in get_codes())

def checknotused(c):
	return (c in get_codes2())

def validate_code_and_activate(c, user):
	if checknotused(c):
		with open(f"user_{user}.txt", "a+") as f:
			if c not in get_user(user):
				f.write(c+"\n")
			else:
				return False
		delete_code(c)
		return True
	return False

def validate_username(u):
	for i in u:
		if u not in VALIDATE:
			return False
	return True
'''
!!!!Hey Guys!!!!
You're a good programmer?
Wanna test your knowledge?
If so, join cryptogame!
You will have your own online wallet with hackercoins.
You have to hack cipher and get hackercoins.
Cryptogame is open source project, so if you understand python,
you can look inside the code and find out the weakness of encrypting.

Source code: 
'''
if __name__ == '__main__':
	for i in range(10):
		c = generate_code()
		save_code(c)
		print(c)
	# print(validate_code_and_activate(get_codes2()[0], "nikita"))