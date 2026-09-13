# TODO 1: Open transactions.txt using read mode
file = open("transactions.txt", "r", encoding="utf-8")


# TODO 2: Read all lines from the file
lines = file.readlines()
 
print("===== TRANSACTION HISTORY =====")
 
 
# TODO 3: Use a for loop to process every line
for line in lines:
    print(line.strip())

# TODO 4: Close the file
file.close()

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 27, 2026
 
## Program Description: This program reads transaction history.
## Reflection: I learned ﻿﻿﻿﻿how to read a file.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
