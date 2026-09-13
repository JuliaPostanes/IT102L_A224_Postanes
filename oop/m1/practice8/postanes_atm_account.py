class Account:
    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance
 
    def check_balance(self):
        print(f"Current Balance: ₱{self._balance:.2f}")
 
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False


            

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 4, 2026
 
## Program Description: This program displays the current balance before
##                          and after the deposit.
## Reflection: I learned ﻿﻿﻿﻿how to create the Account class that will represent
##                      the ATM account.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
