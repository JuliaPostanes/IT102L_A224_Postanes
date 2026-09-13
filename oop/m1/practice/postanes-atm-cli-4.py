balance = 5000.00 
minimum_balance = 500.00 
 
withdraw = float(input("Enter withdrawal amount: ")) 
 
# TODO 1: Calculate the balance after the withdrawal 
remaining_balance = balance - withdraw
 
# TODO 2: Check if the withdrawal is valid 
# The withdrawal must be greater than 0 
# AND the remaining balance must be at least ₱500 
 
if withdraw > 0 and remaining_balance >= minimum_balance: 
  balance -= withdraw 
 
  print("Withdrawal successful.") 
  print(f"Remaining Balance: ₱{balance:.2f}") 
 
else: 
  print("Withdrawal denied.") 
  print(f"Minimum balance required: ₱{minimum_balance:.2f}")

# """ 
######### Learning Signature ######### 
# Programmed by: Mary Julia Gabrielle E. Postanes
# Date Submitted: August 17, 2026
 
# Program Description: This program displays the minimum balance protection.
# Reflection: I learned how to use arithmetic and comparison operators.
#              
 
# AI Usage
# [/] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
# """
