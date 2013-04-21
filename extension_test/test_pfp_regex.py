#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
from pfp_regex import pfp_regex

if __name__ == "__main__":
    pfp = pfp_regex()
    if len(sys.argv) > 1:
        argm = sys.argv[1]
        if argm == "preg_match":
            
            #see http://docs.python.org/2/howto/regex.html to learn about regex in python
            print "-"*15
            match1 = pfp.preg_match("[0-9]+","hello 123")#equivalent:\d
            print "Result 1:",match1.group(0),"\n","-"*15
            match2 = pfp.preg_match("[^0-9]+","hello 123")#equivalent:\D
            print "Result 2:",match2.group(0),"\n","-"*15
            match3 = pfp.preg_match("[a-z0-9\s]+","hello 123")#equivalent: \w\s
            print "Result 3:",match3.group(0),"\n","-"*15
        if argm == "preg_match_all":
            
            match = pfp.preg_match_all('<a href="(.*?)">(.*?)</a>','<a href="http://www.python.org">Python</a>')
            print match
        if argm == "preg_replace":
            
            print "-"*15
            print "Result 1:", pfp.preg_replace("[0-9]+","a","hello 123"),"\n","-"*15
            print "Result 2:", pfp.preg_replace(['href="(.*?)"','>(.*?)<'],['href="#"','>Nothing here<'],'<a href="http://www.python.org">Python</a>'),"\n","-"*15
            print "Result 3:", pfp.preg_replace(['http|https"','www'],'ftp','<a href="http://www.python.org">Python</a>'),"\n","-"*15
            