
# scrape data and store desire product keys and values
import json,requests

# function to iterate over response and pick up desired keys and values 
# end of every lines put "," 
# if each keys include keys and values in itself, dont worry. this function generate nested dictionary automatically
def hadi(i,num):
    yield { 
        "id" : i["data"]["products"][num]["id"],
        "name" :i["data"]["products"][num]["title_fa"],
        "en_name":i["data"]["products"][num]["title_en"],
        "url":"https://digikala.com" + i["data"]["products"][num]["url"]["uri"],
        "rate":i["data"]["products"][num]["rating"]["rate"],
        "count_of_rate":i["data"]["products"][num]["rating"]["count"],
        "image":i["data"]["products"][num]["images"]["main"]["url"]
    }

# dictionary to store nested json
dic = {}

# url is a variable to store desired api
# for loop is for scrape products 12 by 12. in each step scrape all 12 product and store by number "counter + p"
url = 'https://api.digikala.com/v1/categories/notebook-netbook-ultrabook/search/?page={}'
for counter in range(20):
    # send request to get json data using Basalam.com API
    resp = requests.get(url.format(counter+1))

    # convert response to python dictionary
    # ".text" help us to convert to dictionary
    resp = json.loads(resp.text)

    # first for loop prepare number for input "hadi" function
    # "len(resp["products"])" is number of keys
    # x is generator that store output of yield
    # to convert "x" from generator to dictionary using "m"
    # "dic[p] = m" store "m" in key number "p" in "dic" dictionary
    for p in range(len(resp["data"]["products"])):
        x = hadi(resp,p)
        for i in x:
            m = i
            print(m, "\n\n")
            
            # " counter + p"  allows to make ordered dictionary
            dic[(counter*20)+p] = m




# create or open a json file to convert dictionary to json and store json data 
with open('ali.json','w') as l:
    json.dump(dic,l)
