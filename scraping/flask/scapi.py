from crypt import methods

import requests
from flask import Flask, request, redirect, url_for
from flask import render_template
import json
from datetime import datetime

# get current date and time 
date = datetime.now() 
# costumize date format
date = date.strftime("%Y.%m.%d")

app = Flask(__name__)

with open ('first.json') as k:
    a = json.load(k)

@app.route('/digikala')
def digikala():
    cat = request.args['category']
    file_name = request.args['file'] + ".json"

    # dictionary to store nested json
    dic = {}

    # url is a variable to store desired api
    # this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
    url = 'https://api.digikala.com/v1/categories/{}/search/?page={}'
    for counter in range(10):
        # send request to get json data using digikala.com API
        resp = requests.get(url.format(cat,counter+1))

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
    
    # add date to json file
    date_dic={"date":date}
    dic.update(date_dic)

    # print (len(resp["data"]["products"]))
    # create or open a json file to convert dictionary to json and store json data 
    with open(str(file_name),'w') as l:
        json.dump(dic,l)
    
    return dic


@app.route('/basalam')
def basalam():
    cat = request.args['category'] 
    file_name = request.args['file'] + ".json"

    # dictionary to store nested json
    dic = {}

    # url is a variable to store desired api
    # for loop is for scrape products 12 by 12. in each step scrape all 12 product and store by number "counter + p"
    url = 'https://search.basalam.com/ai-engine/api/v2.0/product/search?productAds=true&adsImpressionDisable=false&literal=false&bazarGardy=false&from={}&size=12&filters.categories={}&filters.namedTags=&filters.essenceTags=&filters.cities=&filters.hasDiscount=false&filters.isReady=false&filters.isExists=true&filters.hasDelivery=false&filters.vendorScore=false&filters.hasVideo=false&filters.basalamTag=&filters.excludeBasalamTag=&filters.queryNamedTags=false&exptags=runtime-click-20220609-control-1'
    for counter in range(0,30,12):
        # send request to get json data using Basalam.com API
        resp = requests.get(url.format(counter,cat))

        # convert response to python dictionary
        # ".text" help us to convert to dictionary
        resp = json.loads(resp.text)

        # first for loop prepare number for input "hadi" function
        # "len(resp["products"])" is number of keys
        # x is generator that store output of yield
        # to convert "x" from generator to dictionary using "m"
        # "dic[p] = m" store "m" in key number "p" in "dic" dictionary
        for p in range(len(resp["products"])):
            # " counter + p"  allows to make ordered dictionary
            dic[counter+p] = resp["products"][p]
    
    
    # add date as an object to json file 
    date_dic={"date":date}
    dic.update(date_dic)

    # create or open a json file to convert dictionary to json and store json data 
    with open(str(file_name),'w') as l:
        json.dump(dic,l)

    
    return dic