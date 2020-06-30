#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

import os, sys, argparse

# define char,num Aa-Zz 0-9
charA = '01000001'
charB = '01000010'
charC = '01000011'
charD = '01000100'
charE = '01000101'
charF = '01000110'
charG = '01000111'
charH = '01001000'
charI = '01001001'
charJ = '01001010'
charK = '01001011'
charL = '01001100'
charM = '01001101'
charN = '01001110'
charO = '01001111'
charP = '01010000'
charQ = '01010001'
charR = '01010010'
charS = '01010011'
charT = '01010100'
charU = '01010101'
charV = '01010110'
charW = '01010111'
charX = '01011000'
charY = '01011001'
charZ = '01011010'

chara = '01100001'
charb = '01100010'
charc = '01100011'
chard = '01100100'
chare = '01100101'
charf = '01100110'
charg = '01100111'
charh = '01101000'
chari = '01101001'
charj = '01101010'
chark = '01101011'
charl = '01101100'
charm = '01101101'
charn = '01101110'
charo = '01101111'
charp = '01110000'
charq = '01110001'
charr = '01110010'
chars = '01110011'
chart = '01110100'
charu = '01110101'
charv = '01110110'
charw = '01110111'
charx = '01111000'
chary = '01111001'
charz = '01111010'

num0 = '0'
num1 = '1'
num2 = '10'
num3 = '11'
num4 = '100'
num5 = '101'
num6 = '110'
num7 = '111'
num8 = '1000'
num9 = '1001'

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


def str_encode():
    
    
def str_decode():


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
