STI_info_scrape
===============================

version number: 0.0.1
author: Tan Kok Hua

Overview
--------

Python module to scrape main STI data from SGX main page.

Installation / Usage
--------------------

To install use pip:

    $ pip install STI_info_scrape


Or clone the repo:

    $ git clone https://github.com/spidezad/STI_info_scrape.git
    $ python setup.py install
    
Contributing
------------
All ideas/contributions are welcome.

Example
-------
    w = STIMainData()
    kk = w.SGX_main_data
    print kk.head()