from locale import currency
from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        basic_salary = request.form['basic_salary']
        allowances = request.form['total_allowances']
        deductions = request.form['total_deductions']
        currency = request.form['pegged_currency']

        if not basic_salary:
            basic_salary = 0

        if not allowances:
            allowances = 0

        if not deductions:
            deductions = 0

        if not currency:
            currency = 'LKR'

        basic_salary = int(basic_salary)
        allowances = int(allowances)
        deductions = int(deductions)
        currency = str(currency)



        annual_salary = (basic_salary + allowances) * 12



        str_annual_salary = str(annual_salary)
        str_basic_salary = str(basic_salary)
        str_allowances = str(allowances)
        str_deductions = str(deductions)




        ##Converting Annual Salary
        ################################################################

        if annual_salary != 0:

            url_1 = "https://api.apilayer.com/fixer/convert?to="+"LKR"+"&from="+currency+"&amount="+str_annual_salary

            payload_1 = {}
            headers_1 = {
            "apikey": "QqHPV8tIj6KcqqQkNXdFUCO5fD8mzJ7Q"
            }

            response_1 = requests.request("GET", url_1, headers=headers_1, data = payload_1)

            parsed_json_1 = json.loads(response_1.text)
            result_value_1 = parsed_json_1["result"]

            converted_annual = int(result_value_1)

        else:

            converted_annual = int(0)




        ##Converting Basic Salary
        ################################################################

        if basic_salary != 0:

            url_2 = "https://api.apilayer.com/fixer/convert?to="+"LKR"+"&from="+currency+"&amount="+str_basic_salary

            payload_2 = {}
            headers_2 = {
            "apikey": "QqHPV8tIj6KcqqQkNXdFUCO5fD8mzJ7Q"
            }

            response_2 = requests.request("GET", url_2, headers=headers_2, data = payload_2)

            parsed_json_2 = json.loads(response_2.text)
            result_value_2 = parsed_json_2["result"]

            converted_basic = int(result_value_2)

        else:

            converted_basic = int(0)




        ##Converting Allowances
        ################################################################

        if allowances != 0:

            url_3 = "https://api.apilayer.com/fixer/convert?to="+"LKR"+"&from="+currency+"&amount="+str_allowances

            payload_3 = {}
            headers_3 = {
            "apikey": "QqHPV8tIj6KcqqQkNXdFUCO5fD8mzJ7Q"
            }

            response_3 = requests.request("GET", url_3, headers=headers_3, data = payload_3)

            parsed_json_3 = json.loads(response_3.text)
            result_value_3 = parsed_json_3["result"]

            converted_allowances = int(result_value_3)

        else:

            converted_allowances = int(0)



        ##Converting Deductions
        ################################################################

        if deductions != 0:

            url_4 = "https://api.apilayer.com/fixer/convert?to="+"LKR"+"&from="+currency+"&amount="+str_deductions

            payload_4 = {}
            headers_4 = {
            "apikey": "QqHPV8tIj6KcqqQkNXdFUCO5fD8mzJ7Q"
            }

            response_4 = requests.request("GET", url_4, headers=headers_4, data = payload_4)

            parsed_json_4 = json.loads(response_4.text)
            result_value_4 = parsed_json_4["result"]

            converted_deductions = int(result_value_4)

        else:

            converted_deductions = int(0)



        ##Calculating Tax
        ################################################################

        if converted_annual in range(0, 1200001):
            income_tax = 0
        elif converted_annual in range(1200000, 1700001):
            income_tax = ((converted_annual - 1200000) / 12) * 0.06
        elif converted_annual in range(1700000, 2200001):
            income_tax = (500000 / 12) * 0.06 + ((converted_annual - 1700000) / 12) * 0.12
        elif converted_annual in range(2200000, 2700001):
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + ((converted_annual - 2200000) / 12) * 0.18
        elif converted_annual in range(2700000, 3200001):
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + (500000 / 12) * 0.18 + (
                        (converted_annual - 2700000) / 12) * 0.24
        elif converted_annual in range(3200000, 3700001):
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + (500000 / 12) * 0.18 + (500000 / 12) * 0.24 + (
                        (converted_annual - 3200000) / 12) * 0.30
        else:
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + (500000 / 12) * 0.18 + (500000 / 12) * 0.24 + (
                        500000 / 12) * 0.30 + ((converted_annual - 3700000) / 12) * 0.36




        ##Calculating Final Net Salary
        ################################################################

        net_salary = (converted_basic * 92 / 100 + converted_allowances - income_tax) - converted_deductions

        net_salary = round(net_salary,2)
        income_tax= round(income_tax,2)

        return render_template('index.html', net_salary=net_salary, income_tax=income_tax)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
