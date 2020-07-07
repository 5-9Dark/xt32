#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

import os, sys

# define color class
class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
    
# define clean src
def clearScr():
    os.system('clear')
    
### main ###

alphabet = 'ABCDEFHIJKLMNOPQRSTUVWXYZabcdefhijklmnopqrstuvwxyz 1234567890?><!@#$%^&*():.,;-_'
dic = dict(zip(alphabet, range(82)))
dic2 = {v: k for k, v in dic.items()}

def str_encode():
    string = input(color.RED + "[-]" + color.END + " String to encode: ")
    key = int(input(color.RED + "[-] " + color.END + "Key to string: "))
    list = (dic[x] for x in string)
    encodeNums = ((x + key) % 82 for x in list)
    encodeStr = (dic2[x] for x in encodeNums)
    print("Your cypher is: " + color.IMPORTANT)
    print("".join(encodeStr))
    print("" + color.END)
def str_decode():
    string = input("String to decode: ")
    key = int(input("key to string: "))
    print("[*] Trying basic salt..\n")
    list = (dic[x] for x in string)
    decodeNums = ((x + -key) % 82 for x in list)
    decodeStr = (dic2[x] for x in decodeNums)
    print("".join(decodeStr))
    
### run time ###
clearScr()
print("""
[---------- Welcome to the xt32 encoder by 5/9Dark. ------------]       
|                                                               |    
|   * Make sure to set shift!                                   |
|                                                               |
|                                                               |
|             1.) Encode              2.) Decode                |
|                                                               |
|                  [ (C) 2020 FiveNineDark ]                    |
]---------------------------------------------------------------]\n\n\n\n""")

typeofshift = input("[*] Type: ")
if typeofshift == "1":
    str_encode()
elif typeofshift == "2":
    str_decode()
