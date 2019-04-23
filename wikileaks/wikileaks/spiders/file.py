# -*- coding: utf-8 -*-
import scrapy

class WikileaksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_name = scrapy.Field()
    file_content = scrapy.Field()

class FileSpider(scrapy.Spider):
    name = 'file'
    allowed_domains = ['wikileaks.org']
    start_urls = ['https://file.wikileaks.org/file/']

    def parse(self, response):
        if "pdf" in response.url.split(".") or "jpg" in response.url.split("."):
            file = WikileaksItem()
            file["file_name"] = response.url.split("/")[-1]
            file["file_content"] = response.body
            yield file
        else:
            file_urls = response.xpath('//pre//a//@href').extract()
            for url in file_urls:
                if "pdf" in url.split(".") or "jpg" in url.split("."):
                    url = "https://file.wikileaks.org/file/" + url
                    yield scrapy.Request(url, callback=self.parse)
                else:
                    continue
