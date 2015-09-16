#!/usr/bin/env python
import os
import subprocess
import zipfile
import tarfile
import urllib
import shutil

# download current web2py release
print('Downloading Web2py Source')
web2pyfile = urllib.URLopener()
web2pyfile.retrieve("http://www.web2py.com/examples/static/web2py_src.zip", "web2py_src.zip")
print('Completed')

# extract
with zipfile.ZipFile('web2py_src.zip', "r") as z:
    z.extractall()

# get version and rename folder
with open('web2py/VERSION','r') as f:
    line=f.read()
version = line.split(' ')[1].split('-')[0]

# rename folder
os.rename('web2py','web2py_{}.orig'.format(version))

output_filename = 'web2py_{0}.orig.tar.gz'.format(version)
source_dir = 'web2py_{0}.orig/'.format(version)

# create orig tarfile
with tarfile.open(output_filename, "w:gz") as tar:
    tar.add(source_dir)

# copy debian files
shutil.copytree('debian','{}/debian'.format(source_dir))

# change directory and create package
print('Creating debian package')
os.chdir(source_dir)
subprocess.call('dpkg-buildpackage',shell=True)

# Cleanup
os.unlink(output_filename)
os.unlink('web2py_src.zip')
print('Finished')
