import requests
from bs4 import BeautifulSoup
import smtplib
URL='https://www.amazon.in/ABOUTTHEFIT-Active-Rejection-Precise-10-2-Inch/dp/B088TQZKCN/ref=sr_1_3?crid=3K6AKFNLGFFG5&dchild=1&keywords=stylus+for+ipad&qid=1598535574&sprefix=stylus%2Caps%2C358&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def checkPrice():


    

    page = requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')


    price =soup.find(id ='priceblock_ourprice').get_text()

    title =soup.find(id ='productTitle').get_text()

    
    price=price.replace(',','')

    converted_price=float(price[2:8])

    

   

    if(converted_price<3000):
        send_mail()


def send_mail():

    server =smtplib.SMTP('smtp.gmail.com',587)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login('codervpm@gmail.com','coding@git')

    subject='price fell down!!'

    body='price fell down!!  check th amazon https://www.amazon.in/ABOUTTHEFIT-Active-Rejection-Precise-10-2-Inch/dp/B088TQZKCN/ref=sr_1_3?crid=3K6AKFNLGFFG5&dchild=1&keywords=stylus+for+ipad&qid=1598535574&sprefix=stylus%2Caps%2C358&sr=8-3'


    msg = f'Subjects:{subject}\n\n{body}'

    server.sendmail(

        'codervpm@gmail.com',
        'minhajsinanvp@gmail.com',
        msg
    )

    print('hey mail has been sent')

    server.quit()

    


checkPrice()


# page = requests.get(URL,headers=headers)

# soup=BeautifulSoup(page.content,'html.parser')

# price =soup.find(id ='priceblock_ourprice').get_text()

# price=price.replace(',','')

# convert=float(price[2:8])

# print(convert)



