# Stuff that happens before anything is defined
import random
import time
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
    
