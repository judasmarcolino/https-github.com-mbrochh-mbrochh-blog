#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '/Users/martin/Projects/pelican-responsive/src/responsive'

AUTHOR = u'Martin Brochhaus'
SITENAME = u'martinbrochhaus.com'
SITEURL = 'http://martinbrochhaus.com'
MINI_BIO = u"I build software with Python, Django, ReactJS & React-Native. Every day. All day long."
BIO = u'<strong>Martin Brochhaus</strong> is the founder of <a href="http://bitmazk.com">Bitmazk Pte. Ltd.</a>. He is doing web development since 1998 and currently he is in love with Python & Django. Almost all of his work can be found on <a href="https://github.com/bitmazk">Github</a>. When he is not writing code, he gives <a href="https://speakerdeck.com/mbrochh">talks</a> or helps organizing <a href="https://pycon.sg">conferences</a>.'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/mbrochh', '&#xe037;'),
    ('Twitter', 'https://twitter.com/mbrochh', '&#xe086;'),
    ('Flickr', 'https://secure.flickr.com/photos/mbrochh/', '&#xe029;'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = '/Users/martin/Projects/mbrochh-blog/src/content'
STATIC_PATHS = [
    'CNAME',
    'images',
    'theme/img/avatar.jpg',
]

GOOGLE_ANALYTICS = 'UA-XXXXXXX-XX'
DISQUS_SITENAME = ''
