xmlwitch offers Pythonic XML generation through context generators in a 
minimalist implementation with less than 100 lines of code. BSD-licensed.

Usage
`````

::

    import xmlwitch
    xml = xmlwitch.Builder(version='1.0', encoding='utf-8')
    with xml.feed(xmlns='http://www.w3.org/2005/Atom'):
        xml.title('Example Feed')
        xml.updated('2003-12-13T18:30:02Z')
        with xml.author:
            xml.name('John Doe')
        xml.id('urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6')
        with xml.entry:
            xml.title('Atom-Powered Robots Run Amok')
            xml.id('urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a')
            xml.updated('2003-12-13T18:30:02Z')
            xml.summary('Some text.')
    print(xml)

Setup
`````

::

    $ pip install xmlwitch # or
    $ easy_install xmlwitch # or
    $ cd xmlwitch-0.3; python setup.py install

Links
`````

* `Development repository <http://github.com/galvez/xmlwitch/>`_
* `Author's website <http://hire.jonasgalvez.com.br/>`_



