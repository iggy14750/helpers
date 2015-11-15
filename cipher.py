# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:07:40 2015

@author: Isaac
"""

def cipher(p):
    return (3*p+4)%26

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

plaintext = ""
while not (plaintext=="exit"):
    plaintext = input("New plaintext:")
    p = []
    c = []
    ciphertext = ""
    for letter in plaintext:
        p.append(alpha.index(letter.lower()))
        c.append(cipher(p[len(p)-1]))
        ciphertext += alpha[c[len(c)-1]]
    print(ciphertext)
    