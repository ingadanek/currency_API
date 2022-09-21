
# NBP Web API - Currency Exchange Rate

Using Python and its packages to read and analyse data from the National Bank of Poland (NBP). Data is obtained through an API and provides the indicated currency's rate on the specific day.

This app could be useful for banks in Poland to be able to correctly issue invoices in foreign currency - regulations require that the amounts on such invoices be converted into zloty according to the NBP's exchange rates on specific days.

## How to use:

Option 1:
Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' and filepath followed by url. Once the code's executed, user is asked to provide a date (in any reasonable format) and chosen currency. 

Option 2:
Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' and filepath followed by url and currency. Once the code's executed, user is asked to provide a date (in any reasonable format). 

Option 3:
Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' and filepath followed by url, currency and date (as string if it contains white spaces).

e.g. `python projects/API_NBP/currency.py "http://api.nbp.pl/en.html"`

e.g. `python projects/API_NBP/currency.py "http://api.nbp.pl/en.html" USD`

e.g. `python projects/API_NBP/currency.py "http://api.nbp.pl/en.html" USD '20 Oct 2021'`


## Code and Resources Used
**Python Version:** `3.10.6`

**Modules:** `requests, sys, parser` 

**url:** `http://api.nbp.pl/en.html`
