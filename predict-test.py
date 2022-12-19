#!/usr/bin/env python
# coding: utf-8

import requests

host = 'fraud-detection-env.eba-5v5ncjpg.eu-west-1.elasticbeanstalk.com'
url = f'http://{host}/classify'

app_info = {
  "income": 0.9,
  "name_email_similarity": 0.296286,
  "current_address_months_count": 144,
  "customer_age": 50,
  "days_since_request": 0.005417,
  "intended_balcon_amount": -0.81622,
  "payment_type": "AB",
  "zip_count_4w": 366,
  "velocity_6h": 534.0473,
  "velocity_24h": 2670.91829,
  "velocity_4w": 3124.2981655,
  "bank_branch_count_8w": 718,
  "date_of_birth_distinct_emails_4w": 3,
  "employment_status": "CA",
  "credit_risk_score": 259,
  "email_is_free": 1,
  "housing_status": "BA",
  "phone_home_valid": 0,
  "phone_mobile_valid": 0,
  "bank_months_count": 15,
  "has_other_cards": 0,
  "proposed_credit_limit": 1500.0,
  "foreign_request": 0,
  "source": "INTERNET",
  "session_length_in_minutes": 31.7988193,
  "device_os": "windows",
  "keep_alive_session": 0,
  "device_distinct_emails_8w": 1,
  "month": 7
}

response = requests.post(url, json=app_info)
print(response.text)

# This is the code that was used to send the case to the server and get the return shown in successful_response.png