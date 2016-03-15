# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class T20ScheduleItem(scrapy.Item):
    """
    Data structure for T20Schedule.
    """
    # To hold the date of the match
    date = scrapy.Field()
    # To hold the time of the match
    time = scrapy.Field()
    # Teams playing the match
    match = scrapy.Field()
    # location of the match
    venue = scrapy.Field()
    # if not match means there will be more 2 matches on the same day
    match1 = scrapy.Field()
    match2 = scrapy.Field()
    # location for 2 matches
    venue1 = scrapy.Field()
    venue2 = scrapy.Field()
