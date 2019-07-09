# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import Request
from linkcollect.items import LinkcollectItem

class LinkSpider(scrapy.Spider):
    name = 'link'
    domain_name = input('please input your need crawl domain:')
    allowed_domains = [str(domain_name)]
    domain_name = 'http://'+domain_name
    start_urls = [str(domain_name)]

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//a[@href]')

        #处理所有链接 去重部分和补全
        for link in links:
            item = LinkcollectItem()
            temp_link = str(link.re(r'href="(.*?)"')[0]) #处理每个url
            if temp_link:
                if not temp_link.startswith('http'):
                    temp_link = response.url + temp_link
                yield Request(temp_link, callback=self.parse) #继续爬取
                item['link'] = temp_link

                print(item['link'])
                #print(item['link_text'])
                yield item

        pass
