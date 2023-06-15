import re

text = "United States Dollar USD 300.43 314.65 300.43 314.65 PUBLICCurrency *TT- Telegraphic Transfer"

# Use regular expression to find the desired value
matches = re.findall(r"\d+\.\d+", text)

if matches:
    first_match = matches[1]
    print("First Match:", first_match)
else:
    print("No match found")
