# Stuff that happens before anything is defined
import random
import time
import webbrowser

playablegames = "Coin flip, Roshambo, and Roulette"
money = 20
loop = True

# The games you can play (to make money)
def Coin_Flip(wage):
    global money
    money = money - wage
    coin_states = ["Heads", "Tails"]        
    choice = input("Pick one. Heads, Or Tails: ").strip().title() 
    
    if choice == "Heads":
        coin_real_state = random.choice(coin_states)
        if coin_real_state == "Heads":
            # Player wins: give back their original bet + 1x profit
            money = money + (wage * 2)
            print(f"Great job! Your new balance is ${money}.")
            return money 
        elif coin_real_state == "Tails":
            print(f"Womp womp! You lost your wager!")
            if money <= 0: 
                time.sleep(1)
                print("It appears you are broke now. We'll give you an extra 20 dollars so you can keep trying!")
                money = money + 20
            return money
            
    elif choice == "Tails":
        coin_real_state = random.choice(coin_states)
        if coin_real_state == "Tails":
            money = money + (wage * 2)
            print(f"Great job! Your new balance is ${money}.")
            return money
        elif coin_real_state == "Heads":
            time.sleep(1)
            print(f"Womp womp! You lost your wager! Your new balance is {money}")
            if money <= 0:
                time.sleep(1)
                print("It appears you are broke now. We'll give you an extra 20 dollars so you can keep trying!")
                money = money + 20
            return money

def Roulette(wage):
    global money
    money = money - wage
    red_spots = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    black_spots = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    spts = ["black", "red"]
    time.sleep(1)
    choice = input("Which one do you want? Black, or Red, or do you want a number? \nGuess the right number and your wage increases 4 fold. Get it wrong, and your balance is divided by four. ").strip().lower()
    
    if choice == "black":
        sptchoice = random.choice(spts)
        if sptchoice == "black":
            numberchoice = random.choice(black_spots)
            money = money + (wage * 2) # Win: return original bet + 1x profit
            print(f"Great job brother. Your money has doubled now to ${money}. What was chosen was a {sptchoice} {numberchoice}.")
        else:
            numberchoice = random.choice(red_spots)
            print(f"Ooooh...Not the greatest pick bud. You lost your wager. Balance: ${money}. What was chosen was {sptchoice} {numberchoice}.")
        return money
        
    elif choice == "red":
        sptchoice = random.choice(spts)
        if sptchoice == "red":
            numberchoice = random.choice(red_spots)
            money = money + (wage * 2)
            print(f"Great job brother. Your money has doubled now to ${money}. What was chosen was a {sptchoice} {numberchoice}.") 
        else:
            numberchoice = random.choice(black_spots)
            print(f"Ooooh...Not the greatest pick bud. You lost your wager. Balance: ${money}. What was chosen was {sptchoice} {numberchoice}.")
        return money  
        
    elif choice.isdigit():
        choice_num = int(choice)
        sptchoice = random.choice(spts)
        if sptchoice == "black":
            numberchoice = random.choice(black_spots)
        else:
            numberchoice = random.choice(red_spots)
            
        if choice_num == numberchoice or choice_num == numberchoice - 2 or choice_num == numberchoice + 2:
            money = money + (wage * 4)
            print(f"Amazing bet. Your balance has quadrupled to ${money}!")
        else:
            print(f"Not the greatest choice...Your balance is ${money}. What was chosen was a {sptchoice} {numberchoice}.")
        return money

def Roshambo(wage):
    global money
    money = money - wage
    clankachoice = ["Rock", "Paper", "Scissors"]
    
    roshambochoice = input("Alright, which do you want? Rock, Paper, or Scissors? ").lower().strip().title()
    rpschoice = random.choice(clankachoice)
    print(f"You picked {roshambochoice}, Dealer picked {rpschoice}.")
    
    if roshambochoice == rpschoice:
        # Tie scenario: Return original wager + half benefit profit (total 1.5x)
        money = money + round(wage * 1.5)
        print(f"Lucky, Lucky you! You both picked the same thing, so you get half the benefit. New balance: ${money}")
    elif (roshambochoice == "Rock" and rpschoice == "Scissors") or \
         (roshambochoice == "Scissors" and rpschoice == "Paper") or \
         (roshambochoice == "Paper" and rpschoice == "Rock"):
        # Player wins: Return original wager + 1x profit
        money = money + (wage * 2)
        print(f"On your A game eh? You won, and your new balance is ${money}!")
    else:
        # Player loses: Do not give back any money
        print(f"Can't beat my hand. You lost, and your balance is ${money}")
    return money

def CasinoWar(wage):
    global money   
    money = money - wage
    playercards = list(range(1, 53))
    dealercards = list(range(1, 53))
    print("Alrighty, I'm going to shuffle for a bit and hand you a card...")
    time.sleep(3)

# The console stuff
oneandonlychoice = input(f"Welcome to the casino kid. The only games we have so far is the {playablegames}. Wanna play, or go to settings? \n(type 'coinflip' for coinflip, 'roulette' for roulette, 'roshambo' for roshambo, and 'settings' for settings) ").strip().lower()

if oneandonlychoice in ["coinflip", "coin flip"]:
    time.sleep(1)
    print("Coin Flip, nice choice.")
    
    while loop is True:
        time.sleep(1)
        wageask = input("How much you want to wager? ")
        if wageask.isdigit(): 
            wage_number = int(wageask) 
            if money - wage_number < 0:
                print("Try a lower number, you can't wage that much.")
            else:
                money = Coin_Flip(wage_number)  
                loop = False     
        else:
            time.sleep(1)
            print("Sorry kid, I don't speak letters for wage. Try again!")
            
elif oneandonlychoice == "roulette":
    while loop is True:
        time.sleep(1)
        wageask = input("How much you want to wager? ")
        if wageask.isdigit(): 
            wage_number = int(wageask) 
            if money - wage_number < 0:
                print("Try a lower number, you can't wage that much.")
            else:
                money = Roulette(wage_number)
                loop = False     
        else:
            time.sleep(1)
            print("Sorry kid, I don't speak letters for wage. Try again!")
            
elif oneandonlychoice == "roshambo":
    while loop is True:
        time.sleep(1)
        wageask = input("How much you want to wager? ")
        if wageask.isdigit(): 
            wage_number = int(wageask) 
            if money - wage_number < 0:
                print("Try a lower number, you can't wage that much.")
            else:
                money = Roshambo(wage_number)
                loop = False     
        else:
            time.sleep(1)
            print("Sorry kid, I don't speak letters for wage. Try again!")

print(f"With this game choice your new balance is ${money}!")
time.sleep(1)
print("You have four more rounds before we sadly have to kick you out.")
# To extend gameplay, you can place this game selector block inside a master while loop!
secondandonlychoice = input(f"Alrighty, whats your choice of games? {playablegames} is what you can currently play. ")

import webbrowser
import os

playablegames = "Coin flip, and Roulette"
money = 20
loop = True

# The games you can play (to make money)
def Coin_Flip(wage):
    money - wage
    coin_states = ["Heads", "Tails"]        
    choice = input("Pick one. Heads, Or Tails: ").strip().title() 
    
    if choice == "Heads":
        coin_real_state = random.choice(coin_states)
        if coin_real_state == "Heads":
            new_wage = wage * 2 
            time.sleep(1)
            print(f"Great job! Your new balance is {new_wage}.")
            money + wage
            return money 
        elif coin_real_state == "Tails":
            new_wage = wage / 2
            time.sleep(1)
            print(f"Womp womp! You just halfed your wage!")
            if new_wage <= 0: 
                time.sleep(1)
                print("It appears you are broke now. We'll give you an extra 20 dollars so you can keep trying!")
                new_wage = wage + 20
                money + wage
                return money
            else:
                money + wage
                return money
    elif choice == "Tails":
        coin_real_state = random.choice(coin_states)
        if coin_real_state == "Tails":
            new_wage = wage * 2 
            time.sleep(1)
            print(f"Great job! Your new balance is {new_wage}.")
            money + wage
            return money
        elif coin_real_state == "Heads":
            new_wage = wage / 2
            time.sleep(1)
            print(f"Womp womp! You just halfed your wage!")
            if new_wage <= 0:
                time.sleep(1)
                print("It appears you are broke now. We'll give you an extra 20 dollars so you can keep trying!")
                new_wage = wage + 20
                money + new_wage
                return money
            else:
                money + new_wage
                return money

def Roulette(wage):
    money - wage
    red_spots = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    black_spots = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    spts = ["black", "red"]
    time.sleep(1)
    choice = input("Which one do you want? Black, or Red, or do you want a number?").strip().lower()
    if choice == "black":
        sptchoice = random.choice(spts)
        if sptchoice == "black":
            numberchoice = random.choice(black_spots)
        elif sptchoice == "red":
            numberchoice = random.choice(red_spots)
        if sptchoice == "black":
            wage * 2
            time.sleep(3)
            print(f"Great job brother. Your money has doubled now to ${money}. What was chosen was a {sptchoice} {numberchoice}.")
            money + wage 
            return money
        else:
            wage / 2
            time.sleep(3)
            print(f"Ooooh...Not the greatest pick bud. Your money has now halfed to ${money}. What was chosen was {sptchoice} {numberchoice}.")
            money + wage
            return money
    elif choice == "red":
        sptchoice = random.choice(spts)
        if sptchoice == "black":
            numberchoice = random.choice(black_spots)
        elif sptchoice == "red":
            numberchoice = random.choice(red_spots)
        if sptchoice == "red":
            wage * 2
            time.sleep(3)
            print(f"Great job brother. Your money has doubled now to ${money}. What was chosen was a {sptchoice} {numberchoice}.")
            money + wage 
            return money
        else:
            wage / 2
            time.sleep(3)
            print(f"Ooooh...Not the greatest pick bud. Your money has now halfed to ${money}. What was chosen was {sptchoice} {numberchoice}.")
            money + wage
            return money  
            
            
# The console stuff
oneandonlychoice = input(f"Welcome to the casino kid. The only game we have so far is the {playablegames}. Wanna play, cash out what you got, or go to settings? ").strip().lower()

if oneandonlychoice == "coinflip" or oneandonlychoice == "coin flip":
    time.sleep(1)
    print("Coin Flip, nice choice.")
    loop = True

    # --- HERE IS THE LOOP TO ASK REPEATEDLY ---
    while loop is True:
        time.sleep(1)
        wageask = input("How much you want to wager? ")
        int(wageask)
        int(money)
        if wageask.isdigit(): # FIXED: Added () to make .isdigit() actually work
            wage_number = int(wageask) # Convert the text into a real number for math
            if money - wage_number < 0:
                print("Try a lower number, you can't wage that much.")
                loop = True
            else:  
                money + wage_number 
                Coin_Flip(wage_number)
                loop = False     # Send the number to your game function
        else:
            time.sleep(1)
            print("Sorry kid, I don't speak letters for wage. Try again!")
elif oneandonlychoice == "roulette":
    while loop is True:
        time.sleep(1)
        wageask = input("How much you want to wager? ")
        int(wageask)
        if wageask.isdigit(): # FIXED: Added () to make .isdigit() actually work
            wage_number = int(wageask) # Convert the text into a real number for math
            if money - wage_number < 0:
                print("Try a lower number, you can't wage that much.")
                loop = True
            else:  
                money + wage_number 
                Roulette(wage_number)
                loop = False     # Send the number to your game function
        else:
            time.sleep(1)
            print("Sorry kid, I don't speak letters for wage. Try again!")
elif oneandonlychoice == "settings":
    settingschoice = input("The only thing we can offer you so far is a song change. Paste in the url you want, and we'll play it. \nAn example of this would be 'https://youtube.com ")
    webbrowser.open_new_tab(settingschoice)
elif oneandonlychoice == "cashout":
    print(f"Alrighty you walk away with ${money}. Nice. Goodbye!")
    
