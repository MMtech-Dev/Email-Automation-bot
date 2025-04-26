from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException

df = pd.read_csv("emails.csv")
service = Service("chromedriver.exe")

driver = webdriver.Chrome(service=service)
url = "https://www.techlistic.com/p/selenium-practice-form.html"
driver.get(url)

if __name__ == "__main__":
    for email in df["email"]:
        try:
            input_field = driver.find_element("name", "firstname")
            input_field.clear()
            input_field.send_keys(email)
            print(f"Inserted email: {email}")
            time.sleep(1)
        except NoSuchElementException as e:
            print(f"Could not find the imput field: {e}")
        except Exception as e:
            print(f"Error inserting {email}: {e}")

    driver.quit()