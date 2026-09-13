from abc import ABC, abstractmethod

import postanes_bank_utils


class BankAccount(ABC):

    def __init__(
        self,
        account_number,
        name,
        pin,
        starting_balance
    ):
        self.account_number = account_number
        self.account_name = name

        # Encapsulation
        self._pin = pin
        self._balance = starting_balance

    # Encapsulation
    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount

        return True

    # The stored pin is already a hash (register_account),
    # so we hash the entered pin the same way before comparing them.
    # Also, the plaintext pins are never kept on disk.
    def verify_pin(self, pin):

        return self._pin == (
            postanes_bank_utils.hash_pin(pin)
        )

    # Used by storage when the account
    # needs to be saved.
    def get_pin(self):

        return self._pin

    # Abstraction
    @abstractmethod
    def get_account_type(self):
        pass


# Inheritance
class SavingsAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Savings Account"


# Inheritance
class StudentAccount(BankAccount):

    # Student accounts cap how much can
    # leave the account in a single
    # withdrawal.
    MAX_WITHDRAWAL = 5000.0

    # Polymorphism: overrides the base
    # withdraw() rule with a stricter one,
    # then delays it for the rest.
    def withdraw(self, amount):

        if amount > self.MAX_WITHDRAWAL:
            return False

        return super().withdraw(amount)

    # Polymorphism
    def get_account_type(self):

        return "Student Account"