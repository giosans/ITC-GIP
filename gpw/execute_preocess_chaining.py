# WPS Execute Operation

import requests, os

# loading payload of chaining process
payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\process_chaining.xml").read()

# wpsServerUrl connection to WPS services
wpsServerUrl = "http://130.89.221.193:85/geoserver/ows?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)
