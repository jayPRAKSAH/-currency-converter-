import requests  # pyright: ignore[reportMissingModuleSource] # Import the library at the top of your file

def convert_currency(from_currency, to_currency, amount):
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(from_currency)
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Get the conversion rate from the API response
        conversion_rate = data['rates'][to_currency.upper()]
        converted = amount * conversion_rate
        print(f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    else:
        print("Error fetching exchange rates.")

# Interactive CLI interface
def main():
    print("💱 Welcome to Currency Converter 💱")
    print("==================================")
    
    while True:
        try:
            from_currency = input("Enter the currency to convert FROM (e.g., USD): ").strip().lower()
            to_currency = input("Enter the currency to convert TO (e.g., EUR): ").strip().lower()
            amount = float(input("Enter the amount to convert: "))
            
            convert_currency(from_currency, to_currency, amount)
            
            # Ask if the user wants to continue
            continue_choice = input("\nDo you want to make another conversion? (y/n): ").strip().lower()
            if continue_choice != 'y' and continue_choice != 'yes':
                break
            print("\n")
                
        except ValueError:
            print("Error: Please enter a valid number for the amount.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Run the interactive interface if the script is executed directly
if __name__ == "__main__":
    main()

# Make sure to install the requests library before running the script
# You can install it using the following command:
# pip install requests
