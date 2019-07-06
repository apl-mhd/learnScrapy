# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from  scrapy.loader import  ItemLoader
from w3lib.html import  remove_tags

from  scrapy.loader.processors import MapCompose, TakeFirst, Join



def remove_quotations(value):
    return value.replace(u"\u201c", '').replace(u"\u201d", '').\
        replace(u"\u2019",'').replace(u"\u2026", '').replace("\n", ''),




class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field(
    #
    # )

      text = scrapy.Field(

          input_processor = MapCompose(str.strip, remove_quotations),
          output_processor = TakeFirst()

      )


      author = scrapy.Field(
          input_processor=MapCompose(remove_tags, remove_quotations),
          output_processor=TakeFirst()

      )
      tags = scrapy.Field(
          input_processor=MapCompose(remove_tags),
          output_processor=TakeFirst()
      )


