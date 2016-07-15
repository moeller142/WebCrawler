#!/usr/bin/python
import HTMLParser
import urllib
import threading
import sys

class Crawler(threading.Thread):
    
    def _init_(self):    
        threading.Thread._init_(self)        

    def run(self):
        #sync
        while linksToBeVisited: 
            lock.aquire()
            if linksToBeVisited:
                link = linksToBeVisited.pop()
                linksVisited.append(link)
            lock.release()
            extractContent(link)         

class parser(HTMLParser.HTMLParser):
    def handle_data(self, data):



def extractContent(link):
    #open link and extract html data
    htmlString = urllib.urlopen(link).read()
    #search for term

searchTerm = sys.argv[0]
numberOfThreads = sys.argv[1]
linksVisited =  []
linksToBeVisited = list(open("./links.txt"))
threads = []
lock = threading.Lock()
linksFound = []

#start threads
for i in range(0, numberOfThreads):
    threads[i] = Crawler()
    thread.start()

#wait for threads
for t in threads:
    t.join()

#display links
