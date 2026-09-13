account_name = "Juan Dela Cruz"
account_number = "20260001"
balance = 10000.00
transactions = []
 
 
while True:
    print()
    print("===== PYTHON CLI ATM by POSTANES =====")
    print(f"Welcome, {account_name}!")
    print()
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
 
 
    choice = input("Choose an option: ")
 
 
    # TODO 1: Check Balance
    if choice == "1":
        print(f"Current Balance: ₱{balance:.2f}")
 
 
    # TODO 2: Deposit
    elif choice == "2":
        deposit = float(input("\nEnter deposit amount: "))
 
 
        # TODO 3: Validate the deposit
        if deposit > 0:
            # TODO 4: Add deposit to balance
            balance += deposit
 
 
            # TODO 5: Add transaction to the list
            transactions.append(f"Deposit: ₱{deposit:.2f}")
 
 
            print("Deposit successful.")
            print(f"New Balance: ₱{balance:.2f}")
        else:
            print("Invalid deposit amount.")
 
 
    # TODO 6: Withdraw
    elif choice == "3":
        withdraw = float(input("\nEnter withdrawal amount: "))
 
 
        # TODO 7: Validate withdrawal
        if 0 < withdraw <= balance:
            # TODO 8: Deduct withdrawal
            balance -= withdraw
 
 
            # TODO 9: Add transaction to the list
            transactions.append(f"Withdrawal: ₱{withdraw:.2f}")
 
 
            print("Withdrawal successful.")
            print(f"Remaining Balance: ₱{balance:.2f}")
        else:
            print("Invalid withdrawal amount.")
 
 
    # TODO 10: Display transaction history
    elif choice == "4":
        print()
        print("===== TRANSACTION HISTORY =====")
 
 
        # TODO 11: Use a for loop to display every transaction
        for transaction in transactions:
            print(transaction)
 
 
    # TODO 12: Exit
    elif choice == "5":
        print("\nThank you for using Python CLI ATM.")
 
 
        # TODO 13: Stop the ATM loop
        break
 
 
    # TODO 14: Handle invalid menu choices
    else:
        print("Invalid option.")

## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 26, 2026
 
## Program Description: This program displays the ATM.
## Reflection: I learned ﻿﻿﻿﻿how to use everything I've learned so far.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""
