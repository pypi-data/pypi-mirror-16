.. fulmar documentation master file, created by
   sphinx-quickstart on Tue Aug  2 14:19:45 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

fulmar
=======

Fulmar is a distributed crawler system. By using non-blocking network I/O,
Fulmar can handle hundreds of open connections at the same time. You can
extractthe data you need from websites. In a fast, simple, yet extensible way.


Quick links
^^^^^^^^^^^

* `Source (github) <https://github.com/tylderen/fulmar>`_
* `Wiki <https://github.com/tylderen/fulmar/wiki/Links>`_

Code example
^^^^^^^^^^^^

Here is a simple example::

   import logging

   from fulmar.base_spider import BaseSpider

   logger = logging.getLogger(__name__)

   class Handler(BaseSpider):
      def on_start(self):
         self.crawl('http://www.baidu.com/', callback=self.detail_page)

      def detail_page(self, response):
         try:
            page_lxml = response.page_lxml
         except Exception as e:
            logger.error(str(e))

         return {
            "url": response.url,
            "title": page_lxml.xpath('//title/text()')[0]}



You can save above code in a new file called `baidu_spider.py` and run in console::

                  fulmar start_project baidu_spider.py

If you have installed `redis`, you will get::

                  Successfully start the project, project name: "baidu_spider".

Finally, start Fulmar::

                  fulmar all

Installation
------------

**Automatic installation**::

    pip install fulmar

Fulmar is listed in `PyPI <http://pypi.python.org/pypi/fulmar>`_ and
can be installed with ``pip`` or ``easy_install``.  Note that the
source distribution includes demo applications that are not present
when Tornado is installed in this way, so you may wish to download a
copy of the source tarball as well.

**Manual installation**: Download tarball, then:

.. parsed-literal::

    tar xvzf fulmar-|version|.tar.gz
    cd fulmar-|version|
    python setup.py build
    sudo python setup.py install

The Fulmar source code is `hosted on GitHub
<https://github.com/tylderen/fulmar>`_.

**Prerequisites**: Fulmar runs on Python 2.7, and 3.3+
For Python 2, version 2.7.9 or newer is *strongly*
recommended for the improved SSL support.

Documentation
-------------

This documentation is also available in `PDF and Epub formats
<https://readthedocs.org/projects/fulmar/downloads/>`_.

.. toctree::
   :maxdepth: 2

   quick



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

