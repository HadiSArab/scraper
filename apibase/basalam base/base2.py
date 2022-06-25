
# scrape data and store desire product keys and values
import json,requests

# function to iterate over response and pick up desired keys and values 
# end of every lines put "," 
# if each keys include keys and values in itself, dont worry. this function generate nested dictionary automatically
def hadi(i,num):
    yield { 
        "id" : i["products"][num]["id"],
        "name" :i["products"][num]["name"],
        "photo":i["products"][num]["photo"]
    }

# dictionary to store nested json
dic = {}

# url is a variable to store desired api
# for loop is for scrape products 12 by 12. in each step scrape all 12 product and store by number "counter + p"
url = 'https://search.basalam.com/ai-engine/api/v2.0/product/search?productAds=true&adsImpressionDisable=false&literal=false&bazarGardy=false&from={}&size=12&filters.categories=1183&filters.namedTags=&filters.essenceTags=&filters.cities=&filters.hasDiscount=false&filters.isReady=false&filters.isExists=true&filters.hasDelivery=false&filters.vendorScore=false&filters.hasVideo=false&filters.basalamTag=&filters.excludeBasalamTag=&filters.queryNamedTags=false&exptags=runtime-click-20220609-control-1'
for counter in range(0,100,12):
    # send request to get json data using Basalam.com API
    resp = requests.get(url.format(counter))

    # convert response to python dictionary
    # ".text" help us to convert to dictionary
    resp = json.loads(resp.text)

    # first for loop prepare number for input "hadi" function
    # "len(resp["products"])" is number of keys
    # x is generator that store output of yield
    # to convert "x" from generator to dictionary using "m"
    # "dic[p] = m" store "m" in key number "p" in "dic" dictionary
    for p in range(len(resp["products"])):
        x = hadi(resp,p)
        for i in x:
            m = i
            print(m, "\n\n")
            
            # " counter + p"  allows to make ordered dictionary
            dic[counter+p] = m




# create or open a json file to convert dictionary to json and store json data 
with open('ali.json','w') as l:
    json.dump(dic,l)
