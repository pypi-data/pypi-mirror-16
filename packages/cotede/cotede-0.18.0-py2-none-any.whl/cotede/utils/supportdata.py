# -*- coding: utf-8 -*-

"""

"""

import os
import sys
import shutil
import hashlib
from tempfile import NamedTemporaryFile

if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from urllib.parse import urlparse
else:
    from urllib2 import urlopen
    from urlparse import urlparse


from cotede.utils import cotede_dir

def download_file(url, md5hash, d):
    """ Download data file from web

        IMPROVE it to automatically extract gz files
    """
    download_block_size = 2 ** 16

    assert type(md5hash) is str

    if not os.path.exists(d):
        os.makedirs(d)

    hash = hashlib.md5()

    fname = os.path.join(d, os.path.basename(urlparse(url).path))
    if os.path.isfile(fname):
        h = hashlib.md5(open(fname, 'rb').read()).hexdigest()
        if h == md5hash:
            print("Was previously downloaded: %s" % fname)
            return
        else:
            assert False, "%s already exist but doesn't match the hash: %s" % \
                    (fname, md5hash)

    remote = urlopen(url)

    with NamedTemporaryFile(delete=False) as f:
        try:
            bytes_read = 0
            block = remote.read(download_block_size)
            while block:
                f.write(block)
                hash.update(block)
                bytes_read += len(block)
                block = remote.read(download_block_size)
        except:
            if os.path.exists(f.name):
                os.remove(f.name)
                raise

    h = hash.hexdigest()
    if h != md5hash:
        os.remove(f.name)
        print("Downloaded file doesn't match. %s" % h)
        assert False, "Downloaded file (%s) doesn't match with expected hash (%s)" % \
                (fname, md5hash)

    shutil.move(f.name, fname)
    print("Downloaded: %s" % fname)

def download_supportdata():
    print("This can take several minutes, depending on the network bandwidth. Sorry, in the future I'll include a progress bar.")
    d = os.path.join(cotede_dir(), 'data')
    download_file('http://data.nodc.noaa.gov/thredds/fileServer/woa/WOA09/NetCDFdata/temperature_seasonal_5deg.nc',
            '271f66e8dea4dfef7db99f5f411af330', d)
    download_file('http://data.nodc.noaa.gov/thredds/fileServer/woa/WOA09/NetCDFdata/salinity_seasonal_5deg.nc',
            '1d2d1982338c688bdd18069d030ec05f', d)

def download_testdata(filename):

    d = os.path.join(cotede_dir(), 'testdata')
    if not os.path.exists(d):
        os.makedirs(d)

    test_files = {
            'dPIRX010.cnv': {
                "url": "https://dl.dropboxusercontent.com/u/26063625/seabird/dPIRX010.cnv",
                "md5": "8691409accb534c83c8bd412afbdd285"},
            'dPIRX003.cnv': {
                "url": "https://dl.dropboxusercontent.com/u/26063625/seabird/dPIRX003.cnv",
                "md5": "4b941b902a3aea7d99e1cf4c78c51877"},
            'PIRA001.cnv': {
                "url": "https://dl.dropboxusercontent.com/u/26063625/seabird/PIRA001.cnv",
                "md5": "5ded777144300b63c8775b1d7f033f92"},
            'TSG_PIR_001.cnv': {
                "url": "https://dl.dropboxusercontent.com/u/26063625/seabird/TSG_PIR_001.cnv",
                "md5": "2950ccb9f77e0802557b011c63d2e39b"},
            '20150127_prof.nc': {
                "url": "https://dl.dropboxusercontent.com/u/26063625/argo/20150127_prof.nc",
                "md5": "cedc63d54a556e4782dbacfb2d6cfb30"},
            }

    assert filename in test_files.keys(), \
            "%s is not a valid test file" % filename

    download_file(test_files[filename]["url"], test_files[filename]["md5"],
            d)
    datafile = os.path.join(d, filename)

    return datafile
