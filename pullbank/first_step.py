# Import required modules
from lxml import html
import requests,json

def titles(i,pag):
    yield{
        "نام مرغداری": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "مدیرعامل" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/text()'),
         "اطلاعات بیشتر":pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[7]/a/@href')

    }

dic = {}
for counter in range(15):
    # Request the page
    url = 'https://bankpoultry.com/modules.php?name=Bank&t=1&page={}'
    page = requests.get(url.format(counter+1))
    
    # Parsing the page
    # (We need to use page.content rather than 
    # page.text because html.fromstring implicitly
    # expects bytes as input.)
    page = html.fromstring(page.content)  
    for row in range(99):
        x = titles(row+2 , page)
        for i in x:
            print(i)
            dic[(counter*100)+row] = i

with open('k.json' , 'w') as lk:
    json.dump(dic,lk)
