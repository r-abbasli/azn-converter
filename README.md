# 💱 AZN Converter

A Python command-line tool that calculates currency exchange values using real-time rates from the Central Bank of Azerbaijan (CBAR).

## 🚀 Features
- Automatically retrieves the **latest daily exchange rates**.
- Converts **to/from Azerbaijani Manat (AZN)**.
- Handles **precious metals** measured in **troy ounces**.
- Gracefully exits on unsupported currencies or input errors.
- Includes **unit tests** for key functions.

## 👤 Who Is It For?
- **General users** needing quick exchange rate conversions.
- **Python learners** exploring web scraping, XML parsing, and CLI apps.
- **Recruiters** reviewing a backend-focused, testable, data-handling project.

## 🛠️ Tech Stack
- Python 3
- `requests`, `re`, `xml.etree.ElementTree`, `inflect`, `pytest`

## 📂 Project Structure
- `project.py`: Main CLI application
- `test_project.py`: Contains unit tests for core functions

## 🔍 How It Works
1. Scrapes CBAR’s currency rates page to find the current XML link.
2. Parses XML data into a list of currency exchange rates.
3. Converts user input amounts **to/from AZN** based on selected currency.
4. Detects and formats precious metals (e.g., "troy ounces of gold").
5. Validates and handles user inputs in clean loops.

## 🧪 Tests
- `test_ask_which_way`: Tests input direction logic.
- `test_ounce_prepend`: Tests special formatting for precious metals.
- `test_convert`: Mocks inputs and currency values to test conversion logic.

## 📺 Demo
[Watch on YouTube](https://www.youtube.com/watch?v=iVBfazqebNI)
