#!/usr/bin/env python

from distutils.core import setup

setup(name = "chm2pdf",
    version = "0.0.1",
    description = "A script to convert CHM files into PDF",
    author = "Massimo Sandal",
    author_email = "devicerandom@gmail.com",
    url = "http://code.google.com/p/chm2pdf/",
    scripts = ["chm2pdf"],
    long_description = "A script to convert CHM files into PDF. Requires chmlib, pychm, htmldoc, pdftk."
    )
    

    