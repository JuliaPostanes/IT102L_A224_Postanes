transactions = [
    "Deposit: ₱5000",
    "Withdrawal: ₱1000",
    "Deposit: ₱2000",
    "Withdrawal: ₱500"
]
 
print("===== TRANSACTION SUMMARY =====")
 
for transaction in transactions:
    # TODO 1: Check if the transaction contains "Deposit"
    if "Deposit" in transaction:
        print(f"Deposit Transaction → {transaction}")
 
    # TODO 2: Otherwise, check for "Withdrawal"
    elif "Withdrawal" in transaction:
        print(f"Withdrawal Transaction → {transaction}")
 
    # TODO 3: Handle other transaction types
    else:
        print(f"Other Transaction → {transaction}")
## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 26, 2026
 
## Program Description: This program displays the transaction summary.
## Reflection: I learned ﻿﻿﻿﻿how to combine a list, for loop, and conditions.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
