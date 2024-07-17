import csv
import os

def load_transactions(file_path):
    transactions = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print("Error: File not found at '{}'".format(file_path))
    return transactions

def save_transactions(transactions, file_path):
    try:
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['date', 'description', 'amount', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except Exception as e:
        print("Error: Unable to save transactions to file '{}'. Error: {}".format(file_path, str(e)))

def format_date(date_str):
    return date_str.split('-')[2] + '/' + date_str.split('-')[1] + '/' + date_str.split('-')[0]

def create_directory(directory_path):
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    except Exception as e:
        print("Error: Unable to create directory '{}'. Error: {}".format(directory_path, str(e)))
