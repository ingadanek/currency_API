import requests
import sys
from dateutil import parser

DATE_FORMAT = '%Y-%m-%d'

try:
    currency = sys.argv[2]
except IndexError:
    currency = input('Please enter a currency: ')

currency = currency.upper()

try:
    date_as_str = sys.argv[3]
except IndexError:
    date_as_str = input('Please provide the date: ')


try:
    date = parser.parse(date_as_str)
except  ValueError:
    print('Invalid date format')
    sys.exit(1)

# date = date.date()
date_for_url = date.strftime(DATE_FORMAT)

URL = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_for_url}/?format=json"

resp = requests.get(URL)

if resp.status_code == 404:
    print('No data')
    sys.exit(2)

if not resp.ok:
    print('Unexpected Server Response')
    sys.exit(3)

json = resp.json()

try:
    ex_rate = json['rates'][0]['mid']
except (ValueError, KeyError):
    print('Invalid server response')
    sys.exit(4)


print(f"1 {currency} = {ex_rate} PLN on the following day {date_for_url}")

