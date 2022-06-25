
# scrape data and store all product keys and values
import json,requests

# dictionary to store nested json
dic = {}

# url is a variable to store desired api
# this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
url = 'https://api.digikala.com/v1/categories/headphone/search/?page={}'
for counter in range(500):
    # send request to get json data using digikala.com API
    resp = requests.get(url.format(counter+1))

    # convert response to python dictionary
    # ".text" help us to convert to dictionary
    resp = json.loads(resp.text)
    print (len(resp["data"]["products"]))
    # first for loop prepare number for input "hadi" function
    # "len(resp["products"])" is number of keys
    # x is generator that store output of yield
    # to convert "x" from generator to dictionary using "m"
    # "dic[p] = m" store "m" in key number "p" in "dic" dictionary
    for p in range(len(resp["data"]["products"])):
        # " counter + p"  allows to make ordered dictionary
        
        dic[(counter*20)+p] = resp["data"]["products"][p]

print (len(resp["data"]["products"]))
# create or open a json file to convert dictionary to json and store json data 
with open('qw.json','w') as l:
    json.dump(dic,l)
