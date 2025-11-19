# ---------------------------------------------------------------
# FormatValues.py - Helper library for Honest Harry Car Sales
# Author: Logan Marsh
# Date: November 19th 2025
# ---------------------------------------------------------------

def format_phone(number: str) -> str:
    """
    Formats a 10-digit phone number as: (XXX) XXX-XXXX
    """
    return f"({number[0:3]}) {number[3:6]}-{number[6:]}"


def format_money(amount: float) -> str:
    """
    Formats a float to standard currency: $99,999.99
    """
    return f"${amount:,.2f}"


def format_receipt_id(first_initial: str, last_initial: str, plate: str, phone: str) -> str:
    """
    NEW FUNCTION:
    Creates receipt ID format: XX-XXX-XXXX
    - First two characters: customer initials
    - Next three: last 3 digits of license plate
    - Last four: last 4 digits of phone number
    """
    return f"{first_initial}{last_initial}-{plate[-3:]}-{phone[-4:]}"
