"""
Currency Converter: NGN to Major World Currencies
Author: Python Developer
Date: February 2026

Description:
This program converts amounts from Nigerian Naira (NGN) to major world currencies.
It demonstrates proper use of functions, dictionaries, and user input handling.

Features:
- Accepts user input in Nigerian Naira
- Converts to USD, EUR, GBP, CAD, JPY
- Uses a dictionary to store exchange rates
- Provides clear, formatted output
- Includes input validation and error handling
"""

# Step 1: Define the exchange rates dictionary
# This dictionary stores how much of each currency equals 1 NGN
# Exchange rates are obtained from typical market rates as of February 2026
exchange_rates = {
    "USD": 0.000645,    # 1 NGN = 0.000645 USD
    "EUR": 0.000588,    # 1 NGN = 0.000588 EUR
    "GBP": 0.000513,    # 1 NGN = 0.000513 GBP
    "CAD": 0.000870,    # 1 NGN = 0.000870 CAD
    "JPY": 0.095238     # 1 NGN = 0.095238 JPY
}

# Currency symbols for nice display
currency_symbols = {
    "USD": "$",
    "EUR": "EUR",
    "GBP": "GBP",
    "CAD": "C$",
    "JPY": "JPY"
}


def validate_amount(amount_str):
    """
    Validate that the user input is a valid positive number.
    
    Parameters:
        amount_str (str): The user's input as a string
    
    Returns:
        float or None: The amount as a float if valid, None if invalid
    """
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("Error: Amount must be greater than 0.")
            return None
        return amount
    except ValueError:
        print("Error: Please enter a valid number (e.g., 1000 or 1000.50).")
        return None


def convert_ngn_to_currency(ngn_amount, currency_code):
    """
    Convert Nigerian Naira to a specified currency.
    
    Parameters:
        ngn_amount (float): The amount in Nigerian Naira to convert
        currency_code (str): The target currency code (USD, EUR, GBP, CAD, JPY)
    
    Returns:
        float or None: The converted amount, or None if currency is not supported
    """
    # Check if the requested currency exists in our dictionary
    if currency_code not in exchange_rates:
        return None
    
    # Get the exchange rate for the requested currency
    rate = exchange_rates[currency_code]
    
    # Multiply NGN amount by the exchange rate to get the target currency
    converted_amount = ngn_amount * rate
    
    return converted_amount


def display_conversion_result(ngn_amount, currency_code, converted_amount):
    """
    Display the conversion result in a clear, formatted way.
    
    Parameters:
        ngn_amount (float): The original amount in NGN
        currency_code (str): The target currency code
        converted_amount (float): The converted amount
    """
    symbol = currency_symbols.get(currency_code, currency_code)
    
    print("\n" + "=" * 60)
    print("CONVERSION RESULT")
    print("=" * 60)
    print(f"Input Amount:        {ngn_amount:>20,.2f} NGN")
    print(f"Target Currency:     {currency_code:>20}")
    print(f"Exchange Rate:       {exchange_rates[currency_code]:>20.6f} {currency_code}/NGN")
    print("-" * 60)
    print(f"Result:              {converted_amount:>20,.4f} {symbol}")
    print("=" * 60 + "\n")


def display_menu():
    """
    Display the list of available currencies that can be converted to.
    """
    print("\n" + "=" * 60)
    print("AVAILABLE CURRENCIES")
    print("=" * 60)
    for index, currency_code in enumerate(exchange_rates.keys(), 1):
        symbol = currency_symbols.get(currency_code, currency_code)
        rate = exchange_rates[currency_code]
        print(f"{index}. {currency_code:6} - {symbol:10} (Rate: {rate:.6f})")
    print("=" * 60 + "\n")


def convert_to_all_currencies(ngn_amount):
    """
    Convert an amount in NGN to all supported currencies and display results.
    
    Parameters:
        ngn_amount (float): The amount in Nigerian Naira
    """
    print("\n" + "=" * 60)
    print("CONVERSION TO ALL CURRENCIES")
    print("=" * 60)
    print(f"Amount in NGN: {ngn_amount:,.2f}\n")
    print(f"{'Currency':<12} {'Amount':<20} {'Symbol':<8}")
    print("-" * 60)
    
    for currency_code in exchange_rates.keys():
        converted = convert_ngn_to_currency(ngn_amount, currency_code)
        symbol = currency_symbols.get(currency_code, currency_code)
        print(f"{currency_code:<12} {converted:>15,.4f} {symbol:>8}")
    
    print("=" * 60 + "\n")


def main():
    """
    Main function that runs the currency converter program.
    This function handles user interaction and program flow.
    """
    print("\n" + "=" * 60)
    print("CURRENCY CONVERTER: NGN TO MAJOR WORLD CURRENCIES")
    print("=" * 60)
    print("Convert Nigerian Naira (NGN) to:")
    print("  - USD (US Dollar)")
    print("  - EUR (Euro)")
    print("  - GBP (British Pound)")
    print("  - CAD (Canadian Dollar)")
    print("  - JPY (Japanese Yen)")
    print("=" * 60 + "\n")
    
    # Main program loop - keeps running until user chooses to exit
    while True:
        # Display the menu of available currencies
        display_menu()
        
        # Prompt user for the amount in NGN
        print("Enter the amount in NGN (Nigerian Naira) to convert:")
        amount_input = input("Amount: NGN ").strip()
        
        # Validate the input amount
        ngn_amount = validate_amount(amount_input)
        if ngn_amount is None:
            print("Please try again.\n")
            continue
        
        # Ask user if they want to convert to a specific currency or all
        print("\nWhat would you like to do?")
        print("1. Convert to a specific currency")
        print("2. Convert to all currencies")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            # Specific currency conversion
            currency_input = input("Enter currency code (USD, EUR, GBP, CAD, JPY): ").strip().upper()
            
            # Convert the amount
            converted_amount = convert_ngn_to_currency(ngn_amount, currency_input)
            
            # Check if the currency was valid
            if converted_amount is None:
                print(f"\nError: '{currency_input}' is not a supported currency.")
                print(f"Supported currencies: {', '.join(exchange_rates.keys())}\n")
            else:
                # Display the successful conversion
                display_conversion_result(ngn_amount, currency_input, converted_amount)
        
        elif choice == "2":
            # Convert to all currencies
            convert_to_all_currencies(ngn_amount)
        
        elif choice == "3":
            # Exit the program
            print("\nThank you for using the Currency Converter!")
            print("Goodbye!\n")
            break
        else:
            # Invalid menu choice
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")