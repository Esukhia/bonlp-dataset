# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#
# Extracted data -> EbookItem -> Pipeline -> open-pecha


import scrapy


class BoCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EbookItem(scrapy.Item):
    title = scrapy.Field()
    path = scrapy.Field()
