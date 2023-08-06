STI_info_scrape
===============================

version number: 0.1.0
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
    w.chromedriver_location = r"D:\download (software)\chromedriver.exe"
    w.store_location = r'C:\data\temp\STImaindata.csv'
    kk = w.get_SGX_main_data()
    print kk.head()
    w.save_to_file()

    sys.exit()