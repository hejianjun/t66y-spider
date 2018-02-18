# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy.loader import ItemLoader
from t66ySpider.items import T66YspiderYazhouwumaItem
from t66ySpider.spiders.t66yBaseSpider import t66yBaseSpider

class t66yYazhouwumaSpider(t66yBaseSpider):
    name = 'YaZhouWuMa'
    start_urls = ["https://www.t66y.com/thread0806.php?fid=2"]
    unicode_next_page = u'\u4e0b\u4e00\u9801'
    imgchili_net = re.compile(r'''imgchili''')
    imagetwist_com = re.compile(r'''imagetwist''')
    # croea_com = re.compile(r'''croea.com''')

    def parse_thread(self, response):
        l = ItemLoader(item=T66YspiderYazhouwumaItem(), response=response)
        l.add_xpath('t_title', 'string(//title)')
        l.add_value('t_url', response.url)
        t_img_l = []
        for link in response.selector.xpath('//input/@src').extract() + response.selector.xpath('//img/@src').extract():
            if self.imgchili_net.search(link):
                t_img_l.append(link.replace('http://t','http://i'))
            elif self.imagetwist_com.search(link):
                t_img_l.append(link.replace('/th/','/i/'))
            # elif self.croea_com.search(link):
            #     t_img_l.append(link.replace('/th','/i/').replace('croea','imagetwist'))
            else:
                t_img_l.append(link)
        l.add_value('image_urls', t_img_l)
        t_torrent_list  = response.xpath('//a[contains(text(),"rmdown")]/text()').extract()
        for torrent_url in t_torrent_list:
            yield scrapy.Request(torrent_url, callback=self.parse_rmdown)
        
        l.add_xpath('file_urls', '//a[contains(text(),"rmdown")]/text()')
        return l.load_item()
    
    def parse_rmdown(self, response):
        scrapy.http.FormRequest.from_response(response,file_url)

