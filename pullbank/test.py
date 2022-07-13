from lxml import html
import requests,json

x = requests.get('https://faradars.org/courses/fvrprg101-programming-basics-concepts')
x = html.fromstring(x.content)

p = x.xpath('//*[@id="course-navigation-summary"]/div/div[3]/div[1]/div[2]/a/h6/text()')[0]
p = str(p)
print(p)