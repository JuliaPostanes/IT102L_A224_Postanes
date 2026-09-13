def deposit_money(current_balance, account_name):
    try:            
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            new_balance = current_balance + amount
            file = open("transactions.txt", "a", encoding="utf-8")
            file.write(f"Account: {account_name}\n")
            file.write("Transaction: Deposit\n")
            file.write(f"Amount: ₱{amount:.2f}\n")
            file.close()
                
            print("Deposit successful.")
            print(f"New Balance: ₱{new_balance:.2f}")
            return new_balance
        else:
            print("Invalid deposit amount.")
            return current_balance
    except ValueError:
            print("Invalid input. Please enter a valid number.")
            return current_balance
## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 28, 2026
 
## Program Description: This program displays the Main ATM Deposit module.
## Reflection: I learned how to use function parameters, try-except,
        #           ValueEError, txt file processing, return and local
        #                   variables.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
## """
## """ 
