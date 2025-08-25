# Currency Converter

A Python script that converts currencies using real-time exchange rates from an API.

## Features

- Convert between different currencies using real-time exchange rates
- Simple command-line interface
- Error handling for invalid inputs

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
   ```

2. Install the required packages:
   ```
   pip install requests
   ```

## Usage

Run the script:

```
python app.py
```

Follow the prompts to:

1. Enter the currency to convert from (e.g., USD)
2. Enter the currency to convert to (e.g., EUR)
3. Enter the amount to convert

Example output:

```
💱 Welcome to Currency Converter 💱
==================================
Enter the currency to convert FROM (e.g., USD): USD
Enter the currency to convert TO (e.g., EUR): INR
Enter the amount to convert: 1000
💱 1000.0 USD = 87420.00 INR
```

## API Used

This project uses the [ExchangeRate-API](https://api.exchangerate-api.com) to get real-time exchange rates.

## License

MIT
