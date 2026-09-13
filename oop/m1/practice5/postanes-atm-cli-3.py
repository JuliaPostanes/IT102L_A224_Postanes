transactions = [
    "Deposit: ₱5000",
    "Withdrawal: ₱1000",
    "Deposit: ₱2000"
]
 
 
print("===== ATM TRANSACTION MANAGER =====")
 
 
# TODO 1: Display the original transaction list
print("Original Transactions:")
print(transactions)

 
# TODO 2: Change the second transaction
# Change "Withdrawal: ₱1000" to "Withdrawal: ₱1200"
transactions[1] = "Withdrawal: ₱1200"
 
 
# TODO 3: Add a new transaction at the end
# Add "Deposit: ₱3000"
transactions.append("Deposit: ₱3000")
 
 
# TODO 4: Insert a transaction at index 1
# Insert "Deposit: ₱1500"
transactions.insert(1, "Deposit: ₱1500")


# TODO MYSELF: Updated Transactions
print("\nUpdated Transactions:")
print(transactions)
 
 
# TODO 5: Display the first three transactions using slicing
print("\nFirst Three Transactions:")
print(transactions[:3])
 
 
# TODO 6: Display the total number of transactions
print(f"\nTotal Transactions: {len(transactions)}")
 
 
# TODO 7: Display the final transaction history
print("\nFinal Transaction History:")
print(transactions)

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 27, 2026
 
## Program Description: This program displays the ATM Transaction Manager
## Reflection: I learned ﻿﻿﻿﻿how to use more indexin, slicing, append(), etc.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""


