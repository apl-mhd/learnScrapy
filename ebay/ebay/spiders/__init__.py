


import scrapy
from  scrapy.loader import  ItemLoader


class ebay(scrapy.Spider):


    name = "ebay"

    start_urls = [
                  'https://www.ebay.co.uk/sch/carpartsinmotion/m.html?_nkw=&_armrs=1&_ipg=&_from'

                  ]

    url=''

#response.css('li.sresult.lvresult')
    def parse(self, response):
        for i in response.css('li.sresult.lvresult'):

            ebay.url = i.css('a.vip::attr(href)').get()

            yield scrapy.Request(ebay.url, callback=self.productPage)


        next_page = response.css('a.gspr.next::attr(href)').get()

        if next_page is not None:
            yield scrapy.Request(url= next_page, callback=self.parse)    


    def productPage(self, response):

        x = response.css('div.itemAttr tr ')



        yield{
                'product_name': response.css("h1.it-ttl::text").get(),
                'sold': response.css("a.vi-txt-underline::text").get(),
                'price': response.css("span#prcIsum::attr('content')").get(),
                'item_number': response.css("div#descItemNumber::text").get(),
                'img': response.css("img#icImg::attr('src')").get(),
                'product_url':ebay.url,

                "description": [
                        {
                         "age": 42,
                         "email": "foo@example.com"
                         
                        }
                        ]

             }     


#
      














'''

            loader = ItemLoader(item=QuoteItem(), selector=quote, response=response)

            loader.add_xpath('text', ".//div[@class='quoteText']/text()")
            loader.add_xpath('author', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class ='greyText smallText left']/a/text()")

            yield  loader.load_item()


'''






'''
            yield{

                'product_name': i.css("a.vip::text").get(),
                'product_url': i.css('a.vip::attr(href)').get(),
                'img_url':i.css('img.img::attr(src)').get(),
                'price':i.css('li.lvprice.prc span::text').get(),
                

            }
            
'''