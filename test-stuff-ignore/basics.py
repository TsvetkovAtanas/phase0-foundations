# 1. Variables: names, objects, and references
# price, quantity, and product are names bound to objects.

price = 49.99
quantity = 3
product = "Notebook"

total = price * quantity

print(total)  # 149.97

#==========================================================================================



# 1.1 Assignment and rebinding
# All three assignments are valid. The name value is rebound to a different object each time. This is called dynamic typing.

value = 10
value = "ten"
value = True

#==========================================================================================



# 1.2 Multiple assignment and unpacking
# Python evaluates the right-hand side and unpacks the values into the targets.

x, y = 10, 20
x, y = y, x

print(x, y)  # 20 10

# Unpacking a sequence:
first, *middle, last = [10, 20, 30, 40, 50]

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50

#==========================================================================================



# 1.3 Mutability: a critical distinction
#A list is mutable: its contents can change without creating a new list.
# A string is immutable: concatenation produces a new string, and the name is rebound to it.

# Mutable object
numbers = [1, 2, 3]
numbers.append(4)

# Immutable object
name = "Alex"
name = name + " Smith"


a = [1, 2]
b = a

b.append(3)

print(a)  # [1, 2, 3]
# a and b refer to the same list. Modifying the list through b is visible through a


# With a shallow copy:
a = [1, 2]
b = a.copy()

b.append(3)

print(a)  # [1, 2]
print(b)  # [1, 2, 3]
    
#==========================================================================================



# 1.4 Naming conventions
# Use descriptive snake_case names:

customer_age = 32
monthly_revenue = 12500.00
is_subscription_active = True

#==========================================================================================
#==========================================================================================




#2. Data types: understanding the values Python processes
# A data type determines which values an object can represent and which operations are meaningful for it.


#2.1 The core built-in types

int
float
str
bool
None

# Collection types

list    # [10, 20, 30]	    Ordered, mutable
tuple   # (10, 20, 30)	    Ordered, immutable
dict    # {"name": "Alex"}	Key-value mapping
set     # {10, 20, 30}	    Unique elements, no positional indexing


#2.2 Inspecting types
# Use type() to inspect an object's type and isinstance() to test whether an object belongs to a type or its subclasses.

price = 19.99
quantity = 4

print(type(price))                 # <class 'float'>
print(isinstance(quantity, int))   # True
print(isinstance(True, int))       # True (in Python, bool is a subclass of int.)


#2.3 Type conversion
# Conversion changes how a value is represented or interpreted.

age_text = "35"
age = int(age_text)

price_text = "19.95"
price = float(price_text)

print(age + 5)       # 40
print(price * 2)     # 39.9

int("42")       # 42
float("3.14")   # 3.14
str(42)         # "42"
bool(1)         # True
bool(0)         # False
list("cat")     # ['c', 'a', 't']
int("hello")    # ValueError

# Also, bool() tests truthiness rather than interpreting words semantically:
# A nonempty string is truthy, even when it contains the text "False".
bool("False")  # True
bool("")       # False


#2.4 Floating-point precision

print(0.1 + 0.2)
# 0.30000000000000004

# For approximate numerical comparisons, use math.isclose():
import math

print(math.isclose(0.1 + 0.2, 0.3))
# True


# For financial calculations where decimal arithmetic matters, use decimal.Decimal:
from decimal import Decimal

price = Decimal("19.99")
quantity = 3

total = price * quantity
print(total)  # 59.97
# Construct decimals from strings to avoid importing the binary approximation of a float. For money, also define a rounding policy appropriate to the currency and transaction.


#==========================================================================================
#==========================================================================================



#3. Operators: how Python evaluates expressions
# Operators perform calculations, comparisons, logical tests, and other operations on objects.

# + - * / are obvious
# special onces:
# //	Floor division	10 // 3	= 3
# %	    Modulo	        10 % 3	= 1
# **	Exponentiation	2 ** 4	= 16

# Floor division and modulo are particularly useful for splitting quantities and checking remainders.
total_items = 17
items_per_box = 5

full_boxes = total_items // items_per_box
remaining_items = total_items % items_per_box

print(full_boxes)        # 3
print(remaining_items)   # 2

# Python's floor division rounds toward negative infinity, not toward zero:
print(-7 // 2)  # -4
print(-7 % 2)   # 1


#3.2 Assignment operators

balance = 100
balance += 25
balance -= 10
balance *= 2

print(balance)  # 230

# with mutable objects:
numbers = [1, 2]
numbers += [3]

print(numbers)  # [1, 2, 3]

# For a list, += typically extends the existing list, whereas numbers = numbers + [3] creates a new list and rebinds the name.


#3.3 Comparison operators

age = 25

print(age > 18)      # True
print(age == 25)     # True
print(age != 30)     # True
print(18 <= age < 65)  # True

# Python supports chained comparisons.
(18 <= age < 65) == (18 <= age and age < 65) # the same


# For identity, Python provides is and is not:
result = None

print(result is None)  # True


#3.4 Logical operators and short-circuit evaluation
# Python uses and, or, and not.

age = 30
has_id = True

can_enter = age >= 18 and has_id
print(can_enter)  # True

# 'and' and 'or' do not necessarily return True or False. They return one of their operands.
username = ""
display_name = username or "Guest"

print(display_name)  # Guest


# 'or' returns the first truthy operand, or the last operand if none is truthy. 'and' returns the first falsy operand, or the last operand if all are truthy.
# They also short-circuit: Python may skip evaluating the second operand.
denominator = 0

if denominator != 0 and 100 / denominator > 5:
    print("Above threshold") # The division is never evaluated because the first condition is false. This pattern can prevent errors when used correctly.


#3.5 Membership operators
# Use in and not in to test membership.

allowed_roles = ["admin", "editor", "viewer"]

print("admin" in allowed_roles)   # True
print("guest" not in allowed_roles)  # True

# For dictionaries, membership checks keys, not values:
user = {"name": "Alex", "role": "admin"}

print("name" in user)    # True
print("Alex" in user)    # False
print("Alex" in user.values())  # True


#3.6 Operator precedence
# Python evaluates some operations before others.

result = 2 + 3 * 4
print(result)  # 14

result = (2 + 3) * 4
print(result)  # 20



#==========================================================================================
#==========================================================================================


#4. Input and output (I/O): interacting with users and files

#4.1 Output with print()

name = "Nacho"
revenue = 12500.75

print("Name:", name)
print("Revenue:", revenue)

# You can control separators and line endings:

print("2026", "10", "29", sep="-")
# 2026-10-29

print("Loading", end="...")
print("Complete")
# Loading...Complete

#4.2 String formatting with f-strings

product = "Laptop"
price = 1299.99
quantity = 2

print(f"Product: {product}")
print(f"Unit price: €{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: €{price * quantity:.2f}")


# Useful formatting specifications include:
value = 12345.6789

print(f"{value:.2f}")       # 12345.68
print(f"{value:,.2f}")      # 12,345.68
print(f"{value:>12.2f}")    # Right-aligned, width 12
print(f"{0.175:.1%}")       # 17.5%


#4.3 Reading input with input()
# The input() function reads a line of text from standard input and returns a string.

name = input("Enter your name: ")
print(f"Welcome, {name}.") #The critical rule is that input() returns a str, not a number, even when the user enters digits.


# Convert the inputs before performing arithmetic:
a = int(input("First number: "))
b = int(input("Second number: "))

print(a + b)


#4.4 Handling invalid input
# Direct conversion can fail if the user enters something unexpected. 
# Use try and except to handle conversion errors.
try:
    age = int(input("Enter your age: "))
    print(f"Next year, you will be {age + 1}.")
except ValueError:
    print("Please enter a whole number.")


# A stronger version also validates the range:
try:
    age = int(input("Enter your age: "))

    if not 0 <= age <= 120:
        print("Age must be between 0 and 120.")
    else:
        print(f"Your age is {age}.")

except ValueError:
    print("Invalid input: enter a whole number.")


#Type validation: Can the input be converted to an integer?
#Domain validation: Is the resulting integer acceptable for the application?


#4.5 Reading and writing files
#Standard input/output also includes files. Python's open() function lets you read or write persistent data.

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Monthly revenue: 12500\n")
    file.write("Expenses: 7800\n")


with open("report.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)

# "r"	Read an existing file
# "w"	Write, replacing existing contents
# "a"	Append to the file
# "x"	Create a new file; fail if it exists



#5. Putting the concepts together
# Example: profit calculator


from decimal import Decimal, InvalidOperation

try:
    revenue = Decimal(input("Enter revenue (€): "))
    expenses = Decimal(input("Enter expenses (€): "))

    if not revenue.is_finite() or not expenses.is_finite():
        raise ValueError("Values must be finite numbers.")

    if revenue < 0 or expenses < 0:
        raise ValueError("Values cannot be negative.")

    profit = revenue - expenses

    if revenue > 0:
        margin = profit / revenue * 100
        print(f"Profit: €{profit:,.2f}")
        print(f"Profit margin: {margin:.2f}%")
    else:
        print(f"Profit: €{profit:,.2f}")
        print("Profit margin: undefined when revenue is zero.")

except (ValueError, InvalidOperation):
    print("Invalid input. Enter valid, non-negative numbers.")
