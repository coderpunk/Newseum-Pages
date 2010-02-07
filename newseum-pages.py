#!/usr/bin/env python
"""
    Quick Newseum Frontpage Grabber script
    Copyright 2009 by Brian C. Lane
    Imp Software
    All Rights Reserved

    Modify CITIES list below to add the city designators (as seen in the
    URLS at http://www.newseum.org/todaysfrontpages/default.asp)
"""
import urllib2
import re
import os
import urlparse

# Add more cities here
CITIES = [ "AL_AS", "AL_MA",   ]

NEWSEUM_URL="http://www.newseum.org/todaysfrontpages/hr.asp?fpVname=%s"
NEWSEUM_IMG="http://www.newseum.org"

def fetchNewseumImage(city):
    """
    Fetch the image for a city
    """
    print "Parsing the page for %s" % (city)
    page = urllib2.urlopen(NEWSEUM_URL % city).read()

    # Quick and dirty grep for the image name
    match = re.search('<img class="tfp_lrg_img" src="(.*)" alt=', page)
    if match:
        img_url = NEWSEUM_IMG + os.path.abspath(match.group(1))
        print "Saving the image for %s" % (city)
        image = urllib2.urlopen(img_url).read()
        open(os.path.basename(match.group(1)), "wb").write(image)


def main():
    """
    Main code goes here
    """
    for city in CITIES:
        fetchNewseumImage(city)


if __name__ == '__main__':
    main()


