import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

STORE_ID = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment",
            "buyAlchemy lab", "buyPortal", "buyTime machine"]

chrome_driver_path = r"C:\Users\mzrar\.wdm\drivers\chromedriver\win32\104.0.5112\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, "cookie")

stop_time = float(time.time()) + (60 * 5)
t = float(time.time())
while True:
    cookie_button.click()
    if (t+5) <= float(time.time()):
        money = int("".join(driver.find_element(By.ID, "money").text.split(",")))
        for ID in STORE_ID[::-1]:
            item = driver.find_element(By.ID, ID)
            if item.text.split()[2] == "-":
                cookies_price = item.text.split()[3]
            else:
                cookies_price = item.text.split()[2]
            cookies_price = int("".join(cookies_price.split(",")))
            if money >= cookies_price:
                driver.find_element(By.ID, ID).click()
                t = float(time.time())
                break

    elif stop_time <= float(time.time()):
        break

print(f"cookies/second: {driver.find_element(By.ID, 'cps')}")




