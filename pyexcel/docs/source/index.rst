`pyexcel` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel.git
:Issues: http://github.com/pyexcel/pyexcel/issues
:License: New BSD License
:Development: |release|
:Released: |version|
:Generated: |today|

Introduction
-------------

**pyexcel** provides **one** application programming interface to read,
manipulate and write data in different excel formats. This library makes
information processing involving excel files an enjoyable task. The data in
excel files can be turned into :ref:`array or dict<a-list-of-data-structures>`
with least code, vice versa. This library focuses on data
processing using excel files as storage media hence fonts, colors and charts
were not and will not be considered.

The idea originated from the common usability problem when developing an excel file
driven web applications for non-technical office workers: such as office assistant,
human resource administrator. The fact is that not all people know the
difference among various excel formats: csv, xls, xlsx. Instead of training those people
about file formats, this library helps web developers to handle most of the excel file
formats by providing a common programming interface. To add a specific excel file format
to you application, all you need is to install an extra pyexcel plugin. No code change
to your application. Looking at the community, this library and its associated ones try
to become a small and easy to install alternative to Pandas.


Installation
-------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel.git
    $ cd pyexcel
    $ python setup.py install

For individual excel file formats, please install them as you wish:

.. _file-format-list:
.. _a-map-of-plugins-and-file-formats:

.. table:: A list of file formats supported by external plugins

   ======================== ======================= =============== ==================
   Package name              Supported file formats  Dependencies   Python versions
   ======================== ======================= =============== ==================
   `pyexcel-io`_            csv, csvz [#f1]_, tsv,                  2.6, 2.7, 3.3,
                            tsvz [#f2]_                             3.4, 3.5, 3.6
                                                                    pypy
   `pyexcel-xls`_           xls, xlsx(read only),   `xlrd`_,        same as above
                            xlsm(read only)         `xlwt`_
   `pyexcel-xlsx`_          xlsx                    `openpyxl`_     same as above
   `pyexcel-xlsxw`_         xlsx(write only)        `XlsxWriter`_   same as above
   `pyexcel-ods3`_          ods                     `ezodf`_,       2.6, 2.7, 3.3, 3.4
                                                    lxml            3.5, 3.6
   `pyexcel-ods`_           ods                     `odfpy`_        same as above
   `pyexcel-odsr`_          ods(read only)          lxml            same as above
   `pyexcel-text`_          (write only)json, rst,  `tabulate`_     2.6, 2.7, 3.3, 3.4
                            mediawiki, html,                        3.5, pypy, pypy3
                            latex, grid, pipe,
                            orgtbl, plain simple
   `pyexcel-handsontable`_  handsontable in html    `handsontable`_ same as above
   `pyexcel-pygal`_         svg chart               `pygal`_        same as above [#f3]_
   ======================== ======================= =============== ==================

.. _pyexcel-io: https://github.com/pyexcel/pyexcel-io
.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-odsr: https://github.com/pyexcel/pyexcel-odsr
.. _pyexcel-xlsxw: https://github.com/pyexcel/pyexcel-xlsxw

.. _xlrd: https://github.com/python-excel/xlrd
.. _xlwt: https://github.com/python-excel/xlwt
.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl
.. _XlsxWriter: https://github.com/jmcnamara/XlsxWriter
.. _ezodf: https://github.com/T0ha/ezodf
.. _odfpy: https://github.com/eea/odfpy

.. _pyexcel-text: https://github.com/pyexcel/pyexcel-text
.. _tabulate: https://bitbucket.org/astanin/python-tabulate
.. _pyexcel-handsontable: https://github.com/pyexcel/pyexcel-handsontable
.. _handsontable: https://cdnjs.com/libraries/handsontable
.. _pyexcel-pygal: https://github.com/pyexcel/pyexcel-chart
.. _pygal: https://github.com/Kozea/pygal
.. _pyexcel-matplotlib: https://github.com/pyexcel/pyexcel-matplotlib
.. _matplotlib: https://matplotlib.org

.. [#f3] coming soon

In order to manage the list of plugins installed, you need to use pip to add or remove
a plugin. When you use virtualenv, you can have different plugins per virtual
environment. In the situation where you have multiple plugins that does the same thing
in your environment, you need to tell pyexcel which plugin to use per function call.
For example, pyexcel-ods and pyexcel-odsr, and you want to get_array to use pyexcel-odsr.
You need to append get_array(..., library='pyexcel-odsr').

.. rubric:: Footnotes

.. [#f1] zipped csv file
.. [#f2] zipped tsv file

For compatibility tables of pyexcel-io plugins, please click `here <http://pyexcel-io.readthedocs.io/en/latest/#id5>`_

.. table:: Plugin compatibility table

    ======= ========== ============= ==================== =============
    pyexcel pyexcel-io pyexcel-text  pyexcel-handsontable pyexcel-pygal
    ======= ========== ============= ==================== =============
    0.5.0   0.4.0      0.2.6         0.0.1			      0.0.1(coming)
    0.4.0+  0.3.0+     0.2.5
    ======= ========== ============= ==================== =============


Usage
------

.. testcode::
   :hide:

   >>> import pyexcel
   >>> # make sure you had pyexcel-xls pip-installed
   >>> a_list_of_dictionaries = [
   ...     {
   ...         "Name": 'Adam',
   ...         "Age": 28
   ...     },
   ...     {
   ...         "Name": 'Beatrice',
   ...         "Age": 29
   ...     },
   ...     {
   ...         "Name": 'Ceri',
   ...         "Age": 30
   ...     },
   ...     {
   ...         "Name": 'Dean',
   ...         "Age": 26
   ...     }
   ... ]
   >>> pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")

Suppose you want to process the following excel data :

.. pyexcel-table::

   ---pyexcel:example table---
   Name,Age
   Adam,28
   Beatrice,29
   Ceri,30
   Dean,26


Here are the example usages:

.. code-block:: python

   >>> import pyexcel as pe
   >>> records = pe.iget_records(file_name="your_file.xls")
   >>> for record in records:
   ...     print("%s is aged at %d" % (record['Name'], record['Age']))
   Adam is aged at 28
   Beatrice is aged at 29
   Ceri is aged at 30
   Dean is aged at 26
   >>> pe.free_resources()

.. testcode::
   :hide:

   >>> import os
   >>> os.unlink("your_file.xls")

Design
--------------------

.. toctree::

   design
   capability
   architecture

Tutorial
----------
.. toctree::

   tutorial_file
   tutorial06
   tutorial_data_conversion
   attributes.rst
   bigdata
   tutorial
   tutorial05
   tutorial02
   tutorial03
   tutorial04

Cook book
----------

.. toctree::

   cookbook
   sources

Real world cases
-------------------

.. toctree::

   answers
   showcases/db_injection

API documentation
------------------

.. toctree::
   :maxdepth: 2

   api
   iapi


Developer's guide
------------------

.. toctree::

   guide
   logging
   pyinstaller

Change log
-------------------

.. toctree::
   :maxdepth: 2

   migration_guide
   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
