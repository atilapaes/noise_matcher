#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:58:23 2024
@author: atilapaes

REC: Record audio with default or personalized parameters.
"""


print('Initializing REC...')
status = input("Press R to start recording? ")
status = status.lower()

while status != 'r':
    status = input("Input invalid. Press R to start recording: ")
    status = status.lower()


status = input("Recording. Press S to stop recording: ")
status = status.lower()

while status != 's':
    status = input("Input invalid. Press R to start recording: ")
    status = status.lower()

print('Recording stopped')
