pyimpfuzzy
==========

Python module for comparing the impfuzzy

More details are described in the following documents:
 https://www.jpcert.or.jp/magazine/acreport-impfuzzy.html (Japanese)
 http://blog.jpcert.or.jp/2016/05/classifying-mal-a988.html (English)

Requirements
------------

pyimpfuzzy requires the following modules:

-  pefile 1.2.10-139 or later
-  ssdeep http://ssdeep.sourceforge.net

Installation
------------

::

    $ sudo pip install pyimpfuzzy

Usage
-----

-  get\_impfuzzy - return the impfuzzy hash for a given file
-  get\_impfuzzy\_data - return the impfuzzy hash for a buffer
-  hash\_compare - return the match between 2 hashes

Example Usage
~~~~~~~~~~~~~

::

    import pyimpfuzzy
    import sys

    hash1 = pyimpfuzzy.get_impfuzzy(sys.argv[1])
    hash2 = pyimpfuzzy.get_impfuzzy(sys.argv[2])
    print "ImpFuzzy1: %s" % hash1
    print "ImpFuzzy2: %s" % hash2
    print "Compare: %i" % pyimpfuzzy.hash_compare(hash1, hash2)

