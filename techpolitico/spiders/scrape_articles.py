import scrapy
from scrapy.crawler import CrawlerProcess
import json
from scrapy.http import Request

class ArticlesSpider(scrapy.Spider):
    name = 'scrape_articles'
    allowed_domains = ['politico.com']
    start_urls = []
            
    with open("output.json") as f:
        data = json.load(f)
        for i in data:
            temp = i['Link']
            start_urls.append(str(temp))


    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url=url, callback=self.parse_data, dont_filter=True)

    def parse(self, response):
        wrapper = response.css('div.page-wrapper')
        yield {
            'Title': wrapper.css('h2.headline::text').get(),
            'Text': wrapper.css('p::text').getall()
             }


    