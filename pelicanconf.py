#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexandr Dermenji'
SITENAME = u'Alexandr Dermenji'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://alexandr.dermenji.ru'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10
RSS_FEED_SUMMARY_ONLY = True

# Blogroll
LINKS = (('Biserica Bunavestirea Chisinau', 'http://bunavestirea.md/'),
         ('Moldova Crestina', 'https://moldovacrestina.md/'),)

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/die2live'),
          ('Facebook',  'https://www.facebook.com/die2live'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
