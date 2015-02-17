# PyMemento
Mememto (RFC 7089) Client for Python

RFC 7089 specifies a way to access archived versions of web resources, such as those provided by archive.org (the Wayback 
Machine).  This is done via timegates, which provide access to various versions of a resource, and timemaps, which provide 
lists of versions of a resource.  PyMemento encapsulates these concepts and provides a user extensible registry of
such archives.
