# Import required modules
from lxml import html
import requests,json
def ali(iurl):
   a = requests.get(iurl)
   a = html.fromstring(a.content)
   response = a.xpath('/html/body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[2]/tr/td/table/tr/td/table/tr/td/table/tr/td/table/tr[2]/td/div/text()')
   return(response)

def titles(i,pag):
    yield{
        "نام مرغداری": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "مدیرعامل" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[7]/a/@href')[0])

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
    for row in range(100):
        x = titles(row+2 , page)
        for i in x:
            print(i)
            dic[(counter*100)+row] = i

with open('totally.json' , 'w') as lk:
    json.dump(dic,lk)
