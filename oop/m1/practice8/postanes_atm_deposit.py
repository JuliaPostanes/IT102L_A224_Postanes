def deposit_money(account):
    try:
        raw = input("Enter deposit amount: ")
        amount = float(raw)
        if amount > 0:
            if account.deposit(amount):
                with open("transactions.txt", "a", encoding="utf-8") as file:
                    file.write(f"Account: {account.account_name}\n")
                    file.write("Transaction: Deposit\n")
                    file.write(f"Amount: ₱{amount:.2f}\n")

                print("Deposit successful.")
                print(f"New Balance: ₱{account._balance:.2f}")
                account.check_balance()
            else:
                print("Deposit failed.")
        else:
            print("Invalid deposit amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 4, 2026
 
## Program Description: This program displays the current balance.
## Reflection: I learned ﻿﻿﻿﻿how to create the main program by importing an Account
##              class, object, and displaying the account information, ATM Menu,
##              and accepts the user's menu choice.
 
## AI Usage
## [ ] No AI Assistance – Completed independently without AI.
## [/] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""

## AI USE: I was having trouble to get it running because of the txt file. AI helped me solve it.
