#!/usr/bin/env python
# coding: utf-8

import requests

host = 'medical-cost-env.eba-ghjpan9t.eu-west-1.elasticbeanstalk.com'
url = f'http://{host}/classify'

app_info = {
	"income": 0.9,
	""
}

response = requests.post(url, json=app_info)
print(response.text)

# This is the code that was used to send the case to the server and get the return shown in successful_response.png