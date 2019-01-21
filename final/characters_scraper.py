# -*- coding: utf-8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Liste_des_personnages_de_Vampire_Diaries#Famille_des_Originels_et_autres_personnages_de_Vampire_Diaries']

    def parse(self, response):
        for link in response.css('span.mw-headline'):
            yield {'character': link.css('span.mw-headline ::text').extract_first()}