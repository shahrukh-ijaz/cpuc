# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DocumentDetail(scrapy.Item):
    filling_date = scrapy.Field()
    filled_by = scrapy.Field()
    description = scrapy.Field()
    document_type = scrapy.Field()
    document_link = scrapy.Field()
    proceeding_url = scrapy.Field()
    documents = scrapy.Field()


class Document(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    date = scrapy.Field()


class File(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()