from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.utils.url import urljoin_rfc
from test_dp.items import SitegraphItem


class GraphspiderSpider(CrawlSpider):
    name = 'graphspider'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com']

    rules = (
        Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = Selector(response)
        i = SitegraphItem()
        i['url'] = response.url
        i['http_status'] = response.status
        llinks=[]
        for anchor in hxs.xpath('//a[@href]'):
            href=anchor.xpath('@href').extract()[0]
            if not href.lower().startswith("javascript"):
                #llinks.append(urljoin_rfc(response.url,href))
                llinks.append(response.url)
                llinks.append(href)

        i['linkedurls'] = llinks
        return i