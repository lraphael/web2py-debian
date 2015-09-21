# web2py-debian
This is a helper script to download and create a web2py debian package with the latest web2py version.

## Install required packages
```sh
apt-get install build-essential dpkg-dev git debhelper dh-python libjs-jquery python-feedparser
```

## Checkout and create package
```sh
git clone https://github.com/lraphael/web2py-debian.git
cd web2py-debian
python download-build.py
```
