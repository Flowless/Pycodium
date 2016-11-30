#!/usr/bin/python
#from file.py import *
from cryptography.fernet import Fernet
import sys

def readfile(inp):
	file = open(inp, 'r')	
	content = str(file.readline())
	file.close()
	return content	

def writefile(path, text):
	file = open(path, 'w')
	file.write(text)
	print("Key --> " + path)
	file.close()

def encrypt():
	print("You have chosen Encryption. AES_128_CBC_PKCS7 is used.")
	inp = None
	while not inp: 
		inp = raw_input('String for encryption: ')
	#Key-generate, Base64-encoded, SECRET, SYMMETRIC ENCRYPTION
	key = Fernet.generate_key()
	## KEY is written to def.skey
	writefile("def.skey", key)	
	#Creates a Fernet-object with the given key
	f = Fernet(key)
	#Creates the token (the enc content)
	token = f.encrypt(inp)	
	out = None
	while not out: 
		out = raw_input('Path for output_content: ')
	writefile(out, token)
	print("CHECK_Decrypt: " + f.decrypt(token))

def decrypt():
	print("You have chosen Decryption. AES_128_CBC_PKCS7 will be decrypted.")
	# Makes sure that decrypt-file is given
	inp = None
	while not inp: 
		inp = raw_input('File for decryption: ')
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
	print("Encrypted: " + token)
	# decrypts intended stuffs
	print("DECRYPTION: " + f.decrypt(token) )

def switch(x):
	if (x == 1):
		encrypt()
	elif (x == 2):
		decrypt()
	else:
		print("Quitting..")
		sys.exit()


print("----------------------------")
print("|   Flowless' Pycryptium   |")
print("----------------------------")
print(" ")
print("[1] Encryption")
print("[2] Decryption")
print("[0] Exit")
ans = input('Option: ')

switch(ans)

sys.exit()
