


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

        trs = response.css('div.itemAttr tr')

        a={} 
    
        for i in trs:
        
            x = i.css('td::text')[0].get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n\t\t\t\t\t\t\t\t\t \t\t\t','')
            y = i.css('td')[1].css('span::text').get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n\t\t\t\t\t\t\t\t\t \t\t\t', '')
            a[x]= y    


            x=None
            y=None


            x = i.css('td::text')[2].get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n\t\t\t\t\t\t\t\t\t \t\t\t', '')
            if x is not None:
                y = i.css('td')[3].css('span::text').get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '')
                a[x]= y 
            


        yield{
                'product_name': response.css("h1.it-ttl::text").get(),
                'sold': response.css("a.vi-txt-underline::text").get(),
                'price': response.css("span#prcIsum::attr('content')").get(),
                'item_number': response.css("div#descItemNumber::text").get(),
                'img': response.css("img#icImg::attr('src')").get(),
                'product_url':ebay.url,

                "description": [

                        a

                        ]

             }     


