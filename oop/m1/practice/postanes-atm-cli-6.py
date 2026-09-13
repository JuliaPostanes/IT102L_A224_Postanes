account_name = "Juan Dela Cruz" 
account_number = "20260001" 
balance = 10000.00
 
withdrawal_limit = 10000.00
minimum_balance = 500.00
service_fee = 18.00
 
print("=== PYTHON CLI ATM by POSTANES ===")
print(f"Welcome, {account_name}!")
 
print()
print("===== ATM MENU =====") 
print("1. Check Balance") 
print("2. Deposit") 
print("3. Withdraw") 
print("4. Account Information") 
print("5. Exit")
 
choice = input("Choose an option: ")
 
# TODO 1: Check Balance 
if choice == "1": 
  print(f"Current Balance: ₱{balance:.2f}")
 
# TODO 2: Deposit 
elif choice == "2": 
  deposit = float(input("Enter deposit amount: ")) 
 
  # TODO 3: Validate the deposit 
  if deposit > 0: 
    # Add the deposit to the balance 
    balance += deposit
    print("Deposit successful.")
    print(f"New Balance: ₱{balance:.2f}") 
 
  else: 
    print("Invalid deposit amount.")
 
# TODO 4: Withdrawal 
elif choice == "3": 
  withdraw = float(input("Enter withdrawal amount: "))
 
  # TODO 5: Reject zero or negative withdrawal
  if withdraw <= 0: 
    print("Invalid withdrawal amount.")
 
  # TODO 6: Check the withdrawal limit 
  elif withdraw > withdrawal_limit: 
    print("Withdrawal exceeds the ATM limit.")
        
  # TODO 7: Check available balance including service fee 
  elif withdraw + service_fee > balance: 
    print("Insufficient balance.") 
 
  # TODO 8: Check minimum balance requirement 
  elif minimum_balance > balance - (withdraw + service_fee): 
    print("Withdrawal denied.") 
    print(f"Minimum balance required: ₱{minimum_balance:.2f}")
 
  else: 
    # TODO 9: Calculate the total deduction 
    total_deduction = withdraw + service_fee
 
    # TODO 10: Update the balance 
    balance -= total_deduction
 
    print("Withdrawal successful.") 
    print(f"Withdrawal Amount: ₱{withdraw:.2f}") 
    print(f"Service Fee: ₱{service_fee:.2f}") 
    print(f"Total Deduction: ₱{total_deduction:.2f}") 
    print(f"Remaining Balance: ₱{balance:.2f}")
 
# TODO 11: Account Information 
elif choice == "4": 
  print("===== ACCOUNT INFORMATION =====") 
  print(f"Name: {account_name}") 
  print(f"Account Number: {account_number}") 
  print(f"Balance: ₱{balance:.2f}")
 
# TODO 12: Exit 
elif choice == "5": 
  print("Thank you for using Python CLI ATM.")
 
# TODO 13: Handle invalid menu options 
else: 
  print("Invalid option.")

# """ 
######### Learning Signature ######### 
# Programmed by: Mary Julia Gabrielle E. Postanes
# Date Submitted: August 17, 2026
 
# Program Description: This program displays the ATM Menu Decision System.
# Reflection: I learned how to combine variables, input, arithmetic operators, comparison, logical, etc., into one ATM menu system.
#               
 
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [/] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
# """
# Explaination: I used AI as Support Tool for syntax errors.
