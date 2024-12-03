import json

# Dekorátor pro CSV formát
def to_csv(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        csv_data = "Month,Revenue,Expense\n"  # Hlavička CSV
        for row in result:
            csv_data += f"{row['Month']},{row['Revenue']},{row['Expense']}\n"
        return csv_data
    return wrapper

# Dekorátor pro JSON formát
def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, indent=4)  # Převede seznam na pěkně formátovaný JSON
    return wrapper


def generate_report():
    return [
        {"Month": "Leden", "Revenue": 10000, "Expense": 5000},
        {"Month": "Únor", "Revenue": 12000, "Expense": 6000},
        {"Month": "Březen", "Revenue": 11000, "Expense": 5500},
    ]


# CSV formát
@to_csv
def report_csv():
    return generate_report()

# JSON formát
@to_json
def report_json():
    return generate_report()

print("CSV Report:")
print(report_csv())

print("\nJSON Report:")
print(report_json())
