#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("Welcome to the Dice Game!")

while True:
    # Set the target number
    target = random.randint(2, 12)
    print(f"The target number is {target}.")
    
    # Get the player's guess
    guess = input("Will the sum of the dice be higher or lower than the target number? [higher/lower]: ")
    
    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("You rolled", dice1, "and", dice2, ". The total is", total)
    
    # Compare the total with the target number and determine the outcome
    if total == target:
        print("It's a tie!")
    elif (total > target and guess == 'higher') or (total < target and guess == 'lower'):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")
    
    play_again = input("Do you want to play again? [yes/no]: ")
    if play_again != 'yes':
        break

print("Thank you for playing!")
     


# In[ ]:




