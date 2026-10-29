import decimal


# TODO: Validate all inputs.
try:
    # TODO: Enter and store values for -> Name, Wage, Hours worked, Tax rate %.
    employee_name = input("Enter the employee's name: ")
    hourly_wage = decimal.Decimal(input("Enter the hourly wage: "))
    hours_worked = int(input("Enter the hours worked: "))
    tax_rate = int(input("Enter the tax rate: "))

    if employee_name == "":
        raise ValueError("Enter an employee name")
    if not hourly_wage > 0:
        raise ValueError("Hourly wage should be greater than 0.")
    if not 0 < hours_worked <= 168:
        raise ValueError("Hours worked should be betwwen 0 - 168.")
    if not 0 <= tax_rate <= 100:
        raise ValueError("Tax rate should be betwwen 0% - 100%.")

    # TODO: Calcualte -> Gross pay, Tax deduction, Net pay.
    gross_pay = hourly_wage * hours_worked
    tax_deduction = gross_pay * tax_rate / 100
    net_pay = gross_pay - tax_deduction

except ValueError:
    print("Invalind Input!")



# TODO: Open a file and write formatted payroll report.

with open("report.txt", 'w', encoding="utf-8") as file:
    file.write(f"Employee: {employee_name}\n")
    file.write(f"Gross pay: {gross_pay:.2f}\n")
    file.write(f"Tax deduction: {tax_deduction}\n")
    file.write(f"Net pay: {net_pay:.2f}\n")

with open("report.txt", 'r', encoding="utf-8") as file:
    content = file.read()

print(content)

