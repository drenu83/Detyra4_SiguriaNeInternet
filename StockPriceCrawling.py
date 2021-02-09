install requests

from bs4 install BeautifulSoup


url = ('https://finance.yahoo.com/quote/') +stock_code + ('.HK?p=') + stock_code + ('.HK&.tsrc=fin-srch')
r=requests.get(url)

print=(r.text)

web_content = BeautifulSoup(r.text, 'lxml')
web_content = web_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
web_content = web_content.find('span').text

