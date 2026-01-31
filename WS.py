import requests 
from bs4 import BeautifulSoup
import textwrap
import csv
import time
import random
import lxml

# url='https://www.booking.com/searchresults.html?ss=Vadodara&ssne=Vadodara&ssne_untouched=Vadodara&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4ArCR9ssGwAIB0gIkOTYzOWEwYjktZjg5YS00MDU2LTkzNzYtZjljYmY4MDRhZWU22AIB4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2114049&dest_type=city&checkin=2026-02-23&checkout=2026-02-25&group_adults=2&no_rooms=1&group_children=0'

def Web_scrapper(web_url,file_name):

    print("Thank You sharing the url and file name .\n ... \n Starting the web scrapping")
    t=random.randint(2,5)
    time.sleep(t)
    header={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
    responce= requests.get(web_url,headers=header)
    print(responce.status_code)
    print(responce.text[:1000])
    soup=BeautifulSoup(responce.text,'lxml')
    # print(soup.prettify())

    hotel_div=soup.find_all('div',role="listitem")
    # print(hotel_div)
    with open(f'{file_name}.csv','w',newline="",encoding="utf-8") as f:
        writter = csv.writer(f)
        writter.writerow(['Hotel_name','Location','Price','Rating','Link'])
        for hotel in hotel_div:
            hotel_name=hotel.find('div',class_="b87c397a13 a3e0b4ffd1").text.strip()
            hotel_name if hotel_name else 'NA'
            location=hotel.find('span',class_="d823fbbeed f9b3563dd4").text.strip()
            location if location else "NA"
            price=hotel.find('span',class_="b87c397a13 f2f358d1de ab607752a2").text.strip()
            price if price else "NA"
            rating=hotel.find('div',class_="f63b14ab7a dff2e52086").text.strip()
            rating if rating else 'NA'
            link=hotel.find('a' ,href=True).get('href')
            link if link else "NA"

            #saving
            writter.writerow([hotel_name,location,price,rating,link])
        # print(hotel_name)
        # print(location)
        # print(price)
        # print(rating)
        # print(link)
        # print("")

if __name__=='__main__':
    web_url=input("Please enter url : ")
    file_name=input("Please enter file name : ")

    Web_scrapper(web_url,file_name)