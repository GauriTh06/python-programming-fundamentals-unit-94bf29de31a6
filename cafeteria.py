"""Cafeteria menu, specials, and discounted prices."""

import math
from numbers import Real


MENU = [
    ("Tomato Soup", 3.50),
    ("Grilled Cheese Sandwich", 5.00),
    ("Veggie Wrap", 5.00),
    ("Chicken Curry", 6.75),
    ("Fish and Chips", 7.50),
    ("Garden Salad", 4.00),
    ("Apple Pie", 2.25),
]


SPECIALS = {
    "monday": ("Tomato Soup", 0.20),
    "tuesday": ("Grilled Cheese Sandwich", 0.15),
    "wednesday": ("Veggie Wrap", 0.10),
    "thursday": ("Chicken Curry", 0.25),
    "friday": ("Fish and Chips", 0.30),
}


def menu_lines():
    """Return each menu item formatted with its price."""
    lines = []
    for item, price in MENU:
        lines.append(f"{item}: ${price:.2f}")
    return lines


def print_menu():
    """Print the cafeteria menu."""
    print("Cafeteria Menu:")
    for line in menu_lines():
        print(line)


def price_of(item_name):
    """Return an item's price, or 0.0 when the item is not on the menu."""
    if not isinstance(item_name, str):
        return 0.0
    item_name = item_name.strip()
    for item, price in MENU:
        if item.casefold() == item_name.casefold():
            return price
    return 0.0


def find_special(day):
    """Return the special item and discount for a weekday."""
    if not isinstance(day, str):
        return (None, 0.0)
    chosen = day.strip().casefold()
    return SPECIALS.get(chosen, (None, 0.0))


def discounted_price(price, discount):
    """Return a price after applying a fractional discount."""
    if isinstance(price, bool) or not isinstance(price, Real) or not math.isfinite(price):
        raise ValueError("price must be a finite number")
    if (
        isinstance(discount, bool)
        or not isinstance(discount, Real)
        or not math.isfinite(discount)
        or not 0 <= discount <= 1
    ):
        raise ValueError("discount must be a number between 0 and 1")
    return round(price * (1.0 - discount), 2)


def main():
    """Display the menu and the special selected by the user."""
    print_menu()
    try:
        day = input("Enter the day of the week : ")
    except EOFError:
        day = ""
    special_item, discount = find_special(day)

    if special_item is None:
        print("No special today.")
    else:
        full_price = price_of(special_item)
        sale_price = discounted_price(full_price, discount)
        print(f"Today's special: {special_item}")
        print(f"Was ${full_price:.2f}, now ${sale_price:.2f}")
    print("Discount value:", discount)
    print("Discount type:", type(discount))


if __name__ == "__main__":
    main()
        