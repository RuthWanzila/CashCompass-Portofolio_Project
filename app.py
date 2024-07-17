from flask import Flask, render_template, redirect, url_for, request
from utils import load_transactions, save_transactions, format_date, create_directory
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

TRANSACTIONS_FILE = 'transactions.csv'
TRANSACTIONS_DIR = 'data'

@app.route('/')
def index():
    transactions = load_transactions(os.path.join(TRANSACTIONS_DIR, TRANSACTIONS_FILE))
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'date': request.form['date'],
            'description': request.form['description'],
            'amount': request.form['amount'],
            'category': request.form['category']
        }
        
        transactions = load_transactions(os.path.join(TRANSACTIONS_DIR, TRANSACTIONS_FILE))
        transactions.append(transaction)
        save_transactions(transactions, os.path.join(TRANSACTIONS_DIR, TRANSACTIONS_FILE))
        return redirect(url_for('index'))
    
    return render_template('add_transaction.html')

if __name__ == '__main__':
    create_directory(TRANSACTIONS_DIR)
    app.run(debug=True)
