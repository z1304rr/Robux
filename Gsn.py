import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor

def generate_roblox_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))

def redeem_roblox_code(code):
    url = f"https://www.roblox.com/redeem?code={code}"
    response = requests.get(url)
    if "Code is already being used" in response.text:
        return f"Code {code} is already being used."
    elif "Invalid code" in response.text:
        return f"Code {code} is invalid."
    else:
        return f"Code {code} has been redeemed."

# Ask the user how many Roblox codes they want to generate
num_codes = int(input("How many Roblox codes do you want to generate? "))

# Generate the specified number of Roblox codes
codes = [generate_roblox_code() for _ in range(num_codes)]

# Redeem the generated Roblox codes using a thread pool
with ThreadPoolExecutor() as executor:
    results = executor.map(redeem_roblox_code, codes)

for result in results:
    print(result)

print(f"Generated and redeemed {num_codes} Roblox codes.")
