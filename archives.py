## Auto-generated code.

"""
doc string
"""

from memento import Memento, register_as


@register_as('archivetoday')
class Archivetoday(Memento):
    """
archive.today is "your personal Wayback Machine". For information, see
http://archive.today.

>>> obj = Archivetoday().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
[('http://archive.today/20120527002537/http://www.w3.org/TR/webarch/', {'datetime': 'Sun, 27 May 2012 00:25:37 GMT'})]
"""
    timegate_template = 'http://archive.today/timegate/%s'
    timemap_template = 'http://archive.today/timemap/%s'

@register_as('archiveit')
class Archiveit(Memento):
    """
Archive-It is a subscription-based web, on-demand archive affiliated
with the Internet Archive. Information about its collection is
available from its home page.

>>> obj = Archiveit().get_timegate(for_uri='http://www.ameb.unimelb.edu.au/')
>>> obj.first
[('http://wayback.archive-it.org/all/20130930230459/http://ameb.unimelb.edu.au/', {'datetime': 'Mon, 30 Sep 2013 23:04:59 GMT'})]
"""
    timegate_template = 'http://wayback.archive-it.org/all/%s'
    timemap_template = 'http://wayback.archive-it.org/all/timemap/link/%s'

@register_as('dbpedia')
class Dbpedia(Memento):
    """
This archive contains prior versions of DBpedia. It is based on data
available from the DBpedia Downloads page, and covers the following
DBpedia dumps: DBpedia 3.7, DBpedia 3.6, DBpedia 3.5.1, DBpedia 3.5,
DBpedia 3.4, DBpedia 3.3, DBpedia 3.2, DBpedia 3.1, DBpedia 3.0,
DBpedia 3.0RC, DBpedia 2.0 The English (en) version of all Core
Datasets. No other languages are available.

>>> obj = Dbpedia().get_timegate(for_uri='http://dbpedia.org/data/Oaxaca')
>>> obj.first
"""
    timegate_template = 'http://dbpedia.mementodepot.org/timegate/document/%s'
    timemap_template = 'http://dbpedia.mementodepot.org/timemap/link/%s'

@register_as('icelandic')
class Icelandic(Memento):
    """
For information about the Icelandic Web Archive, see
http://vefsafn.is/index.php?page=english.

>>> obj = Icelandic().get_timegate(for_uri='http://www.government.is')
>>> obj.first
[('http://wayback.vefsafn.is/wayback/20011204062750/http://www.government.is/', {'datetime': 'Tue, 04 Dec 2001 06:27:50 GMT'})]
"""
    timegate_template = 'http://wayback.vefsafn.is/wayback/%s'
    timemap_template = 'http://wayback.vefsafn.is/wayback/timemap/link/%s'

@register_as('ia')
class Ia(Memento):
    """
The Internet Archive is the largest public web archive. It contains
billions of web pages that were archived from 1996 to a few months
ago, and is accessible via the Wayback Machine.

>>> obj = Ia().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
[('http://web.archive.org/web/20020911073933/http://www.w3.org/TR/webarch/', {'datetime': 'Wed, 11 Sep 2002 07:39:33 GMT'})]
"""
    timegate_template = 'http://web.archive.org/web/%s'
    timemap_template = 'http://web.archive.org/web/timemap/link/%s'

@register_as('proni')
class Proni(Memento):
    """
The PRONI Web Archive is made available by the Public Record Office of
Northern Ireland, the official archive of Northern Ireland. The PRONI
web archive aims to permanently preserve and make accessible websites
that are of historical and cultural importance to Northern Ireland.
Further information about this web archive is available via its home
page.

>>> obj = Proni().get_timegate(for_uri='http://www.dojni.gov.uk')
>>> obj.first
[('http://webarchive.proni.gov.uk/20100805094632/http://www.dojni.gov.uk', {'datetime': 'Thu, 05 Aug 2010 09:46:32 GMT'})]
"""
    timegate_template = 'http://webarchive.proni.gov.uk/timegate/%s'
    timemap_template = 'http://webarchive.proni.gov.uk/timemap/%s'

@register_as('stanfordwebarchive')
class Stanfordwebarchive(Memento):
    """
The Stanford Web Archive is provided by Stanford University Libraries.
The archive will ultimately include historical web content reflecting
a range of institutional use cases. You can learn more about web
archiving at Stanford University on their micro-site.

>>> obj = Stanfordwebarchive().get_timegate(for_uri='http://www.slac.stanford.edu/')
>>> obj.first
[('https://swap.stanford.edu/19951222000000/http://www.slac.stanford.edu/', {'datetime': 'Fri, 22 Dec 1995 00:00:00 GMT'})]
"""
    timegate_template = 'https://swap.stanford.edu/%s'
    timemap_template = 'https://swap.stanford.edu/timemap/link/%s'

@register_as('uknationalarchives')
class Uknationalarchives(Memento):
    """
The UK Government Web Archive is made available by the UK National
Archives and consists of archived versions of UK government
information published on the web. Further information about this web
archive is available via its home page.

>>> obj = Uknationalarchives().get_timegate(for_uri='http://www.jisc.ac.uk/')
>>> obj.first
[('http://webarchive.nationalarchives.gov.uk/20040105023747/http://www.jisc.ac.uk/', {'datetime': 'Mon, 05 Jan 2004 02:37:47 GMT'})]
"""
    timegate_template = 'http://webarchive.nationalarchives.gov.uk/timegate/%s'
    timemap_template = 'http://webarchive.nationalarchives.gov.uk/timemap/%s'

@register_as('ukparliament')
class Ukparliament(Memento):
    """
The UK Parliament's Web Archive provides access to previous versions
of the UK's parliamentary website and related websites. Further
information about this web archive is available via its home page.

>>> obj = Ukparliament().get_timegate(for_uri='http://mpsallowances.parliament.uk')
>>> obj.first
[('http://webarchive.parliament.uk/20090618153959/http://mpsallowances.parliament.uk', {'datetime': 'Thu, 18 Jun 2009 15:39:59 GMT'})]
"""
    timegate_template = 'http://webarchive.parliament.uk/timegate/%s'
    timemap_template = 'http://webarchive.parliament.uk/timemap/%s'

@register_as('blarchive')
class Blarchive(Memento):
    """
The UK Web Archive is made available by the British Library and
contains websites that publish research, that reflect the diversity of
lives, interests and activities throughout the UK, and demonstrate web
innovation. This includes "grey literature" sites: those that carry
briefings, reports, policy statements, and other ephemeral but
significant forms of information. Further information about this web
archive is available via its home page.

>>> obj = Blarchive().get_timegate(for_uri='http://www.jisc.ac.uk/')
>>> obj.first
[('http://www.webarchive.org.uk:80/wayback/archive/20080211163828/http://www.jisc.ac.uk/', {'datetime': 'Mon, 11 Feb 2008 16:38:28 GMT'})]
"""
    timegate_template = 'http://www.webarchive.org.uk/wayback/archive/%s'
    timemap_template = 'http://www.webarchive.org.uk/wayback/archive/timemap/link/%s'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

