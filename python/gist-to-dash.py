#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Forked from https://gist.github.com/fedir/5466075
Changes:
- allows to import Github gists into a local DASH database (https://kapeli.com/dash) 
- gists are added to any existing snippet already in database
- filetypes are added, but support is very basic
- tags are not added at this stage
IMPORTANT
- the script requires an existing Dash database to begin with, so you probably want to make a backup copy of it first
WARNING: https://developer.github.com/v3/#rate-limiting
> For requests using Basic Authentication or OAuth, you can make up to 5,000 requests per hour. For unauthenticated requests, the rate limit allows you to make up to 60 requests per hour. Unauthenticated requests are associated with your IP address, and not the user making requests. 
@TODO: extract tags as well!
@TODO: extract from CodeBox too!
"""


import json
import urllib2
from subprocess import call
from urllib2 import urlopen
import os
import math

import sqlite3, sys

# TIP: safer to backup the old database first! 
DASH_DATABASE = "/Users/michele.pasin/Dropbox/Apps/Dash/mysnippets.dash"

# IMPORTANT: if you modify this make sure names match the dropdown in Dash (otherwise it'll crash)
ALLOWED_FILE_TYPES = ['HTML', 'Python', 'Shell', 'JavaScript']

# added to the abbreviation of a snippet to prevent accidental triggering 
SHORTCUT_PREFIX = "."


# GITHUB USERNAME - change as needed
USER = 'lambdamusic'
# GITHUB SETTINGS
perpage=30.0
userurl = urlopen('https://api.github.com/users/' + USER)
public_gists = json.load(userurl)
gistcount = public_gists['public_gists']
print "Found gists : " + str(gistcount)
pages = int(math.ceil(float(gistcount)/perpage))
print "Found pages : " + str(pages)


# if you want to test the script, this limits to page 1 or results
TESTING = False





def import_dash(title, body, syntax):
		"""
		update the default dash sqlite3 database
		"""
		conn = sqlite3.connect(DASH_DATABASE)
		c = conn.cursor()

		group = "snippets"
		c.execute("""
					insert into {} (title, body, syntax, usageCount)
					values (?, ?, ?, ?)
					""".format(group), (SHORTCUT_PREFIX + title, body, syntax, 1))

		conn.commit()
		conn.close()




def main():
		"""
		get snippets from github gists and move them to local Dash DB
		"""
		n = 0 
		for page in range(pages):
				pageNumber = str(page + 1)
				print "Processing page number " + pageNumber
				pageUrl = 'https://api.github.com/users/' + USER  + '/gists?page=' + pageNumber + '&per_page=' + str(int(perpage))
				u = urlopen (pageUrl)
				gists = json.load(u)
						 
				for gist in gists:
						n += 1
						print "==== %d ====" % n
						# print gist.keys()
						gistd = gist['id']
						gisturl = gist['html_url']
						gistdesc = gist['description'] or gistd
						gistfiles = gist['files']
						print "gistd: ", gistd
						print "gisturl: ", gisturl
						print "gistdesc: ", gistdesc
						print "gistfiles: ", len(gistfiles)
						for f in gistfiles:
								fileurl = gistfiles[f]['raw_url']
								_filetype = gistfiles[f]['language']
								if _filetype in ALLOWED_FILE_TYPES:
										filetype = _filetype
								else:
										filetype = "None"
								print "fileurl: ", fileurl           
								print "filetype: ", filetype, "(found='%s')" % _filetype 
					 
								if TESTING:
										# testing
										req = urlopen(fileurl)
										bodytext = req.read()
										encoding=req.headers['content-type'].split('charset=')[-1]
										ucontent = unicode(bodytext, encoding)
										bodytext = "# " + gisturl + "\n\n" + ucontent
										# bodytext = ucontent
										import_dash(gistdesc, bodytext, filetype)
								
								else:
										try:
												req = urlopen(fileurl)
												bodytext = req.read()
												encoding=req.headers['content-type'].split('charset=')[-1]
												ucontent = unicode(bodytext, encoding)
												bodytext = "# " + gisturl + "\n\n" + ucontent
												# bodytext = ucontent
												import_dash(gistdesc, bodytext, filetype)
										except Exception as e:
												print e
												print "*** ERROR WRITING TO sqlite3 ***"
												pass

				if TESTING:
						# so to avoid calling github API too much...
						break 



if __name__ == '__main__':
		main()