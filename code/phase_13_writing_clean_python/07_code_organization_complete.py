"""
Phase 13 - Writing Clean Python
07 Code Organization
One function = one job. Keep calculating, formatting and printing apart.
"""

from helpers import separator

RAW_ORDERS = [
    "apple,3,1.50",
    "banana,x,0.50",       # bad quantity
    "mango,2,4.00",
    "broken line",         # wrong format
]

TAX_RATE = 0.18


# ---------- BAD ----------
def bad_do_everything(lines):
    t = 0
    for l in lines:
        p = l.split(",")
        if len(p) == 3 and p[1].isdigit():
            t = t + int(p[1]) * float(p[2])
        else:
            print("skipping", l)
    print("total", t + t * 0.18)


# ---------- CLEAN ----------
def parse_order(line):
    """Turn 'name,quantity,price' into a dict, or None if it is invalid."""
    parts = line.split(",")
    if len(parts) != 3 or not parts[1].isdigit():
        return None
    return {
        "name": parts[0],
        "quantity": int(parts[1]),
        "price": float(parts[2]),
    }


def load_orders(lines):
    """Return (valid_orders, invalid_lines)."""
    valid, invalid = [], []
    for line in lines:
        order = parse_order(line)
        if order is None:
            invalid.append(line)
        else:
            valid.append(order)
    return valid, invalid


def calculate_total(orders, tax_rate=TAX_RATE):
    subtotal = sum(order["quantity"] * order["price"] for order in orders)
    return subtotal + subtotal * tax_rate


def format_report(orders, invalid, total):
    lines = [
        f"{o['name']}: {o['quantity']} x {o['price']:.2f}" for o in orders
    ]
    lines.append(f"Skipped lines: {len(invalid)}")
    lines.append(f"Total with tax: {total:.2f}")
    return "\n".join(lines)


def main():
    separator("BAD: one function does everything")
    bad_do_everything(RAW_ORDERS)

    separator("CLEAN: small functions, one job each")
    orders, invalid = load_orders(RAW_ORDERS)         # load
    total = calculate_total(orders)                   # process
    print(format_report(orders, invalid, total))      # output

    separator("Each small function is easy to reuse and check")
    print(parse_order("pen,10,2.5"))
    print(parse_order("pen,ten,2.5"))
    print(calculate_total([], tax_rate=0.05))


if __name__ == "__main__":
    main()