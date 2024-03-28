## Rental Data Automation with Python

This project automates the process of collecting rental data from a website, filling out Google Forms with that data, and storing it in a Google Sheet. 

### Features

* **Web Scraping:** Uses BeautifulSoup to extract property details like addresses, prices, and links from a housing rental website.
* **Automated Google Form Filling:** Leverages Selenium to automatically populate Google Forms with the scraped data.
* **Google Sheet Integration:** Employs the Sheety API to seamlessly add the scraped data to a centralized Google Sheet for easy access and management.

### Dependencies

* BeautifulSoup4 (`bs4`)
* Selenium
* Requests
* Sheety API

### Usage

1. **Configure API Keys:**
    * Obtain API keys for Sheety and potentially Selenium (depending on your setup).
    * Update the `GOOGLE_FORM`, `HOSE_DATA_SITE`, and `SHEET_URL` variables with your respective links.
    * Store your API keys securely (**not** in this file).
2. **Run the Script:**
    * Execute the script using `python main.py` (assuming the script is named `main.py`).

### Code Structure

* `main.py`: Defines a class `HouseData` to manage scraped data (address, price, link).
    * `get_data`: Scrapes data from the rental website using BeautifulSoup.
    * `feel_google_form`: Automates Google Form filling with Selenium.
    * `feel_google_sheet`: Uploads data to Google Sheet using the Sheety API.
* `main.py`: Creates an instance of `HouseData`, retrieves data, and populates Google Forms and Sheets.

### How it Works

1. The script initializes a `HouseData` object.
2. The `get_data` method scrapes data from the rental website and stores it in the object.
3. The `feel_google_form` method iterates through the scraped data, opening Google Forms and filling them with the corresponding address, price, and link.
4. The `feel_google_sheet` method iterates through the data again, sending requests to the Sheety API to add each entry to the specified Google Sheet.

### Disclaimer

This script is for educational purposes only. Use it responsibly and be mindful of website terms of service regarding web scraping.
