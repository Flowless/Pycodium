#!/usr/bin/python

#from file.py import *
from cryptography.fernet import Fernet
import sys

def encrypt():
	print("You have chosen Encryption. AES_128_CBC_PKCS7 is used.")
	inp = None
	while not inp: 
		inp = raw_input('File for encryption: ')
	output = raw_input('Output: ')
	if not output:
		print("STDOUT is used for output.")
	#Key-generate, Base64-encoded, SECRET, SYMMETRIC ENCRYPTION
	for i in range(0,9):
		key = Fernet.generate_key()
		print(key)
	#Creates a Fernet-object with the given key
	f = Fernet(key)
	#Creates the token (the enc content)
	token = f.encrypt(b"this is super secret")

def decrypt():
	print("You have chosen Decryption. AES_128_CBC_PKCS7 will be decrypted.")
	inp = None
	while not inp: 
		inp = raw_input('File for encryption: ')
	output = raw_input('Output: ')
	if not output:
		print("STDOUT is used for output.")

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
print("    Use --help for help.")
print(" ")
print("[1] Encryption")
print("[2] Decryption")
print("[0] Exit")

ans = input('Option: ')

switch(ans)







