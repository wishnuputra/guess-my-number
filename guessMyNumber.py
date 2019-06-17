# -*- coding: utf-8 -*-
"""
===============================================
Exercise 3 Lecture 3
Guess My Number
===============================================

This program will guess a number from 0 to 
100(not inclusive), thank you think of.

It will guess the number using bisection search.

Created on Mon Jun 17 16:34:09 2019

@author: Wishnuputra
===============================================
"""

low = 0
high = 100
guess = (low + high) // 2
ans = ''
prompt = "Enter 'h' to indicate the guess is too high, Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."

print("Please think of a number between 0 and 100!")

while True:
    print("Is you secret number %i?" %(guess))
    
    while True:
        ans = input(prompt)
        if  ans == 'h' or ans == 'l' or ans == 'c':
            break
        else:
            print("Sorry, I did not understand your input.")
            print("Is you secret number %i?" %(guess))
            
    if ans == 'c':
        print("Game Over. Your secret number was:", guess)
        break
    elif ans == 'l':
        low = guess
        guess = (low + high) // 2
        
    elif ans == 'h':
        high = guess
        guess = (low + high) // 2