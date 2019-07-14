


import scrapy
from  scrapy.loader import  ItemLoader


class ebay(scrapy.Spider):


    name = "ebay"

    start_urls = [
                  'https://www.ebay.co.uk/sch/carpartsinmotion/m.html?_nkw=&_armrs=1&_ipg=&_from'

                  ]

#response.css('li.sresult.lvresult')
    def parse(self, response):
        for i in response.css('li.sresult.lvresult'):


            yield{

                'product_name': i.css("a.vip::text").get(),
                'product_url': i.css('a.vip::attr(href)').get(),
                'img_url':i.css('img.img::attr(src)').get(),
                'price':i.css('li.lvprice.prc span::text').get(),
                

            }


        next_page = response.css('a.gspr.next::attr(href)').get()

        if next_page is not None:
            yield scrapy.Request(url= next_page, callback=self.parse)

'''
            next_page = response.selector.xpath("//a[@class='next_page']/@href").extract_first()

            if next_page is not None:

                next_page_link = response.urljoin(next_page)

                yield scrapy.Request(url=next_page_link, callback=self.parse)

'''
'''

            loader = ItemLoader(item=QuoteItem(), selector=quote, response=response)

            loader.add_xpath('text', ".//div[@class='quoteText']/text()")
            loader.add_xpath('author', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class ='greyText smallText left']/a/text()")

            yield  loader.load_item()


'''