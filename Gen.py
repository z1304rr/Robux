import random
import string
import webbrowser
import requests

def generate_roblox_codes(num_codes):
    codes = []
    for _ in range(num_codes):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        codes.append(code)
    return codes

def redeem_roblox_codes(codes):
    for code in codes:
        url = f"https://www.roblox.com/redeem?code={code}"
        response = requests.get(url)
        if "Code is already being used" in response.text:
            print(f"Code {code} is already being used.")
            break
        else:
            webbrowser.open(url)

# Ask the user how many Roblox codes they want to generate
num_codes = int(input("How many Roblox codes do you want to generate? "))

# Generate the specified number of Roblox codes
codes = generate_roblox_codes(num_codes)

# Redeem the generated Roblox codes
redeem_roblox_codes(codes)

print(f"Generated and redeemed {num_codes} Roblox codes.")
