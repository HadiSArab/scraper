# Import required modules
from lxml import html
import requests,json
def ali(iurl):
   a = requests.get(iurl)
   a = html.fromstring(a.content)
   response = a.xpath('/html/body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[2]/tr/td/table/tr/td/table/tr/td/table/tr/td/table/tr[2]/td/div/text()')
   return(response)

def t1titles(i,pag):
    yield{
        "نام مرغداری": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "مدیرعامل" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[7]/a/@href')[0])

    }

def t2titles(i,pag):
    yield{
        "نام واحد": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/a/@href')[0])

    }

def t3titles(i,pag):
    yield{
        "نام شرکت": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/a/@href')[0])

    }

def t4titles(i,pag):
    yield{
        "نام": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/a/@href')[0])

    }

def t5titles(i,pag):
    yield{
        "نام سازمان": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "زمینه فعالیت" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/a/@href')[0])

    }

def t6titles(i,pag):
    yield{
        "نام و نام خانوادگی": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "رشته تحصیلی" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "میزان تحصیلات" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "شهرستان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[7]/a/@href')[0])

    }

def t7titles(i,pag):
    yield{
        "نام و نام خانوادگی": pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[2]/text()'),
        "بخش" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[3]/text()'),
        "سابقه کار" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[4]/text()'),
        "میزان تحصیلات" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[5]/text()'),
        "استان" : pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[6]/text()'),
        "اطلاعات بیشتر": ali('https://bankpoultry.com/'+ pag.xpath('//body/table/tr[6]/td[2]/table[2]/tr/td[2]/table[3]/tr/td/table/tr/td/table/tr/td/table/tr/td/table[1]/tr['+str(i)+']/td[7]/a/@href')[0])

    }


for t in range(7):
    
    dic = {}

    for counter in range(2):
        # Request the page
        url = 'https://bankpoultry.com/modules.php?name=Bank&t={}&page={}'
        page = requests.get(url.format(t+1 , counter+1))
        # Parsing the page
        # (We need to use page.content rather than 
        # page.text because html.fromstring implicitly
        # expects bytes as input.)
        page = html.fromstring(page.content)  
        for row in range(10):
            if t==0 :
                x = t1titles(row+2 , page)
            elif t==1:
                x = t2titles(row+2 , page)
            
            elif t==2:
                x = t3titles(row+2 , page)
            
            elif t==3:
                x = t4titles(row+2 , page)
            
            elif t==4:
                x = t5titles(row+2 , page)
            
            elif t==5:
                x = t6titles(row+2 , page)
            
            elif t==6:
                x = t7titles(row+2 , page)


            for i in x:
                print(i)
                dic[(counter*100)+row] = i

    with open(str(t+1)+'.json' , 'w') as lk:
        json.dump(dic,lk,indent=2)
