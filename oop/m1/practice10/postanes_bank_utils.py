import hashlib


def is_valid_amount(amount):

    return amount > 0


def format_currency(amount):

    return f"₱{amount:,.2f}"


def hash_pin(pin):

    return hashlib.sha256(
        pin.encode()
    ).hexdigest()