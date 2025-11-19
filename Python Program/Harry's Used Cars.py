#Desc: Honest Harry owns a used car lot and would like a program to keep track of his sales
#Author: Logan Marsh
#Date: November 19th 2025
# ---------------------------------------------------------------

from datetime import date, timedelta
from FormatValues import format_phone, format_money, format_receipt_id

# --------------------------
# CONSTANTS
# --------------------------
MAX_SELL_PRICE = 50000.00
HST_RATE = 0.15
LUXURY_RATE = 0.016
TRANSFER_RATE = 0.01
LICENSE_LOW = 75.00
LICENSE_HIGH = 165.00
FINANCE_RATE = 39.99


# --------------------------
# FUNCTIONS
# --------------------------

def get_valid_plate() -> str:
    """
    Must be 6 characters. Convert to upper.
    BONUS allowed: format XXX999 (not forced)
    """
    while True:
        plate = input("Enter plate number (6 chars): ").upper().strip()
        if len(plate) == 6:
            return plate
        print("ERROR – Plate must be exactly 6 characters.")


def get_valid_phone() -> str:
    """
    Must be 10 digits.
    """
    while True:
        phone = input("Enter phone number (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("ERROR – Phone must be exactly 10 digits.")


def calculate_fees(sell_price: float, trade: float) -> tuple:
    """
    Calculates:
    - price after trade
    - license fee
    - transfer + luxury fee
    - subtotal
    - HST
    - total price
    """
    price_after_trade = sell_price - trade

    # License fee
    if sell_price <= 15000:
        license_fee = LICENSE_LOW
    else:
        license_fee = LICENSE_HIGH

    # Transfer fee + luxury tax if needed
    transfer_fee = sell_price * TRANSFER_RATE
    if sell_price > 20000:
        transfer_fee += sell_price * LUXURY_RATE

    subtotal = price_after_trade + license_fee + transfer_fee
    hst = subtotal * HST_RATE
    total_price = subtotal + hst

    return price_after_trade, license_fee, transfer_fee, subtotal, hst, total_price


# ---------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------

while True:

    first = input("Enter Customer First Name (or END to stop): ").strip()
    if first.upper() == "END":
        break

    last = input("Enter Customer Last Name: ").strip()

    # Validation only where required
    first = first.title()
    last = last.title()

    phone = get_valid_phone()
    plate = get_valid_plate()

    make = input("Enter Car Make: ").title()
    model = input("Enter Car Model: ").title()
    year = input("Enter Car Year: ").strip()

    # Selling price
    while True:
        price = float(input("Enter selling price (max 50000): "))
        if price <= MAX_SELL_PRICE:
            break
        print("ERROR – Price too high.")

    # Trade value
    while True:
        trade = float(input("Enter trade-in amount: "))
        if trade <= price:
            break
        print("ERROR – Trade cannot exceed selling price.")

    salesperson = input("Enter salesperson name: ")

    # -----------------------------------------------------------
    # CALCULATE FEES
    # -----------------------------------------------------------
    price_after_trade, license_fee, transfer_fee, subtotal, hst, total_price = calculate_fees(price, trade)

    # -----------------------------------------------------------
    # BUILD RECEIPT
    # -----------------------------------------------------------

    # Receipt ID
    receipt_id = format_receipt_id(first[0], last[0], plate, phone)

    # Customer display name
    customer_name = f"{first[0]}. {last}"

    car_details = f"{year} {make} {model}"

    invoice_date = date.today().strftime("%a %b %d, %Y")

    print("\n" + "-"*80)
    print(f"Honest Harry Car Sales{'':>28}Invoice Date: {invoice_date}")
    print(f"Used Car Sale and Receipt{'':>23}Receipt No: {receipt_id}")
    print(f"Sale price:{format_money(price):>55}")
    print(f"Sold to:{customer_name:>12}")
    print(f"  {format_phone(phone)}")
    print(f"Trade Allowance:{format_money(trade):>42}")
    print("-"*35)
    print(f"Price after Trade:{format_money(price_after_trade):>38}")
    print(f"License Fee:{format_money(license_fee):>45}")
    print(f"Transfer Fee:{format_money(transfer_fee):>44}")
    print("-"*35)
    print(f"Car Details: {car_details}")
    print(f"Subtotal:{format_money(subtotal):>52}")
    print(f"HST:{format_money(hst):>60}")
    print("-"*35)
    print(f"Total sales price:{format_money(total_price):>38}")
    print("-"*80)

    # -----------------------------------------------------------
    # PAYMENT SCHEDULE
    # -----------------------------------------------------------
    print(" Financing        Total      Monthly")
    print(" # Years   # Payments  Fee     Price      Payment")
    print(" ------------------------------------------------------------")

    for years in range(1, 5):
        months = years * 12
        finance_fee = FINANCE_RATE * years
        finance_total = total_price + finance_fee
        monthly_payment = finance_total / months

        print(f"  {years:<6}{months:<12}{format_money(finance_fee):<10}"
              f"{format_money(finance_total):<12}{format_money(monthly_payment)}")

    # -----------------------------------------------------------
    # FIRST PAYMENT DATE
    # -----------------------------------------------------------
    today = date.today()
    next_month = today.replace(day=1) + timedelta(days=32)
    next_month = next_month.replace(day=1)

    # If current day >= 25, add an extra month
    if today.day >= 25:
        next_month = next_month.replace(day=1) + timedelta(days=32)
        next_month = next_month.replace(day=1)

    pay_date = next_month.strftime("%d-%b-%y").upper()

    print(" ------------------------------------------------------------")
    print(f" First payment date: {pay_date}")
    print("-"*80)
    print(" Best used cars at the best prices!")
    print("-"*80 + "\n")
