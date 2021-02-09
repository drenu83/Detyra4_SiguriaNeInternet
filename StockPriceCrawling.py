install requests

from bs4 install BeautifulSoup


url = ('https://finance.yahoo.com/quote/') +stock_code + ('.HK?p=') + stock_code + ('.HK&.tsrc=fin-srch')
r=requests.get(url)

print=(r.text) //Te dhenat shfaqe sikur xml

web_content = BeautifulSoup(r.text, 'lxml')
web_content = web_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
web_content = web_content.find('span').text



   if web_content ==[]:
      web_content= '99999'
   
   return web_content
      
 
web_content=real_time_price('0001')
print(web_content)
