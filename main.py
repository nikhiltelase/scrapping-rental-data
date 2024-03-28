from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdr1SZQQ4iwp5WYF0ZyoGXnPXPsa7O6CduqQGRWujpf89sAwA/viewform"
HOSE_DATA_SITE = "https://appbrewery.github.io/Zillow-Clone/"
SHEET_URL = "https://api.sheety.co/06611c666efcc4e05beb6ca9c244f4fa/rentResearch/sheet1"


class HouseData:
    def __init__(self):
        self.address = []
        self.prices = []
        self.links = []

    def get_data(self):
        response = requests.get(HOSE_DATA_SITE)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
            for link in links:
                self.links.append(link.get("href"))
                self.address.append(link.text.strip().replace(",", ""))

            prices = soup.find_all(name="div", class_="StyledPropertyCardDataArea-fDSTNn")
            for price in prices:
                self.prices.append(price.text.strip().replace("/mo", "").split("+")[0])

            print("Fetched data from the website")
        else:
            print("Failed to fetch data from the website.")

    def feel_google_form(self):
        print("Felling Google Form...")
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_option)

        for i in range(len(self.prices)):
            driver.get(GOOGLE_FORM)
            time.sleep(3)
            address_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(self.address[i])

            price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(self.prices[i])

            link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(self.links[i])

            time.sleep(2)
            submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

            submit_button.click()

    def feel_google_sheet(self):
        header = {"Authorization": "Bearer 2846",
                  "Content-Type": "application/json"
                  }
        print("Feeling google sheet")
        for i in range(len(self.prices)):
            data = {
                "sheet1": {
                    'address': self.address[i],
                    'pricePerMonth': self.prices[i],
                    'links': self.links[i],
                }
            }
            response = requests.post(SHEET_URL, json=data, headers=header)
            if response.status_code != 200:
                print("Failed to add data to Google Sheet.")
                print("Response:", response.text)
                return
        print("Data added to Google Sheet successfully.")


house_data = HouseData()
house_data.get_data()
house_data.feel_google_sheet()


