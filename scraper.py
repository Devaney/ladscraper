import scrapy


class LadSpider(scrapy.Spider):
    name = "lad_spider"
    start_urls = ['https://www.memset.com']

    def parse(self, response):
        SET_SELECTOR = 'a'
        for lada in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::attr(href)'
            yield {
                'name': lada.css(NAME_SELECTOR).extract_first(),
            }
