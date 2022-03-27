from symtable import Symbol
from urllib import response
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "a22cf685c764fc99b005"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url= BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())

    data.sort()
    
    return data
   
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id}---{name}---{symbol}")

def exchange_rate(currency_1, currency_2):
    endpoint = f"api/v7/convert?q={currency_1}_{currency_2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json()
    if len(data) == 0:
        print("Invalid Currencies.")
        return
    rate = list(data.values())[0]
    print(f"{currency_1} -> {currency_2} = {rate}")
    return  rate

def convert(currency_1, currency_2, amount):
    rate = exchange_rate(currency_1, currency_2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = amount * rate
    print(f"{amount} {currency_1} is equal to {converted_amount} {currency_2}.")
    return converted_amount

def main():
    currencies = get_currencies()

    print("Welcome to the Currency Converter!")
    print("Lists - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies.")


    while True:
        command = input("Enter a command(q to quit)(help to list commands): ").lower()

        if command == 'q':
            break
        elif command == "help":
            print("list - prints list of currencies available. \n convert - converts one currency to another. \n rate - shows current exchange rate between currency pair.")
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency_1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter the amount of {currency_1} you would like to convert: ")
            currency_2 = input("Enter the currency you are converting to: ").upper()
            convert(currency_1, currency_2, amount)
        elif command == 'rate':
            currency_1 = input("Enter a base currency: ").upper()
            currency_2 = input("Enter the currency you are converting to: ").upper()
            exchange_rate(currency_1, currency_2)
        else:
            print("Unrecognized Command.")






main()

#data = get_currencies()

#print_currencies(data)

exchange_rate("USD", "CAD")

