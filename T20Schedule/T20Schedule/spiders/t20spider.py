"""
A spider for scrapping T20 match details.
"""

import ast
import scrapy
import sys

from T20Schedule.items import T20ScheduleItem
import ConfigReader

# Error message for missing configuration values.
MISSING_CONFIGURATION_VALUES = 'Some configuration values are missing. Please check the configuration file.'

class T20Spider(scrapy.Spider):
    """
    Spider class for scrapping T20 match details.
    """
    # configuration for the T20 spider.
    global config
    config = ConfigReader.read_config()
    if not config:
        # this is an error condition and we can not proceed further.
        sys.exit(1)
    try:
        # name is the name of the spider.
        name = config['name']
        # allowed_domains has list of domains that can be scrapped.
        allowed_domains = ast.literal_eval(config['allowed_domains'])
        # start_urls has the list of urls to start the scraping with.
        start_urls = ast.literal_eval(config['start_urls'])
    except KeyError as ke:
        print ('Improper configuration variable %s' %(ke, ))
        sys.exit(1)
    except Exception as e:
        # Lets catch the general exception too for graceful program termination.
        print e
        sys.exit(1)

    if not (name and allowed_domains and start_urls):
        # These are compulsory fields. We must have it.
        print MISSING_CONFIGURATION_VALUES
    
    def parse(self, response):
        """
        Method to parse the required items.
        """
        # urls has the common urls for all the items.
        try:
            urls = response.xpath(ast.literal_eval(config['base_url']))
            for url in urls:
                obj_t20schedule_item = T20ScheduleItem()
                obj_t20schedule_item['date'] = url.xpath(ast.literal_eval(config['rf_date'])).extract()
                obj_t20schedule_item['time'] = url.xpath(ast.literal_eval(config['rf_time'])).extract()
                match = url.xpath(ast.literal_eval(config['rf_match'])).extract()
                venue = url.xpath(ast.literal_eval(config['rf_venue'])).extract()
                if match:
                    # This is the condition where only one match is available as part of the url.
                    obj_t20schedule_item['match'] = match
                    obj_t20schedule_item['venue'] = venue
                else:
                    # Here more than 1 match is being played on the same section of the url.
                    obj_t20schedule_item['match1'] = url.xpath(ast.literal_eval(config['rf_match1'])).extract()
                    obj_t20schedule_item['venue1'] = url.xpath(ast.literal_eval(config['rf_venue1'])).extract()
                    obj_t20schedule_item['match2'] = url.xpath(ast.literal_eval(config['rf_match2'])).extract()
                    obj_t20schedule_item['venue2'] = url.xpath(ast.literal_eval(config['rf_venue2'])).extract()

                yield obj_t20schedule_item
        except Exception as e:
                # Its good to catch the exact exception for gracefull program termination.
                # lets catch the generic exception here as there can be many exceptions
                print ('Error seen while traversing through xpath in configuration file. Please check the coniguration file.') 
                print e
