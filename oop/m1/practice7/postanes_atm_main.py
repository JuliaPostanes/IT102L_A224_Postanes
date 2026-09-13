import postanes_atm_balance
import postanes_atm_deposit
import postanes_atm_history
import postanes_atm_analysis

account_name = "Juan Dela Cruz"
balance = 10000.00
 
 
print("==============================")
print("  PYTHON CLI ATM by POSTANES")
print(f"  Welcome, {account_name}!")
print("==============================")
 
 
print()
print("===== ATM MENU by POSTANES =====")
print("1. Check Balance")
print("2. Deposit")
print("3. View History")
print("4. Analyze Transactions")
 
choice = input("Choose option: ")
 
 
if choice == "1":
    postanes_atm_balance.check_balance(balance)
 
 
elif choice == "2":
    balance = postanes_atm_deposit.deposit_money(balance, account_name)

 
elif choice == "3":
    postanes_atm_history.view_history()
 
elif choice == "4":
    postanes_atm_analysis.analyze_transactions()
 

else:
    print("Invalid Option.")


## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 28, 2026
 
## Program Description: This program displays the Main ATM Module.
## Reflection: I learned how to import the ATM modules, and storing the account information.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
## """
## """ 
######### Learning Signature ######### 
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: August 28, 2026
 
## Program Description: This program displays the Main ATM Module.
## Reflection: I learned how to import the ATM modules, and storing the account information.
 
## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
## """
