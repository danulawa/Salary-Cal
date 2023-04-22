from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        basic_salary = int(request.form['basic_salary'])
        allowances = int(request.form['total_allowances'])
        annual_salary = (basic_salary + allowances) * 12

        if annual_salary in range(0, 1200001):
            income_tax = 0
        elif annual_salary in range(1200000, 1700001):
            income_tax = ((annual_salary - 1200000) / 12) * 0.06
        elif annual_salary in range(1700000, 2200001):
            income_tax = (500000 / 12) * 0.06 + ((annual_salary - 1700000) / 12) * 0.12
        elif annual_salary in range(2200000, 2700001):
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + ((annual_salary - 2200000) / 12) * 0.18
        elif annual_salary in range(2700000, 3200001):
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + (500000 / 12) * 0.18 + (
                        (annual_salary - 2700000) / 12) * 0.24
        elif annual_salary in range(3200000, 3700001):
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + (500000 / 12) * 0.18 + (500000 / 12) * 0.24 + (
                        (annual_salary - 3200000) / 12) * 0.30
        else:
            income_tax = (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + (500000 / 12) * 0.18 + (500000 / 12) * 0.24 + (
                        500000 / 12) * 0.30 + ((annual_salary - 3700000) / 12) * 0.36

        net_salary = basic_salary * 92 / 100 + allowances - income_tax
        return render_template('index.html', net_salary=net_salary)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
