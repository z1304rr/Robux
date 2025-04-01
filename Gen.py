from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor

def generate_roblox_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))

def redeem_roblox_code(code, driver):
    url = f"https://www.roblox.com/redeem?code={code}"
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Code is already being used')]"))
        )
        return f"Code {code} is already being used."
    except:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid code')]"))
            )
            return f"Code {code} is invalid."
        except:
            print(f"Code {code} has been redeemed.")
            return f"Code {code} has been redeemed."

# Ask the user for Roblox credentials
username = input("Enter your Roblox username: ")
password = input("Enter your Roblox password: ")

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the Roblox login page
driver.get("https://www.roblox.com/login")

# Find the username and password fields and enter the credentials
username_field = driver.find_element(By.ID, "login-username")
username_field.send_keys(username)
password_field = driver.find_element(By.ID, "login-password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Welcome')]"))
    )
    print("Logged in successfully.")
except:
    print("Login failed.")
    driver.quit()
    exit()

# Ask the user how many Roblox codes they want to generate
num_codes = int(input("How many Roblox codes do you want to generate? "))

# Generate the specified number of Roblox codes
codes = [generate_roblox_code() for _ in range(num_codes)]

# Redeem the generated Roblox codes using a thread pool
with ThreadPoolExecutor() as executor:
    results = executor.map(lambda code: redeem_roblox_code(code, driver), codes)

for result in results:
    if "has been redeemed" in result:
        print(result)
    else:
        break

print(f"Generated and redeemed {num_codes} Roblox codes.")

# Close the browser
driver.quit()
