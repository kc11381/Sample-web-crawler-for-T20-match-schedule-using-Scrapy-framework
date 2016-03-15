"""
Module to read the configuration file.
"""

import ConfigParser
import os
import subprocess
import sys

# Name of the configuration file. 
CONFIG_FILE = 'config.ini'
# Name of the section to look for.
SECTION_NAME = 'spider'
# Section not found error message
SECTION_ERROR_MSG = 'No such section exists: '

def read_config():
    """
    Method to read the config for spider.
    """
    config = ConfigParser.ConfigParser()
    if not os.path.isfile(CONFIG_FILE):
        print ('configuration file %s does not exists.' % (CONFIG_FILE, ))
        sys.exit(1)
    else:
        config.read(CONFIG_FILE)

    return config_section_map(config, SECTION_NAME)


def config_section_map(config, section):
    """
    Returns a dictionary of all the configuration variables.
    """
    return_dict = {}
    try:
        options = config.options(section)
        for option in options:
            try:
                return_dict[option] = config.get(section, option)
                if return_dict[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                return_dict[option] = None
    except ConfigParser.NoSectionError:
        print SECTION_ERROR_MSG, SECTION_NAME
        print 'Please check the configuration file'
        return_dict = None

    return return_dict
