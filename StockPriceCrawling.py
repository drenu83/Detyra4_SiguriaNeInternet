install requests

from bs4 install BeautifulSoup


url = ('https://finance.yahoo.com/quote/') +stock_code + ('.HK?p=') + stock_code + ('.HK&.tsrc=fin-srch')
r=requests.get(url)

print=(r.text)
