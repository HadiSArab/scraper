
import subprocess
import json

a = subprocess.run(["scrapy","crawl","link"])
print(a)

with open ('alli.json','w') as json_file:
    json.dump('alli.json',a,sort_keys=True,indent=2)