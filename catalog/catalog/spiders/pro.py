import scrapy
import csv
class catalog_project(scrapy.Spider):
    name='catalog_project'
    start_urls=['http://dmoztools.net']


    def parse(self,response):
        website_name = response.css('a::text')[12:].extract()
        website_url = response.css("a").xpath("@href")[12:].extract()
        yield {'website_name': website_name, 'website_url': website_url}







