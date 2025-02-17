
tax_rates = {
    "income_tax_brackets": [
        {"upper_limit": 600000, "rate": 0, "fixed": 0},
        {"upper_limit": 1200000, "rate": 2.5, "fixed": 0},
        {"upper_limit": 2400000, "rate": 12.5, "fixed": 15000},
        {"upper_limit": 3600000, "rate": 22.5, "fixed": 165000},
        {"upper_limit": 6000000, "rate": 27.5, "fixed": 435000},
        {"upper_limit": float('inf'), "rate": 35, "fixed": 1095000}
    ],
    "gst_rate": 18,
    "vat_rate": 18,
    "zakat_threshold": 135179,
    "zakat_rate": 2.5,
    "ushr_natural_rate": 10,
    "ushr_artificial_rate": 5
}


def calculate_income_tax(monthly_salary):
    annual_salary = monthly_salary * 12
    tax = 0
    for bracket in tax_rates["income_tax_brackets"]:
        if annual_salary <= bracket["upper_limit"]:
            tax = bracket["fixed"] + (annual_salary - (bracket["upper_limit"] - 600000)) * (bracket["rate"] / 100)
            break
    return round(tax / 12)

def calculate_property_tax(property_worth, tax_rate):
    return round(property_worth * tax_rate / 100)

def calculate_gst(price):
    gst_value = round(price * tax_rates["gst_rate"] / 100)
    return gst_value

def calculate_vat(cost):
    vat_value = round(cost * tax_rates["vat_rate"] / 100)
    return vat_value

def calculate_commission(selling_price, commission_rate):
    return round(selling_price * commission_rate / 100)

def calculate_zakat(savings):
    if savings >= tax_rates["zakat_threshold"]:
        return round(savings * tax_rates["zakat_rate"] / 100)
    return 0

def calculate_ushr(cost_price, irrigation_type):
    if irrigation_type == 'n':
        return round(cost_price * tax_rates["ushr_natural_rate"] / 100)
    elif irrigation_type == 'a':
        return round(cost_price * tax_rates["ushr_artificial_rate"] / 100)
    return 0

def update_tax_rates():
    print("\n--- Current Tax Rates ---")
    print(tax_rates)
    print("\n--- UPDATE TAX RATES ---")
    print("1. GST Rate")
    print("2. VAT Rate")
    print("3. Zakat Rate and Threshold")
    print("4. Ushr Rates")
    print("5. Back to Main Menu")
    
    while True:
        choice = input("Select the tax rate to update (1-5): ")
        if choice == "1":
            tax_rates["gst_rate"] = float(input("Enter new GST rate (%): "))
            print("GST rate updated.")
        elif choice == "2":
            tax_rates["vat_rate"] = float(input("Enter new VAT rate (%): "))
            print("VAT rate updated.")
        elif choice == "3":
            tax_rates["zakat_rate"] = float(input("Enter new Zakat rate (%): "))
            tax_rates["zakat_threshold"] = float(input("Enter new Zakat threshold: "))
            print("Zakat rate and threshold updated.")
        elif choice == "4":
            tax_rates["ushr_natural_rate"] = float(input("Enter new Ushr rate for natural irrigation (%): "))
            tax_rates["ushr_artificial_rate"] = float(input("Enter new Ushr rate for artificial irrigation (%): "))
            print("Ushr rates updated.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
    
    print("\nUpdated Tax Rates Dictionary:")
    print(tax_rates)

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a valid number.")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a valid number.")

def main():
    while True:
        print("\n" + "=" * 40)
        print("            TAX CALCULATOR")
        print("=" * 40)
        print("1. Income Tax Calculator")
        print("2. Property Tax Calculator")
        print("3. General Sales Tax (GST) Calculator")
        print("4. Value Added Tax (VAT) Calculator")
        print("5. Commission Calculator")
        print("6. Zakat Calculator")
        print("7. Ushr Calculator")
        print("8. Update Tax Rates")
        print("9. Exit Program")
        print("=" * 40)

        choice = get_valid_int("Select an option (1-9): ")

        if choice == 1:
            monthly_salary = get_valid_float("Enter Monthly Salary: ")
            print("Monthly Income Tax:", calculate_income_tax(monthly_salary))
        elif choice == 2:
            property_worth = get_valid_float("Enter Property Worth: ")
            tax_rate = get_valid_float("Enter Tax Rate (%): ")
            print("Property Tax:", calculate_property_tax(property_worth, tax_rate))
        elif choice == 3:
            price = get_valid_float("Enter Price of Item: ")
            gst = calculate_gst(price)
            print("GST (Rate:", tax_rates['gst_rate'], "%):", gst)
        elif choice == 4:
            cost = get_valid_float("Enter Cost of Object: ")
            vat = calculate_vat(cost)
            print("VAT (Rate:", tax_rates['vat_rate'], "%):", vat)
        elif choice == 5:
            selling_price = get_valid_float("Enter Selling Price: ")
            commission_rate = get_valid_float("Enter Commission Rate (%): ")
            print("Commission:", calculate_commission(selling_price, commission_rate))
        elif choice == 6:
            savings = get_valid_float("Enter Savings: ")
            print("Zakat:", calculate_zakat(savings))
        elif choice == 7:
            cost_price = get_valid_float("Enter Land Cost Price: ")
            irrigation_type = input("Irrigation Type: Natural (N) or Artificial (A): ").lower()
            print("Ushr:", calculate_ushr(cost_price, irrigation_type))
        elif choice == 8:
            update_tax_rates()  # Print the dictionary after update
        elif choice == 9:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")
main()
