import scrapy
from  scrapy.loader import  ItemLoader
from  one4helloWorld.items import QuoteItem

class QuotesSpider(scrapy.Spider):


    name = "goodreads"

    start_urls = [
                  'https://www.goodreads.com/quotes?page=95',

                  ]


    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):

            loader = ItemLoader(item=QuoteItem(), selector=quote, response=response)

            loader.add_xpath('text', ".//div[@class='quoteText']/text()")
            loader.add_xpath('author', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class ='greyText smallText left']/a/text()")

            yield  loader.load_item()


            next_page = response.selector.xpath("//a[@class='next_page']/@href").extract_first()

            if next_page is not None:

                next_page_link = response.urljoin(next_page)

                yield scrapy.Request(url=next_page_link, callback=self.parse)


