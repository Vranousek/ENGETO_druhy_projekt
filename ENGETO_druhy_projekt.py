"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Vrána
email: deny.vrana@gmail.com
discord: vranousek
"""

import random
import time 

def generate_secret_number():
    while True:
        number = random.sample('1234567890', 4)  
        if number[0] != '0': 
            return ''.join(number)

def is_valid_guess(guess):
    if len(guess) != 4:
        return False
    if not guess.isdigit(): 
        return False
    if len(set(guess)) != 4: 
        return False
    if guess[0] == '0': 
        return False
    return True

def evaluate_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def print_bulls_and_cows(bulls, cows):
    if bulls == 1:
        print("1 bull", end=", ")
    else:
        print(f"{bulls} bulls", end=", ")
    
    if cows == 1:
        print("1 cow")
    else:
        print(f"{cows} cows")

def play_game():
    secret_number = generate_secret_number()
    attempts = 0
    
 
    start_time = time.time()
    
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    
    while True:
        guess = input("Enter a number: ")
        attempts += 1
        
        if not is_valid_guess(guess):
            print("Invalid guess. The number must be 4 digits, unique digits, and cannot start with 0.")
            continue
        
        bulls, cows = evaluate_guess(secret_number, guess)
        
        print_bulls_and_cows(bulls, cows)
        
        if bulls == 4:
        
            end_time = time.time()
            elapsed_time = end_time - start_time 
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"Time taken: {elapsed_time:.2f} seconds")
            if attempts == 1:
                print("That's amazing!")
            elif attempts <= 5:
                print("That's average!")
            else:
                print("That's not so good...")
            break
play_game()
