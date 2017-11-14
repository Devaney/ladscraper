import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class LadSpider(scrapy.Spider):
    # The name of the spider
    name = "lad_spider"
    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ['memset.com']
    # The URLs to start with
    start_urls = ['https://www.memset.com']

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    Rule(LinkExtractor(canonicalize=True, unique=True), follow=True)

    def parse(self, response):
        #SET_SELECTOR = 'a'
        #for lada in response.css(SET_SELECTOR):

        #    NAME_SELECTOR = 'a ::attr(href)'
        #    yield {
        #        'name': lada.css(NAME_SELECTOR).extract(),
        #    }
        links = set(LinkExtractor(allow=self.allowed_domains, tags=("a"),attrs=("href")).extract_links(response))
        for link in links:
            yield {
                'XXXname': response.css('a').xpath('@href').extract(),
            }
