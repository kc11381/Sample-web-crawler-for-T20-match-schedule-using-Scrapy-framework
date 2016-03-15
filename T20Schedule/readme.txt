T20Schedule Spider
--------------------------------------------------------------------------------

Description:
     This program scraps the "in.bookmyshow.com" for T20 2016 match schedules.
     It gives the information on date, time, match and venue for a match.

To run:
     To run this program (from here) do:

     1. cd T20Schedule/spiders
     2. scrapy crawl T20Spider

To run and save the output:
    If you want to save the output of the program for later analysis you can do:

    1. To save in json format
       scrapy crawl T20Spider -o t20schedule.json 
    2. To save in csv format
       scrapy crawl T20Spider -o t20schedule.csv

Modules involved in the code:
    Follwing are different modules along with their descriptions:
     
    1. ConfigReader.py
       This reads the config for the Spider like name, start_with and so on from config.ini file.
    2. config.ini
       It has the values for configuration variables like name, start_with and so on.
    3. items.py
       It defines the data structure T20ScheduleItem for the spider.
    4. t20spider.py
       It contains the spider logic. It reads the config using ConfigReader and tries to scrap the data.
    5. Rest of the structure is as in documentation of scrapy project.
       Please follow : http://scrapy.org/
