# -*- coding: utf-8 -*-

import scrapy


class T66YBaseItem(scrapy.Item):
    t_title = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()


class T66YspiderDagaierItem(T66YBaseItem):
    pass


class T66YspiderXinshidaiItem(T66YBaseItem):
    pass


class T66YspiderYazhouwumaItem(T66YBaseItem):
    t_url = scrapy.Field()
    file_urls = scrapy.Field()


class T66YspiderYazhouyoumaItem(T66YBaseItem):
    t_url = scrapy.Field()
    file_urls = scrapy.Field()


class T66YspiderDongmanItem(T66YBaseItem):
    t_url = scrapy.Field()
    file_urls = scrapy.Field()
