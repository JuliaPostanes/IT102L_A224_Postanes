def view_history():
    
    try: 
        with open("transactions.txt", "r", encoding="utf-8") as file:
            
            lines = file.readlines()
            
        return lines
    
    except FileNotFoundError:
        
        return []

## """
######### Learning Signature #########
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 10, 2026

## Program Description: This program creates a new module for viewing the ATM transaction history.
## Reflection: I learned how to create a function that reads from a file and returns its contents.

## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
## """