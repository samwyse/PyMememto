'''Access an RFC 7089 web archive.

Copyright 2015 by Sam Denton, samwyse@gmail.com
'''

from __future__ import absolute_import, division, print_function, unicode_literals

__all__ = [ 'Memento', 'register_memento', 'lookup_memento' ]

__version__ = '0.1.0'

import re, sys

if sys.version_info < (3,):
    PY3 = False
    from urllib2 import Request, urlopen
else:
    PY3 = True
    from urllib.request import Request, urlopen


class RegexToken(object):
    r'''Create a token object for a parser.

>>> word_token = RegexToken(r'(\w+)', RegexToken.ILS)
>>> word_token('foo bar')
(3, ('foo',))
>>> word_token('foo bar', 3)
(7, ('bar',))
>>> word_token('foo bar', 7)
Traceback (most recent call last):
...
ValueError: expected '(\\w+)', found ''
'''
    ILS = IGNORE_LEADING_SPACE = 1<<15

    def __init__(self, pattern, flags=0):
        self.pattern = pattern
        if flags & self.IGNORE_LEADING_SPACE:
            pattern = r'\s*' +  pattern
            flags ^= self.IGNORE_LEADING_SPACE
        self.re = re.compile(pattern , flags=flags)

    def __call__(self, string, pos=0):
        match = self.re.match(string, pos)
        if not match:
            raise ValueError('expected %r, found %r' % (
                self.pattern,
                string[pos:]))
        return match.end(), match.groups()

class HeadRequest(Request):
    method = 'HEAD'

class Memento(object):
    timegate_template = None
    timemap_template = None

    # Create tokens needed for our parser
    uri_token = RegexToken(r'\<([^>]*)\>', RegexToken.ILS)
    param_token = RegexToken(r'\;\s*(\w+)\=', RegexToken.ILS)
    pvalue_token = RegexToken(r"([-!#$%&'*+.^_`|~\w]+)", RegexToken.ILS)
    qvalue_token = RegexToken(r'"([^"\\]*(?:\\.[^"\\]*)*)"', RegexToken.ILS)
    comma_token = RegexToken(r'\,', RegexToken.ILS)

    @classmethod
    def parse_link_header(self, linkheader):
        r'''
>>> from pprint import pprint

>>> pprint(Memento.parse_link_header('<foo>, <bar>'))
[('foo', {}), ('bar', {})]

>>> pprint(Memento.parse_link_header('<foo>; p=foo; q="foo bar", <bar>; p=bar'))
[('foo', {'p': 'foo', 'q': 'foo bar'}), ('bar', {'p': 'bar'})]
'''
        pos = 0
        retval = []
        while True:
            pos, (uri,) = self.uri_token(linkheader, pos)
            params = {}
            while True:
                try:
                    pos, (key,) = self.param_token(linkheader, pos)
                except ValueError:
                    break
                try:
                    pos, (value,) = self.qvalue_token(linkheader, pos)
                except ValueError:
                    pos, (value,) = self.pvalue_token(linkheader, pos)
                params[key] = value
            retval.append((uri, params))
            try:
                pos, nothing = self.comma_token(linkheader, pos)
            except ValueError:
                break
        return retval

    class _DictOfLists(dict):
        def __missing__(self, key):
            lst = self[key] = list()
            return lst

    @classmethod
    def pivot_links(self, links, pivot):
        r'''
>>> from pprint import pprint

>>> links = Memento.parse_link_header('<example.com>; rel=foo, <example.org>; rel="foo bar"')
>>> pprint(Memento.pivot_links(links, 'rel'))
{'bar': [('example.org', {})],
 'foo': [('example.com', {}), ('example.org', {})]}
'''
        retval = self._DictOfLists()
        for uri, params in links:
            params = params.copy()
            for value in params.pop(pivot).split():
                retval[value].append((uri, params))
        return retval

    class _Generic(object):
        '''Objects whose attributes are defined by a mapping object.'''
        def __init__(_self, **kwds):
            _self.__dict__ = kwds

    def get_timegate(self, uri=None, for_uri=None):
        if for_uri:
            if uri:
                raise TypeError('cannot specify both "uri" and "for_uri"')
            uri = self.timegate_template % for_uri
        http_response = urlopen(HeadRequest(uri))
        if 'link' in http_response.headers:
            raw_info = http_response.headers['link']
            links = self.parse_link_header(raw_info)
            by_rel = self.pivot_links(links, 'rel')
            return self._Generic(**by_rel)

    def get_timemap(self, uri=None, for_uri=None):
        if for_uri:
            if uri:
                raise TypeError('cannot specify both "uri" and "uri_for"')
            uri = self.timemap_template % for_uri
        http_response = urlopen(
            Request(uri, headers={'accept': 'application/link-format'}))
        if http_response.headers['Content-Type'] == 'application/link-format':
            raw_info = str(http_response.read(), 'utf-8')
            links = self.parse_link_header(raw_info)
            by_rel = self.pivot_links(links, 'rel')
            return self._Generic(**by_rel)


registry = {}

def register_memento(name, memento):
    ''' '''
    global registry
    registry[name.lower()] = memento

def register_as(name):
    ''' '''
    def wrapper(f):
        register_memento(name, f)
        return f
    return wrapper

def lookup_memento(name):
    ''' '''
    global registry
    return registry[name.lower()]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
