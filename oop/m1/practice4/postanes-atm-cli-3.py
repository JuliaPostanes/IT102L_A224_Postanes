balance = 10000.00
 
while True:
    print()
    print("===== PYTHON CLI ATM by POSTANES =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
 
 
    choice = input("Choose an option: ")
 
 
    # TODO 1: Check Balance
    if choice == "1":
        print(f"Current Balance: ₱{balance:.2f}")
 
 
    # TODO 2: Display a message for Deposit
    elif choice == "2":
        print("Deposit selected.")
 
 
    # TODO 3: Display a message for Withdraw
    elif choice == "3":
        print("Withdraw selected.")
 
 
    # TODO 4: Exit the loop
    elif choice == "4":
        print("Thank you for using Python CLI ATM.")
        break
 
 
    # TODO 5: Handle invalid choices
    else:
        print("Invalid option.")
## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 26, 2026
 
## Program Description: This program displays the ATM Menu.
## Reflection: I learned ﻿﻿﻿﻿that while loop is very useful when repetition 
##                      depends on a condition.
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
## ﻿"""

