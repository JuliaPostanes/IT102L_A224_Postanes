def view_history():
    file = open("transactions.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
 
    print("===== TRANSACTION HISTORY =====")

    for line in lines:
        print(line.strip())
 
## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 4, 2026
 
## Program Description: This program displays the transaction history
## Reflection: I learned ﻿﻿﻿﻿how to create a separate module that reads transaction
##                  records from transaction.txt.

## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
