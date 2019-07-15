


import scrapy
from  scrapy.loader import  ItemLoader


class ebay(scrapy.Spider):


    name = "ebay"

    start_urls = [
                  'https://www.ebay.co.uk/sch/carpartsinmotion/m.html?_nkw=&_armrs=1&_ipg=&_from'

                  ]

    urlLink = ''

#response.css('li.sresult.lvresult')
    def parse(self, response):
        for i in response.css('li.sresult.lvresult'):

            urlLink = i.css('a.vip::attr(href)').get()

            yield scrapy.Request(urlLink, callback=self.productPage)


        next_page = response.css('a.gspr.next::attr(href)').get()

        if next_page is not None:
            yield scrapy.Request(url= next_page, callback=self.parse)    


    def productPage(self, response):

        trs = response.css('div.itemAttr tr')

        a={} 

        n=0

        for i in trs:
            if n==0:
                    
               y = "New: A brand-new, unused, unopened and undamaged item in original retail packaging (where packaging is applicable). If the item comes direct from a manufacturer," + "it may be delivered in non-retail packaging, such as a plain or unprinted box or plastic bag.   See the seller's listing for full details."
               n = n+1 
            else:
                y = i.css('td')[1].css('span::text').get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n\t\t\t\t\t\t\t\t\t \t\t\t', '')

        
            x = i.css('td::text')[0].get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n\t\t\t\t\t\t\t\t\t \t\t\t','')
            a[x]= y    


            x=None
            y=None


            try:

               if n==1:
                   x='Brand:'
                   n = n+1
               else:
                  x = i.css('td::text')[2].get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n\t\t\t\t\t\t\t\t\t \t\t\t', '')

               y = i.css('td')[3].css('span::text').get().replace('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '')   
               a[x]= y      
            except IndexError:
                gotdata = 'null'


            #
            #if x is not None:
             #   
              #  a[x]= y 
            
        yield{
                'product_name': response.css("h1.it-ttl::text").get(),
                'sold': response.css("a.vi-txt-underline::text").get(),
                'price': response.css("span#prcIsum::attr('content')").get(),
                'item_number': response.css("div#descItemNumber::text").get(),
                'img': response.css("img#icImg::attr('src')").get(),
                'product_url':response.request.url,


                "description": [

                        a

                        ]

             }     


