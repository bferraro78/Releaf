#!/bin/sh

# Install Libraries
cd pyexcel
sudo python setup.py install
cd ..
cd pyexcel-xlsx
sudo python setup.py install
cd ..
cd openpyxl-openpyxl-0f8537998f95
sudo python setup.py install
cd ..
cd feedparser
sudo python setup.py install
cd ..
