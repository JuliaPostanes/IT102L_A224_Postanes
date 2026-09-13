balance = 10000.00 
maximum_deposit = 50000.00 
 
deposit = float(input("Enter deposit amount: ")) 
 
# TODO 1: Check if the deposit is zero or negative 
if deposit <= 0: 
  print("Invalid deposit amount.") 
 
# TODO 2: Check if the deposit is greater than the maximum deposit 
elif deposit > maximum_deposit: 
  print("Deposit exceeds the maximum deposit limit.") 
 
# TODO 3: Process a valid deposit 
else: 
  # Add the deposit to the balance 
  balance += deposit 
 
  print("Deposit successful.") 
 
  # TODO 4: Display the updated balance 
  print(f"New Balance: ₱{balance:.2f}")


# """ 
######### Learning Signature ######### 
# Programmed by: Mary Julia Gabrielle E. Postanes
# Date Submitted: August 17, 2026
 
# Program Description: This program displays the deposit validation.
# Reflection: I learned how to do more if-else statement, as well as the
#               "elif" (which is basically else-if) in the project.
 
# AI Usage
# [/] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
# """

