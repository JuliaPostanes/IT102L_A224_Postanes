def analyze_transactions():
    file = open("transactions.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()

    
    deposit_count = content.count("Deposit")


    first_deposit = content.find("Deposit")

    print("===== TRANSACTION ANALYSIS =====")


    print(f"Total Deposits: {deposit_count}")


    print(f"First Deposit Index: {first_deposit}")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 4, 2026
 
## Program Description: This program displays the Transaction Analysis.
## Reflection: I learned ﻿﻿﻿﻿how to create a separate analysis module.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
