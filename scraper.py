import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

url_list = []

class LadSpidyTest(CrawlSpider):
    name = "lad_scraper"
    allowed_domains = ["www.memset.com"]
    start_urls = (
        'http://www.memset.com/',
    )
    rules = (
        Rule(LinkExtractor(canonicalize=True, unique=True), callback="parse_obj", follow=True),
    )

    def parse_obj(self, response):
        extractor = LinkExtractor(allow=self.allowed_domains, unique=True)
        links = extractor.extract_links(response)
        for i in links:
            url_list.append(i.url)

    def closed(self, reason):
        completeList()

def completeList():
    url_set = set(url_list)
    print len(url_list)
    print len(url_set)
