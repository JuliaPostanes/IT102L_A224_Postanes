
from postanes_atm_account import Account
import postanes_atm_balance as balance
import postanes_atm_deposit as deposit
import postanes_atm_history as history
import postanes_atm_analysis as analysis
## Hello! I used import and followed by "as" because it crashes
##  for some reason when I just used "import". Just a heads up!

account = Account("Juan Dela Cruz", 10000.00)

 
print("==============================")
print("  PYTHON CLI ATM by POSTANES")
print(f"  Welcome, {account.account_name}!")
print("==============================")
 
print()
print("===== ATM MENU by POSTANES =====")
print("1. Check Balance")
print("2. Deposit")
print("3. View History")
print("4. Analyze Transactions")
 
choice = input("Choose option: ")

if choice == "1":
    balance.check_balance(account)
elif choice == "2":
    deposit.deposit_money(account)
elif choice == "3":
    history.view_history()
elif choice == "4":
    analysis.analyze_transactions()
else:
    print("Invalid option.")
    


## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 4, 2026
 
## Program Description: This program displays the current balance.
## Reflection: I learned ﻿﻿﻿﻿how to create the main program by importing an Account
##              class, object, and displaying the account information, ATM Menu,
##              and accepts the user's menu choice.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
