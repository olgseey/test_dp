# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class DnuSpider(scrapy.Spider):
    name = 'DNU_spider'
    allowed_domains = ['dnu.dp.ua']
    start_urls = ['http://dnu.dp.ua/']

    rules = (
        Rule(LinkExtractor(allow=('/page\d+/',)), callback='parse_page'),
    )

    def parse(self, response):
        pass
