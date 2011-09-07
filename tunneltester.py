#!/usr/bin/env python
# encoding: utf-8

# Onur Senture [08.2010]
# Put.io Tunnel Checker

import putio
import time
import pycurl
import os

class Downloader:
    def __init__(self):
        self.contents = ''
        self.line = 0

    def body_callback(self, buf):
        self.line = self.line + 1
        self.contents = "%s%i: %s" % (self.contents, self.line, buf)

    def fetch(self, url, username, password):

        print "dowloading: %s" % url
        retrieved_headers = Downloader()
        c = pycurl.Curl()
        c.setopt(c.URL, "%s" % url)
        c.setopt(c.WRITEFUNCTION, self.body_callback)
        c.setopt(c.HEADERFUNCTION, retrieved_headers.body_callback)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.UNRESTRICTED_AUTH, True)
        c.setopt(c.VERBOSE, False)
        c.setopt(c.USERPWD, '%s:%s' % (username,password) )
        c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
        c.perform()
        c.close()

        return self.contents

    def __str__(self):
        return self.contents

def connect_api():
    api = putio.Api(api_key= "tunneltester", api_secret="513offa763")
    return api

def test_routes():
    api = connect_api()
    item = api.get_items()[0]
    d = Downloader()
    url_prefix = [line.strip() for line in open('tunnels.txt')]
    for pre in url_prefix:
        url = 'http://'+ pre + 'put.io/download-file/8849/' + str(item.id)
        try:
            time_difference = time.time()
            d.fetch(url ,'tunneltester', 'tun3llt3st')
            if pre == "":
                print "%s --> %s" % ("default", "ok")
            else:
                print "%s --> %s" % (pre, "ok")
            time_difference = time.time() - time_difference
            print "download speed: " + str(((os.path.getsize('xspf_player_slim.swf'))/1024)/time_difference) + " kb/sn"

        except:
            if pre == "":
                print "%s --> %s" % ("default", "error")
            else:
                print "%s --> %s" % (pre, "error")
                
        print "------------------------"

if __name__ == "__main__":

    test_routes()
    print "end of test"
    print "testing github for mac"