from postanes_bank_account import (
    SavingsAccount,
    StudentAccount
)


USERS_FILE = "users.txt"


def account_exists(account_number):

    return find_account(account_number) is not None


def _write_account_record(file, account):

    file.write(
        f"Account Number: "
        f"{account.account_number}\n"
    )

    file.write(
        f"Account Name: "
        f"{account.account_name}\n"
    )

    file.write(
        f"PIN: "
        f"{account.get_pin()}\n"
    )

    file.write(
        f"Account Type: "
        f"{account.get_account_type()}\n"
    )

    file.write(
        f"Balance: "
        f"{account.check_balance():.2f}\n\n"
    )


def save_account(account):

    with open(
        USERS_FILE,
        "a", encoding="utf-8"
    ) as file:

        _write_account_record(file, account)


def load_accounts():

    accounts = []

    try:

        with open(
            USERS_FILE,
            "r", encoding="utf-8"
        ) as file:

            lines = file.readlines()

    except FileNotFoundError:

        return accounts

    current = {}

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Account Number:"):

            current["account_number"] = (
                line
                .replace(
                    "Account Number:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Account Name:"):

            current["account_name"] = (
                line
                .replace(
                    "Account Name:",
                    ""
                )
                .strip()
            )

        elif line.startswith("PIN:"):

            current["pin"] = (
                line
                .replace(
                    "PIN:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Account Type:"):

            current["account_type"] = (
                line
                .replace(
                    "Account Type:",
                    ""
                )
                .strip()
            )

        elif line.startswith("Balance:"):

            balance_text = (
                line
                .replace(
                    "Balance:",
                    ""
                )
                .strip()
            )

            current["balance"] = float(
                balance_text
            )

            if (
                "account_number" in current
                and
                "account_name" in current
                and
                "pin" in current
                and
                "account_type" in current
            ):

                if (
                    current["account_type"]
                    == "Savings Account"
                ):

                    account = SavingsAccount(
                        current["account_number"],
                        current["account_name"],
                        current["pin"],
                        current["balance"]
                    )

                else:

                    account = StudentAccount(
                        current["account_number"],
                        current["account_name"],
                        current["pin"],
                        current["balance"]
                    )

                accounts.append(account)

            current = {}

    return accounts


def find_account(account_number):

    accounts = load_accounts()

    for account in accounts:

        if (
            account.account_number
            == account_number
        ):

            return account

    return None


def update_account(account):

    accounts = load_accounts()

    with open(
        USERS_FILE,
        "w", encoding="utf-8"
    ) as file:

        for saved_account in accounts:

            # Writes the freshly updated account
            # object in place of its copy
            # from disk, instead of reaching into
            # saved_account's private _balance since
            # that would break the encapsulation.
            
            # Also, BankAccount is meant to enforce.
            if (
                saved_account.account_number
                == account.account_number
            ):

                record = account

            else:

                record = saved_account

            _write_account_record(file, record)