class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount > 0:
            self._balance += amount
            return True

        return False

    def withdraw(self, amount):

        if amount > 0 and amount <= self._balance:

            self._balance -= amount

            return True

        return False
## """
######### Learning Signature #########
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 9, 2026

## Program Description: This program updates my account class from practice 8 with OOP this time.
## Reflection: I learned how to create a class and its methods.

## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
## """