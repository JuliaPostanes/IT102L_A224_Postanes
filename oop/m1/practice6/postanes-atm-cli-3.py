account_name = "Juan Dela Cruz"
transaction_type = "Deposit"
amount = 3000

# TODO 1: Open transactions.txt using write mode
file = open("transactions.txt","w", encoding="utf-8")
 
# TODO 2: Write the account name
file.write(f"Account: {account_name}\n")
 
# TODO 3: Write the transaction type
file.write(f"Transaction: {transaction_type}\n")
 
# TODO 4: Write the amount
file.write(f"Amount: ₱{amount}")
 
# TODO 5: Close the file
file.close()
 
print("Transaction saved successfully.")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 27, 2026
 
## Program Description: This program writes the transactions in a txt file.
## Reflection: I learned ﻿﻿﻿﻿how to use a txt file!
 
## AI Usage
## [ ] No AI Assistance – Completed independently without AI.
## [/] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""

## AI USE: I used AI to fix the file=open, because it won't write without the
##          encoding="utf-8" thing.
