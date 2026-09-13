from datetime import datetime


def withdraw_money(account, amount):

    if amount <= 0:
        return False

    success = account.withdraw(amount)

    if success:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open("transactions.txt", "a", encoding="utf-8") as file:

            file.write(
                f"Timestamp: {timestamp}\n"
            )

            file.write(
                f"Account: {account.account_name}\n"
            )

            file.write(
                "Transaction: Withdraw\n"
            )

            file.write(
                f"Amount: ₱{float(amount):.2f}\n\n"
            )

        return True

    return False

## """
######### Learning Signature #########
## Programmed by: Mary Julia Gabrielle E. Postanes
## Date Submitted: September 9, 2026

## Program Description: This program creates a new module for withdrawing money.
## Reflection: I learned how to create a function that receives an object as a parameter
#                         and calls its method. I also learned how to write to a file to log transactions.

## AI Usage
## [/] No AI Assistance – Completed independently without AI.
## [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
## [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
## """