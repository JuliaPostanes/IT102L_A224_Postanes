# TODO 1:
# Create analyze_transactions().
 
def analyze_transactions():
 
    # TODO 2:
    # Open transactions.txt
    # using read mode.
    file = open("transactions.txt", "r", encoding="utf-8")
 
    # TODO 3:
    # Read the entire file.
    content = file.read()

 
    # TODO 4:
    # Close the file.
    file.close()
 
    # TODO 5:
    # Count how many times "Deposit"
    # appears in the file.
    deposit_count = content.count("Deposit")
 
    # TODO 6:
    # Find the position of the first
    # occurrence of "Deposit".
    first_deposit = content.find("Deposit")
 
    print("===== TRANSACTION ANALYSIS =====")
 
    # TODO 7:
    # Display the total number of deposits.
    print(f"Total Deposits: {deposit_count}")
 
    # TODO 8:
    # Display the first Deposit index.
    print(f"First Deposit Index: {first_deposit}")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 26, 2026
 
## Program Description: This program displays the analyzed transactions.
## Reflection: I learned ﻿﻿﻿﻿how to use read(). count(), and find().
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
