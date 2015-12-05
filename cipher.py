# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:07:40 2015

@author: Isaac
"""

def cipher(p, n, k):
    return (n*p+k)%26

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

plaintext = ""
while not (plaintext=="exit"):
    plaintext = input("New plaintext:")
    n=int(input("Cipher parameters?<n>x"))
    k=int(input("Cipher parameters?+<k>"))
    p = []
    c = []
    ciphertext = ""
    for letter in plaintext:
        p.append(alpha.index(letter.lower()))
        c.append(cipher(p[len(p)-1],n,k))
        ciphertext += alpha[c[len(c)-1]]
    print(ciphertext)
    
