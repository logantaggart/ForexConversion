from flask import Flask, flash, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
code = CurrencyCodes()

app = Flask(__name__)
app.config['SECRET_KEY'] = "DO NOT TELL!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def conversion():
    accept = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']
    orig = str(request.args.get('from'))
    new = str(request.args.get('to'))
    
    if not str(request.args.get('from')) in accept:
        flash("INVALID FIRST LINE SUBMISSION")
        if not str(request.args.get('to')) in accept:
            flash("INVALID SECOND LINE SUBMISSION")
            return render_template('index.html')
        try:
            float(request.args.get('num'))
        except ValueError:
            flash("INVALID NUMERICAL VALUE SUBMISSION")
            return render_template('index.html')
        return render_template('index.html')

    if not str(request.args.get('to')) in accept:
        flash("INVALID SECOND LINE SUBMISSION")
        return render_template('index.html')
        try:
            float(request.args.get('num'))
        except ValueError:
            flash("INVALID NUMERICAL VALUE SUBMISSION")
            return render_template('index.html')

    else:
        try:
            float(request.args.get('num'))
        except ValueError:
            flash("INVALID NUMERICAL VALUE SUBMISSION")
            return render_template('index.html')

    amount = float(request.args.get('num'))
    newamount = str(round(c.convert(orig, new, amount),2))
    symbol = str(code.get_symbol(new))

    return render_template('result.html', newamount=newamount, symbol=symbol)

