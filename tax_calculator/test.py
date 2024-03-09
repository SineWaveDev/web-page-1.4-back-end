from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import requests
from flask import Flask
from flask_cors import CORS

# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": ""}})
#
# if __name__ == '__main__':
#     app.run()

payload = {
    "financial_year": "FY 2020-21",
    "pan": "XXXPX0000X",
    "age": 30,
    "residential_status": "Resident",
    "basic_salary": 720000,
    "hra": 120000,
    "rent_paid": 240000,
    "other_allowances": 50000,
    "interest_paid_on_homeloan": 0,
    "rent_received": 5000000,
    "property_tax_paid": 120000,
    "savings_interest": 10000,
    "fd_interest": 50000,
    "dividend_income": 12000,
    "other_income": 100000,
    "deductions_80_cce": 0,
    "deductions_80_ccd_2": 0,
    "deductions_80_ccd_1b": 0,
    "deductions_80_d": 0,
    "deductions_80_g": 0,
    "deductions_80_gg": 0,
    "deductions_80_eea": 0,
    "deductions_80_ee": 0,
    "deductions_80_e": 0,
    "deductions_80_dd": 0,
    "deductions_80_u": 0,
    "deductions_80_ddb": 0,
    "deductions_80_eeb": 0
}

# Now, you can make the API request with the defined payload
import requests

url = "https://api.example.com/calculate-tax"  # Replace this with the actual API endpoint
headers = {
    "Authorization": "Your_Authorization_Header_Value",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers, json=payload)

# Check the response status and process the response data accordingly
if response.status_code == 200:
    data = response.json()
    # Process the response data as needed
else:
    print("API request failed with status code:", response.status_code)