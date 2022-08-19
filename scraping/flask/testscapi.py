
import requests
import json
from datetime import datetime
date = datetime.now() 
# costumize date format
date = date.strftime("%Y.%m.%d")
last_dic={}

cat = ["headphone","casual-shoes-for-men"]
pages = 1

# url is a variable to store desired api
# this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
url = 'https://api.digikala.com/v1/categories/{}/search/?page={}'
for j in cat:
    # dictionary to store nested json
    dic = {}

    for counter in range(pages):
        # send request to get json data using digikala.com API
        resp = requests.get(url.format(j,counter+1))

        # convert response to python dictionary
        # ".text" help us to convert to dictionary
        resp = json.loads(resp.text)

        # print (len(resp["data"]["products"]))
        # first for loop prepare number for input "hadi" function
        # "len(resp["products"])" is number of keys
        # x is generator that store output of yield
        # to convert "x" from generator to dictionary using "m"
        # "dic[p] = m" store "m" in key number "p" in "dic" dictionary
        for p in range(len(resp["data"]["products"])):
            # " counter + p"  allows to make ordered dictionary
            
            dic[(counter*20)+p] = resp["data"]["products"][p]


    # beacuse flask doesnt show result with date and time in browser, i define a variable names "s" to store dic without date and show it in browser
    # json file involved date 
    s={}
    for t in dic:
        s[t] = dic[t]

    # add date to json file
    date_dic={"date":date}
    dic.update(date_dic)

    #don in variable to jasonify dic and finally store in last dic
    don = {j:dic}
    last_dic.update(don)

# print (len(resp["data"]["products"]))
# create or open a json file to convert dictionary to json and store json data 
with open(str("./digikala/ali"),'w') as l:
    json.dump(last_dic,l,indent=2)