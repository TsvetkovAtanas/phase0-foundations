
from decimal import Decimal, InvalidOperation

try:
    # 1. Collect input
    product_name = input("Enter product name: ")
    selling_price = Decimal(input("Enter selling price per unit (€): "))
    unit_cost = Decimal(input("Enter cost per unit (€): "))
    quantity = int(input("Enter quantity sold: "))

    # 2. Validate input
    # TODO: Reject negative prices and costs.
    if selling_price < 0 or unit_cost < 0:
        raise ValueError("The selling price and cost per unit can not be a negative number!")
    # TODO: Reject quantity <= 0.
    if quantity <= 0:
        raise ValueError("The quantity can no be zero or negative number!")
    # TODO: Check that monetary values are finite.
    if not Decimal.isfinite(selling_price) or not Decimal.isfinite(unit_cost):
        raise ValueError("The selling price and cost per unit are not finite!")

    # 3. Calculate results
    # TODO: Calculate total revenue.
    revenue = selling_price * quantity
    # TODO: Calculate total cost.
    total_cost = unit_cost * quantity
    # TODO: Calculate total profit.
    total_profit = revenue - total_cost
    # TODO: Calculate profit margin safely.
    if revenue != 0:
        profit_margin = total_profit / revenue
        print(f"Profit margin: {profit_margin:.1%}")
    else:
        print("Profit margin: undefined (revenue is zero).")
    
    # 4. Print the report
    print("--- SALES REPORT ---")
    # TODO: Display the product name.
    print(f"Product: {product_name}")
    # TODO: Format monetary values to 2 decimal places.
    print(f"Total revenue: {revenue:.2f}")
    print(f"Total cost: {total_cost:.2f}")
    print(f"Total profit: {total_profit:.2f}")
    # TODO: Display profit margin as a percentage.
    print(f"Profit margin: {profit_margin:.1%}")

except (ValueError, InvalidOperation):
    print("Invalid input. Please enter valid numerical values.")
