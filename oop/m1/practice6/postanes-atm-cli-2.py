balance = 10000.00 
 
# TODO 1: Create a function named deposit_money() 
# Parameters: 
# current_balance 
# amount

def deposit_money(current_balance, amount):
    return current_balance + amount
 
deposit = float(input("Enter deposit amount: ")) 
 
# TODO 2: Check if the deposit is valid 
if deposit > 0: 
 
# TODO 3: Call deposit_money() 
# Store the returned value in balance

    balance = deposit_money(balance, deposit)
    print("Deposit successful.") 
    print(f"New Balance: ₱{balance:.2f}") 
 
else: 
   print("Invalid deposit amount.")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 27, 2026
 
## Program Description: This program displays the deposit function with return.
## Reflection: I learned ﻿﻿﻿﻿how to use functions with parameters, arguments,
##                  return, and arithmetic inside a function.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
