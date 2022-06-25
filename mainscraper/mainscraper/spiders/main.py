
from signal import SIG_DFL
from wsgiref.util import setup_testing_defaults
import scrapy
import json

def links():
    with open('k.json') as k:
        a = json.load(k)
    m = []
    m = list(a.values())
    return m

class MainSpider(scrapy.Spider):
    name = "main"
    
    start_urls = links()

    def parse(self, response):
        
        # class method .................................................
        for item in response.css('article#item'):
            yield{
               "url" : "https://www.khabaronline.ir" + item.css("div.item-title a::attr(href)").get(),
               "title": item.css("div.item-title h1.title a::text").get(),
               "subtitle": item.css("div.item-title h4.subtitle a::text").get(),
               "time": item.css("div.item-date span::text").get(),
               "summary": item.css("div.item-summary p.summary::text").get(),
               "body": item.css("div.item-body div.item-text p::text").getall(),
               "body_img": item.css("div.item-body div.item-text p img::attr(src)").getall(),
               "summary_img":item.css("div.item-summary figure.item-img img::attr(src)").get(),
               "news_code": item.css("div.item-body div.item-code span::text").get(),
               "tags": item.css("section.tags a::text").getall(),
               
               
            }

            # # xpath method ................................................
            # for item in response.xpath('//section[@id="box4"]'): 
            # yield{
            #    "url" : item.xpath("//div[@class='desc']/h3/a/@href").extract(),
            #     "time" : item.xpath("//div[@class='desc']/h3/a/title/text()").extract(),
            #     "title": item.xpath("//div[@class='desc']/h3/a/text()").extract()
            # }


        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:       
        #     yield response.follow(next_page, callback=self.parse)

