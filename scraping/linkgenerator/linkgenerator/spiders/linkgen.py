# this code crawl given page and generate a json file include "title", "url", "time" 
# this code will generate feed for main scraping code ..............................

from signal import SIG_DFL
from wsgiref.util import setup_testing_defaults
import scrapy

class linkgenspider(scrapy.Spider):
    name = "linkgen"
    start_urls=["https://www.khabaronline.ir/service/Politics"]

    def parse(self, response):
        
        # class method .................................................
        for item in response.css('div.desc'):
            yield{
               "url" : item.css("a::attr(href)").get(),
               "time": item.css("a::attr(title)").get(),
               "title": item.css("a::text").get(),
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

