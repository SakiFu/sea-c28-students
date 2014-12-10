#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import string


def rot13(str):
    rot13 = string.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(str, rot13)

if __name__ == '__main__':
    assert rot13("ABCDE") == "NOPQR"
    assert rot13("vwxyz") == "ijklm"
    assert rot13("AEKjSCpw") == "NRXwFPcj"
    print ("All Tests Pass")
