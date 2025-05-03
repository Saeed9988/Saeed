def convert_currency(amount, from_currency, to_currency):
    rates = {
        "CHF": {"EUR": 0.93, "USD": 1.10},
        "EUR": {"CHF": 1.08, "USD": 1.18},
        "USD": {"CHF": 0.91, "EUR": 0.85}
    }

    if from_currency == to_currency:
        return amount

    try:
        rate = rates[from_currency][to_currency]
        return round(amount * rate, 2)
    except KeyError:
        return None

print("📌 Einfacher Währungsrechner")
print("Unterstützte Währungen: CHF, EUR, USD")

amount = float(input("Betrag eingeben: "))
from_currency = input("Von Währung (CHF/EUR/USD): ").upper()
to_currency = input("In Währung (CHF/EUR/USD): ").upper()

result = convert_currency(amount, from_currency, to_currency)

if result is not None:
    print(f"✅ {amount} {from_currency} = {result} {to_currency}")
else:
    print("❌ Ungültige Währungskombination.")
    