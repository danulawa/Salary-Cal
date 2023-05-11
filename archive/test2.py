from locale import currency
import requests
import json

str_annual_salary = str(171000)
str_basic_salary = str(0)
currency = "LKR"

url_1 = "https://api.apilayer.com/fixer/convert?to="+"LKR"+"&from="+currency+"&amount="+str_annual_salary

payload_1 = {}
headers_1 = {
"apikey": "fRq5sWPRvOY0io8V8C4nieQajxGtNCG8"
}

response_1 = requests.request("GET", url_1, headers=headers_1, data = payload_1)

parsed_json_1 = json.loads(response_1.text)
result_value_1 = parsed_json_1["result"]

converted_annual = int(result_value_1)

print(converted_annual)




url_2 = "https://api.apilayer.com/fixer/convert?to="+"LKR"+"&from="+currency+"&amount="+str_basic_salary

payload_2 = {}
headers_2 = {
"apikey": "fRq5sWPRvOY0io8V8C4nieQajxGtNCG8"
}

response_2 = requests.request("GET", url_2, headers=headers_2, data = payload_2)

parsed_json_2 = json.loads(response_2.text)
result_value_2 = parsed_json_2["result"]

converted_basic = int(result_value_2)


print("=====================================")
print(converted_basic)