# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class AudMisclassifiedSpider(scrapy.Spider):
    name = 'notsonaivebayespart4scraper'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://philadelphia.craigslist.org/d/cell-phones/search/moa/']

    def parse(self, response):
        listings = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for listing in listings:
            yield {'Title':listing}

        next_rel_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        next_url = response.urljoin(next_rel_url)
        yield Request(next_url, callback=self.parse)