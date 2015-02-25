## Automatically generated code.

"""
doc string
"""

from memento import Memento, register_as


@register_as('archivetoday')
class Archivetoday(Memento):
    """
archive.today is "your personal Wayback Machine". For information, 
    see http://archive.today.
    
>>> obj = Archivetoday().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://archive.today/timegate/%s'
    timemap_template = u'http://archive.today/timemap/%s'

@register_as('archiveit')
class Archiveit(Memento):
    """
Archive-It is a subscription-based web, on-demand archive affiliated with the Internet Archive. Information about 
    its collection is available from its home page. 
    
>>> obj = Archiveit().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://wayback.archive-it.org/all/%s'
    timemap_template = u'http://wayback.archive-it.org/all/timemap/link/%s'

@register_as('dbpedia')
class Dbpedia(Memento):
    """
This archive contains prior versions of DBpedia. It is 
    based on data available from the DBpedia Downloads page, and covers the following DBpedia dumps:
      DBpedia 3.7, DBpedia 3.6, DBpedia 3.5.1, DBpedia 3.5, DBpedia 3.4, DBpedia 3.3, DBpedia 3.2, DBpedia 3.1, DBpedia 3.0, DBpedia 3.0RC, DBpedia 2.0
         The English (en) version of all Core Datasets. No other languages are available.
         
>>> obj = Dbpedia().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://dbpedia.mementodepot.org/timegate/document/%s'
    timemap_template = u'http://dbpedia.mementodepot.org/timemap/link/%s'

@register_as('icelandic')
class Icelandic(Memento):
    """
For information about the Icelandic Web Archive, see http://vefsafn.is/index.php?page=english.
    
>>> obj = Icelandic().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://wayback.vefsafn.is/wayback/%s'
    timemap_template = u'http://wayback.vefsafn.is/wayback/timemap/link/%s'

@register_as('ia')
class Ia(Memento):
    """
The Internet Archive is the largest public web archive. It contains billions of web pages that were archived 
    from 1996 to a few months ago, and is accessible via the Wayback Machine. 
    
>>> obj = Ia().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://web.archive.org/web/%s'
    timemap_template = u'http://web.archive.org/web/timemap/link/%s'

@register_as('proni')
class Proni(Memento):
    """
The PRONI Web Archive is made available by the Public Record Office of Northern Ireland, 
    the official archive of Northern Ireland. 
    The PRONI web archive aims to permanently preserve and make accessible websites that are of historical and cultural importance to Northern Ireland.
    Further information about this web archive is available via its home page. 
    
>>> obj = Proni().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://webarchive.proni.gov.uk/timegate/%s'
    timemap_template = u'http://webarchive.proni.gov.uk/timemap/%s'

@register_as('stanfordwebarchive')
class Stanfordwebarchive(Memento):
    """
The Stanford Web Archive is provided by Stanford University Libraries. 
    The archive will ultimately include historical web content reflecting 
    a range of institutional use cases. 
    You can learn more about web archiving at Stanford University on their micro-site.
    
>>> obj = Stanfordwebarchive().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'https://swap.stanford.edu/%s'
    timemap_template = u'https://swap.stanford.edu/timemap/link/%s'

@register_as('uknationalarchives')
class Uknationalarchives(Memento):
    """
The UK Government Web Archive is made available by the UK National Archivesand consists of 
    archived versions of UK government information published on the web. 
    Further information about this web archive is available via its home page. 
    
>>> obj = Uknationalarchives().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://webarchive.nationalarchives.gov.uk/timegate/%s'
    timemap_template = u'http://webarchive.nationalarchives.gov.uk/timemap/%s'

@register_as('ukparliament')
class Ukparliament(Memento):
    """
The UK Parliament's Web Archive 
    provides access to previous versions of the UK's parliamentary website and related websites. 
    Further information about this web archive is available via its home page. 
    
>>> obj = Ukparliament().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://webarchive.parliament.uk/timegate/%s'
    timemap_template = u'http://webarchive.parliament.uk/timemap/%s'

@register_as('blarchive')
class Blarchive(Memento):
    """
The UK Web Archive is made available by the British Libraryand contains websites that publish research, that reflect the diversity of lives, 
    interests and activities throughout the UK, and demonstrate web innovation. This includes "grey literature" sites: 
    those that carry briefings, reports, policy statements, and other ephemeral but significant forms of information.
    Further information about this web archive is available via its home page. 
    
>>> obj = Blarchive().get_timegate(for_uri='http://www.w3.org/TR/webarch/')
>>> obj.first
"""
    timegate_template = u'http://www.webarchive.org.uk/wayback/archive/%s'
    timemap_template = u'http://www.webarchive.org.uk/wayback/archive/timemap/link/%s'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

