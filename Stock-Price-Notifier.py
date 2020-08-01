#by AbdulBasit Hakimi
import requests # pip install requests and pip install requests_html
from yahoo_fin import stock_info # pip install yahoo_fin
import time
from plyer import notification # pip install plyer

def get_symbol(company):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(company)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if company.lower() in x['name'].lower():
            return x['symbol']

brands = input("Enter the company name : ")
symbol = get_symbol(brands)
buyPrice = input("Enter the buy price of stock : ")
sellPrice = input("Enter the price you want to sell stock at : ")
b=0
s=0
price = stock_info.get_live_price(symbol)
print(price)
while True:
    price = stock_info.get_live_price(symbol)
    if(float(price) < float(buyPrice)) :
        if(b==0):
            notification.notify(
                title = "Price of your stock is below " + buyPrice,
                message = "Current price is " + str(price),
                app_icon = "C:\\Users\\Abdul\\Downloads\\3890929-chart-growth-invest-market-stock_111188.ico",
                timeout = 100
            )
            b=b+1
            s=0
    
    elif(float(price) > float(sellPrice)) :
        if(s==0):  
            notification.notify(
                title = "Price of your stock is above " + sellPrice,
                message = "Current Stock price is " + str(price),
                app_icon = "C:\\Users\\Abdul\\Downloads\\3890929-chart-growth-invest-market-stock_111188.ico",
                timeout = 100
            )
            s=s+1
            b=0