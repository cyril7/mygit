#!/usr/bin/python

import sys
import urllib2
import time
from BeautifulSoup import BeautifulSoup
from optparse import OptionParser

NAGIOS_OK = 0
NAGIOS_WARNING = 1
NAGIOS_CRITICAL = 2
WEBSITE_ROOT = 'http://news.bbc.co.uk'

def fetch_top_story():
    status = []
    try:
        result = urllib2.urlopen(WEBSITE_ROOT)
        html = result.read()
        soup = BeautifulSoup(html)
        #a_tag = soup.find('a', 'tshsplash')
        '''
        <a class="story" href="http://www.bbc.co.uk/news/world-asia-china-23063829">US businessman Chip Starnes is freed after being detained in his factory in China for nearly a week by workers over a pay dispute</a>
        '''
        a_tag = soup.find('a', 'story')
        story_heading = a_tag.string
        topstory_rul = ''
        if a_tag.has_key('href'):
            #topstory_url = "%s%s" % (WEBSITE_ROOT, a_tag['href'])
            topstory_url = "%s" % a_tag['href']
        else:
            status = [NAGIOS_CRITICAL, 'ERROR: Top story anchor tag has no link']
        result = urllib2.urlopen(topstory_url)
        html = result.read()
        status = [NAGIOS_OK, story_heading]
    except:
        status = [NAGIOS_CRITICAL, 'ERROR: Failed to retrieve the top story']
    return status

def main():
    parser = OptionParser()
    parser.add_option('-w', dest='time_warn', default=1.8,
                      help="Warning threshold in seconds, default: %default")
    parser.add_option('-c', dest='time_crit', default=3.8,
                      help="Critical threshold in seconds, default: %default")
    (options, args) = parser.parse_args()

    if options.time_crit < options.time_warn:
        options.time_warn = options.time_crit

    start = time.time()
    code, message = fetch_top_story()
    elapsed = time.time() - start
    if code != 0:
        print message
        sys.exit(code)
    else:
        if elapsed < float(options.time_warn):
            print "OK: Top story '%s' retrieved in %f seconds" % (message, elapsed)
            sys.exit(NAGIOS_OK)
        elif elapsed < float(options.time_crit):
            print "WARNING: Top story '%s' retrieved in %f seconds" % (message, elapsed)
            sys.exit(NAGIOS_WARNING)
        else:
            print "CRITICAL: Top story '%s' retrieved in %f seconds" % (message, elapsed)
            sys.exit(NAGIOS_CRITICAL)

if __name__ == '__main__':
    main()
