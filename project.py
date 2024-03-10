import inflect
import requests
import re
import xml.etree.ElementTree as ET
import sys

p = inflect.engine()

# Accessing to Central Bank of Azerbaijan's rates page to retrieve exchange rates
try:
    cbar = requests.get("https://cbar.az/currency/rates").text
except requests.exceptions.RequestException as e:
    sys.exit(f"Error occured: {e}")


# The link always is in https://cbar.az/currencies/dd.mm.yyyy.xml format
current = re.search(r"(https://cbar\.az/currencies/\d{2}\.\d{2}\.\d{4}\.xml)", cbar).group(0)
if current:
    try:
        rates = requests.get(current).text
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error occured while fetching the data: {e}")

# Setting the root of xml tree and adding currencies into a list
root = ET.fromstring(rates)

# Appending currencies in dict structure to a list
rates = []
for type in root:
    for currency in type:
        unit = currency[0].text
        code = currency.attrib['Code']
        currency_value = float(currency[2].text)
        if unit == "100":
            currency_value = currency_value / 100
            unit = "1"
        rates.append({"unit": unit, "code": code, "currency_value": currency_value})


# Main function
def main():
    while True:
        mode = ask_which_way()    
        if mode != "exit":
            result = convert(mode)
            print(result)
        else:
            exit_app()


# Deciding whether the conversation will be to or from AZN
def ask_which_way():
    while True:
        mode = input("\nType 'to' or 'from' to convert AZN, or 'exit' to leave the app:\n").strip().lower()
        if mode in ["to", "from", "exit"]:
            return mode


def convert(mode):
    # Amount inputted by the user
    while True:
        amount = input(f"\nAmount to convert {mode} AZN, or 'exit' to leave the app:\n").strip().lower()
        if amount != "exit":
            try:
                amount = float(amount)
                break
            except ValueError:
                pass
        else:
            exit_app()

    # Currency code inputted by the user
    while True:
        code = input(f"\nCurrency code to convert {mode} AZN, or 'exit' to leave the app:\n").upper()
        # Checking if it matches
        for rate in rates:
            if rate["code"] == code:
                currency_value = rate["currency_value"]
                oz = ounces_prepend(code, mode, amount, amount / currency_value) 

                # Returning results
                if mode == "to":
                    return f"\n{amount:.2f} {oz}{code} is {amount * currency_value:.2f} AZN"
                elif mode == "from":
                    return f"\n{amount:.2f} AZN is {amount / currency_value:.2f} {oz}{code}"
        
        # If the user's input doesn't match any supported currency
        if not any(code == rate["code"] for rate in rates) and code != "EXIT":
            # Showing the user the list of the supported currencies, and seperating the last element by "and" rather than a comma.
            supported = ""
            for rate in rates:
                supported = (", ".join([supported, rate["code"]])).lstrip(", ") if rate != rates[-1] else (" and ".join([supported, rate["code"]]))
            print(f"\nEntered currency is either not supported or invalid.\nOnly {supported} are supported\n")
        
        # Exit option
        elif code == "EXIT":
            exit_app()
        

# Only precious metals' codes start with the letter X, and they are measured in troy ounces
def ounces_prepend(code, mode, input, result):
    if code[0] == "X":
        if mode == "to":
            return f'troy {p.plural("ounce", input)} of '
        elif mode == "from":
            return f'troy {p.plural("ounce", result)} of '
    else:
        return ""


def exit_app():
    sys.exit("\nExited\n")


if __name__ == "__main__":
    main()