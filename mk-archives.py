from __future__ import absolute_import, division, print_function, unicode_literals

import re, sys

PY3 = sys.version_info >= (3,)
if PY3:
    from urllib.request import urlopen
    from html.parser import HTMLParser
else:
    from urllib2 import urlopen
    from HTMLParser import HTMLParser

last_component_re = re.compile(r'\/(\w+)\/?$')
example_url_re = re.compile(r'(.*\/)http\:\/\/.*')
yyyymmdd_re = re.compile(r'\/[12][90]\d\d\d\d\d\d')

class_def_prolog = '''\
"""
doc string
"""

from memento import Memento, register_as'''

class_def_template = '''

@register_as(%(group)r)
class %(title)s(Memento):
    """
%(flavor)s
>>> obj = %(title)s().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""'''


class ArchivePageParser(HTMLParser):
    def __init__(self):
        self.state = 0
        self.examples = []
        self.flavor = []
        if PY3:
            super().__init__()
        else:
            HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'h3':
            id = dict(attrs).get('id', '')
            if id == 'ArchiveContent':
                self.state = 9
                self.flavor = []
            else:
                self.state = 0
        if tag == 'ul' and self.state == 0:
            self.state = 1
        if tag == 'li' and self.state == 1:
            self.state = 2
        if tag == 'code' and self.state == 2:
            self.state = 3
    def handle_endtag(self, tag):
        if tag == 'ul' and self.state == 1:
            self.state = 0
        if tag == 'li' and self.state == 2:
            self.state = 1
        if tag == 'code' and self.state == 3:
            self.state = 2
    def handle_data(self, data):
        if self.state == 3:
            match = example_url_re.match(data)
            if match:
                self.examples.append(match.group(1))
        if self.state == 9:
            self.flavor.append(data)

class IndexPageParser(HTMLParser):
    def __init__(self):
        self.state = 0
        if PY3:
            super().__init__()
        else:
            HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and self.state == 0:
            self.state = 1
        if tag == 'li' and self.state == 1:
            self.state = 2
        if tag == 'a' and self.state == 2:
            href = dict(attrs)['href']
            match = last_component_re.search(href)
            if match:
                http_response = urlopen(href)
                archive_parser = ArchivePageParser()
                if PY3:
                    buffer = str(http_response.read(), 'utf-8')
                else:
                    buffer = http_response.read()
                archive_parser.feed(buffer)
                if archive_parser.examples:
                    print(class_def_template % {
    'flavor': ''.join(s.lstrip() for s in archive_parser.flavor[1:]),
    'group': match.group(1),
    'title': match.group(1).title(),
    })
                    for example in archive_parser.examples:
                        if yyyymmdd_re.search(example):
                            continue
                        var = 'timemap' if 'timemap' in example else 'timegate'
                        print('    %s_template = %r' % (var, example + '%s'))
    def handle_endtag(self, tag):
        if tag == 'ul' and self.state == 1:
            self.state = 0
        if tag == 'li' and self.state == 2:
            self.state = 1

depot = urlopen('http://mementoweb.org/depot/')
print(class_def_prolog)
index_parser = IndexPageParser()
if PY3:
    buffer = str(depot.read(), 'utf-8')
else:
    buffer = depot.read()
index_parser.feed(buffer)
