import pandas as pd
import datetime
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

for step in range(1,101): //100 steps
    price=[]
    col =[]
    times_stamp=datetime.datetime.now()
    times_stamp=times_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in HSI:
        price.append(real_time_price(stock_code)
    col=[time_stamp]
    col.extend(price)
    
    df=pd.DateFrame(col)
    df=df.T
    df.to_csv('real time stock data.csv', mode='a', header=False)
    print(col)
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
               
