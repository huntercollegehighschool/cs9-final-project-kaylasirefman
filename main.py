"""
Name(s): Kayla Sirefman
Name of Project: Hangman
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
#importing the time module 
import time 
def raw_input():
   input("what is your guess:")

name = raw_input
print("Hello, Time to play hangman!") 
print (" ") 
#wait for 1 second 
time.sleep(1) 
print ("Start guessing...") 
time.sleep(0.5) 
word = "secret" 
guesses = '' 
turns = 10 
while turns > 0: 
  failed = 0  
  for char in word:  
    if char in guesses:
      print (char,) 
  else: 
    print ("_",) 
    failed += 1 
    if failed == 0: 
      print ("You won") 
      break 
      print (raw_input) 
      guess = raw_input("guess a character:") 
      guesses += guess 
    if guess () not in word: 
        turns -= 1 
        print ("Wrong ") 
        print ("You have", + turns, 'more guesses')  
    if turns == 0: 
          print ("You Lose ")