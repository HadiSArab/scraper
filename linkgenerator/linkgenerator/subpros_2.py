
import subprocess
import json
from textwrap import indent
from typing import Text
from requests import request

# run scrapy command and create json file from link with desired name 
ss = "sa"
subprocess.run(["scrapy", "crawl", "linkgen", "-o", "sa.json"],capture_output=True,text=True)

# Opening JSON file and convert to Dictionary
with open(('{}.json').format(ss)) as json_file:
    i = json.load(json_file)

# explore into json keys and values and print desired object
s = 0
k = {}
for m in i:
    k[s] = "https://khabaronline.ir"+i[s]["url"]
    s+=1

with open ('k.json','w') as dfg:
  json.dump(k,dfg)

    
 



