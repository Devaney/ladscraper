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
        for link in links:
            print link.url

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
