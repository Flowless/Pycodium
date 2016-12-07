#!/usr/bin/python

from cryptography.fernet import Fernet
import sys

def menu():
	print("----------------------------")
	print("|   Flowless' Pycryptium   |")
	print("----------------------------")

def readfile(inp):
	file = open(inp, 'r')
	content = str(file.readlines())
	file.close()
	return content

def writefile(path, text):
	file = open(path, 'w')
	file.write(text)
	print("Written --> " + path)
	file.close()

def encrypt():
	menu()
	print("You have chosen Encryption. AES_128_CBC_PKCS7 is used.")
	inp = sys.argv[2]
	#Key-generate, Base64-encoded, SECRET, SYMMETRIC ENCRYPTION
	key = Fernet.generate_key()
	## KEY is written to def.skey
	writefile("def.skey", key)
	#Creates a Fernet-object with the given key
	f = Fernet(key)
	#Creates the token (the enc content)
	token = f.encrypt(readfile(inp))
	out = None
	while not out:
		out = raw_input('Path for output_content: ')
	writefile(out, token)
	print("CHECK_Decrypt: " + f.decrypt(token))

def decrypt():
	menu()
	print("You have chosen Decryption. AES_128_CBC_PKCS7 will be decrypted.")
	# File to decrypt is argument after option
	inp = sys.argv[2]
	# Makes sure that secret key file is given
	d_key = None
	while not d_key:
		d_key = raw_input('File for secret_key: ')
	#catches the key from path given above
	key = readfile(d_key)
	print("Secret key: " + key + "\n")
	#create Fernet-object with key
	f = Fernet(key)
	#catches token from created file
	token = readfile(inp)
	print("Encrypted: " + token + "\n")
	# decrypts intended stuffs
	print("Decrypted: " + f.decrypt(token) )

def init():
	if (sys.argv[1] == '-e'):
		encrypt()
	elif (sys.argv[1] == '-d'):
		decrypt()
	else:
		print("Invalid option or no file given.")

	sys.exit()
