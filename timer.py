"""
 This program is for MGTC28's in-class exercise 4: Nerve of Steel game.
 The code is modified from the forked timer.py project by Lazigerbill.
 This is a simple Python script that will first display the words "Players stand",
 then sleep for a random time between 5 to 25 seconds. During this time, players can sit down.
 When sleep is over, the program displays "Time Up. Last to sit down wins."

 
"""

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random # The random library has a function that returns a random floating point number between a and b inclusive.

# Display the words "Players stand"
print("Players stand")

# Generate a random floating point number between 5.0 and 25.0 inclusive and set that as the sleep time. 
set_time = random.uniform(5.0, 25.0)

# Make the program sleep for the set amount of time.
time.sleep(set_time)

# Print "Time Up. Last to sit down wins." once the program finishes sleeping.
print("Time Up. Last to sit down wins.")

