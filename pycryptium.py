#!/usr/bin/python

#from file.py import *
import sys

def encrypt():
	print("You have chosen Encryption. AES will be used.")
	inp = None
	while not inp: 
		inp = raw_input('File for encryption: ')
	output = raw_input('Output: ')
	if not output:
		print("STDOUT is used for output.")

def decrypt():
	print("You have chosen Decryption. AES will be decrypted.")
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







