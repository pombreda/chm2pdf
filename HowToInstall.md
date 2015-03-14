# From your package manager #
As of Ubuntu 8.04, chm2pdf is in the universe repository. You can therefore install chm2pdf from your package manager. The same holds for Debian testing.

It also seems that it is included in FreeBSD ports. An unofficial Gentoo ebuild is available (check bugs.gentoo.org)

# From source #
## Dependencies ##
If you want to install chm2pdf from source, you need those packages installed and working:
Gentoo:
  * chmlib
  * pychm
  * htmldoc

Ubuntu/Kubuntu/Debian:
Anyway, you should need:
  * libchm
  * libchm-bin
  * libchm-dev
  * python-chm
  * html-doc
  * htmldoc-common


Analogous packages should exist on most other Linux/BSD distributions. It seems that

Users have reported success on Mac OS X, however currently this is unsupported.

On Fedora, it has been reported that the chmlib package is missing some essential files. You need to look for chmlib-bin or to compile chmlib by hand.

If you install chmlib from source, do not forget to use the --enable-examples on chmLib, otherwise this script will throw a bunch of exceptions, and will fail.

If you use Mac OS X, and you use darwin ports (port on the cmdline), be aware that the chmlib will NOT be built with this option. You can, however, separately download chmlib and build it yourself with this option, install it, and then re-run the script.


## Install ##
  * Download the archive
  * Unzip it (tar -xzvf chm2pdf-x.x.x.tar.gz)
  * Enter the directory
  * Become root
  * Type "python setup.py install"
  * Enjoy

**PLEASE AVOID POLLUTING THIS PAGE WITH COMMENTS**
If you have installation problems, use the Google group.