file = open("transactions.txt", "r") 
content = file.read() 
file.close() 
 
# TODO 1: Count how many times "Deposit" appears 
deposit_count = content.count("Deposit")
# TODO 2: Find the first position of "Deposit"
first_deposit = content.find("Deposit")
 
print("===== TRANSACTION ANALYSIS by POSTANES =====") 
print(f"Total Deposits: {deposit_count}") 
print(f"First Deposit Index: {first_deposit}")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 28, 2026
 
## Program Description: This program searches and count transactions.
## Reflection: I learned ﻿﻿﻿﻿how to read the complete contents of the file,
##                  and using count(), find(), and string processing.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
