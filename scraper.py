import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class LadSpidyTest(CrawlSpider):
    name = "lad_scraper"
    allowed_domains = ["www.memset.com"]
    start_urls = (
        'http://www.memset.com/',
    )
    rules = (
        Rule(LinkExtractor(canonicalize=True, unique=True), callback="parse_obj", follow=False),
    )

    def parse_obj(self, response):
        extractor = LinkExtractor(allow=self.allowed_domains, unique=True)
        links = extractor.extract_links(response)
        url_list = []
        print url_list
        print "print before loooop"
        for i in links:
            #print ("Printing link ")
            #print i.url
            url_list.append(i.url)
            print "print DURING loooop"
            #print ("Printing LIST ")
            #print len(url_list)
            #print ("printing request")
            #print scrapy.Request(url=i.url)
        print "print afteerrr loooop"
        print url_list

    #def print_lists():
    #    unique_url_list = set(self.url_list)
    #    print unique_url_list
