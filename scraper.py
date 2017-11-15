from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

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
        extractor = LinkExtractor(allow=self.allowed_domains)
        links = extractor.extract_links(response)
        url_list = []
        for link in links:
            #print link.url
            #url_list.append(link.url)
            if link.url not in url_list:
                url_list.append(link.url)

        unique_url_list = set(url_list)
        print unique_url_list
