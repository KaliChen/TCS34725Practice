# TCS34725Practice
[https://github.com/adafruit/Adafruit_Python_TCS34725](https://github.com/adafruit/Adafruit_Python_TCS34725)

[https://learn.adafruit.com/adafruit-color-sensors/python-circuitpython](https://learn.adafruit.com/adafruit-color-sensors/python-circuitpython)

# Layout
![https://github.com/KaliChen/TCS34725Practice/blob/main/picture/tcs34725.png](https://github.com/KaliChen/TCS34725Practice/blob/main/picture/tcs34725.png)

# Execute
```
python3 TCS34725.py 
```
# UI
![https://github.com/KaliChen/TCS34725Practice/blob/main/picture/ui.JPG](https://github.com/KaliChen/TCS34725Practice/blob/main/picture/ui.JPG)

# Demo
[![Yes](https://img.youtube.com/vi/pMt5h8mP-Rw/0.jpg)](https://www.youtube.com/watch?v=pMt5h8mP-Rw)

[![Yes](https://img.youtube.com/vi/BBwuX95dqZ4/0.jpg)](https://www.youtube.com/watch?v=BBwuX95dqZ4)


1. However, before we install the I2C tools, we need first to update our device.

To update the package list then upgrade the packages, all we need to do is run the command below.
```
sudo apt update
sudo apt full-upgrade
```
2. Once your Raspberry Pi has finished updating, we can install the I2C tools and the Python SMBus package.

To install these two packages, run the following command.
```
sudo apt install -y i2c-tools python3-smbus
```
The i2c-tools package allows us to interact with the I2C protocol on our Raspberry Pi. Using this, we will be able to detect our I2C connections.

The python3-smbus package will allow us to interact with I2C devices from our Raspberry Pi by using Python.

[https://pimylifeup.com/raspberry-pi-i2c/](https://pimylifeup.com/raspberry-pi-i2c/)

```
sudo apt-get install libatlas-base-dev
```

# Install requirements
```
sudo pip3 install adafruit-tcs34725
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting adafruit-tcs34725
  Downloading https://www.piwheels.org/simple/adafruit-tcs34725/Adafruit_TCS34725-1.0.3-py3-none-any.whl
Collecting Adafruit-GPIO>=0.6.5 (from adafruit-tcs34725)
  Downloading https://www.piwheels.org/simple/adafruit-gpio/Adafruit_GPIO-1.0.3-py3-none-any.whl
Requirement already satisfied: spidev in /usr/lib/python3/dist-packages (from Adafruit-GPIO>=0.6.5->adafruit-tcs34725) (3.4)
Collecting adafruit-pureio (from Adafruit-GPIO>=0.6.5->adafruit-tcs34725)
  Downloading https://www.piwheels.org/simple/adafruit-pureio/Adafruit_PureIO-1.1.8-py3-none-any.whl
Installing collected packages: adafruit-pureio, Adafruit-GPIO, adafruit-tcs34725
Successfully installed Adafruit-GPIO-1.0.3 adafruit-pureio-1.1.8 adafruit-tcs34725-1.0.3
```
```
sudo pip3 install adafruit-circuitpython-tcs34725
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting adafruit-circuitpython-tcs34725
  Downloading https://www.piwheels.org/simple/adafruit-circuitpython-tcs34725/adafruit_circuitpython_tcs34725-3.3.4-py3-none-any.whl
Collecting Adafruit-Blinka (from adafruit-circuitpython-tcs34725)
  Downloading https://www.piwheels.org/simple/adafruit-blinka/Adafruit_Blinka-6.0.1-py3-none-any.whl (146kB)
    100% |████████████████████████████████| 153kB 290kB/s 
Collecting adafruit-circuitpython-busdevice (from adafruit-circuitpython-tcs34725)
  Downloading https://www.piwheels.org/simple/adafruit-circuitpython-busdevice/adafruit_circuitpython_busdevice-5.0.4-py3-none-any.whl
Collecting pyftdi>=0.40.0 (from Adafruit-Blinka->adafruit-circuitpython-tcs34725)
  Downloading https://files.pythonhosted.org/packages/f3/95/8f6fe08d1f361c16f8ce384f85ea3b86739053c285b5db90dcc3c9d101d4/pyftdi-0.52.9-py3-none-any.whl (139kB)
    100% |████████████████████████████████| 143kB 747kB/s 
Requirement already satisfied: Adafruit-PureIO>=1.1.7 in /usr/local/lib/python3.7/dist-packages (from Adafruit-Blinka->adafruit-circuitpython-tcs34725) (1.1.8)
Collecting Adafruit-PlatformDetect>=2.18.1 (from Adafruit-Blinka->adafruit-circuitpython-tcs34725)
  Downloading https://www.piwheels.org/simple/adafruit-platformdetect/Adafruit_PlatformDetect-3.0.0-py3-none-any.whl
Requirement already satisfied: pyserial>=3.0 in /usr/lib/python3/dist-packages (from pyftdi>=0.40.0->Adafruit-Blinka->adafruit-circuitpython-tcs34725) (3.4)
Collecting pyusb>=1.0.0 (from pyftdi>=0.40.0->Adafruit-Blinka->adafruit-circuitpython-tcs34725)
  Downloading https://files.pythonhosted.org/packages/b5/28/b857ac783257f142932b23379d761a3d9becf6deecf5d14075ec19bdb890/pyusb-1.1.1-py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 1.8MB/s 
Installing collected packages: pyusb, pyftdi, Adafruit-PlatformDetect, Adafruit-Blinka, adafruit-circuitpython-busdevice, adafruit-circuitpython-tcs34725
Successfully installed Adafruit-Blinka-6.0.1 Adafruit-PlatformDetect-3.0.0 adafruit-circuitpython-busdevice-5.0.4 adafruit-circuitpython-tcs34725-3.3.4 pyftdi-0.52.9 pyusb-1.1.1
```
```
pip3 install smbus2
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting smbus2
  Downloading https://files.pythonhosted.org/packages/c8/bf/62ef029fb7077fc87c3539f7365859bccc6cedb2bb20796b737b788c8d09/smbus2-0.4.1-py2.py3-none-any.whl
Installing collected packages: smbus2
Successfully installed smbus2-0.4.1
```
```
sudo apt-get install libi2c-dev
```
```
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  alsa-base cython freetype2-doc gdal-data geoclue-2.0 gir1.2-gtk-2.0
  gir1.2-harfbuzz-0.0 gir1.2-rsvg-2.0 gstreamer0.10-alsa
  gstreamer0.10-plugins-base hdf5-helpers iio-sensor-proxy libaec-dev libaec0
  libarmadillo-dev libarmadillo9 libarpack2 libarpack2-dev libatk1.0-dev
  libblas-dev libboost-dev libcaf-openmpi-3 libcairo-script-interpreter2
  libcharls-dev libcharls2 libcoarrays-openmpi-dev libdap-dev libdap25
  libdapclient6v5 libdapserver7v5 libepsilon-dev libepsilon1
  libevent-core-2.1-6 libevent-pthreads-2.1-6 libfreexl-dev libfreexl1
  libfyba-dev libfyba0 libgdal20 libgeos-3.7.1 libgeos-c1v5 libgeos-dev
  libgeotiff-dev libgeotiff2 libgif-dev libgl2ps-dev libgl2ps1.4
  libgraphite2-dev libgstreamer-plugins-base0.10-0 libgstreamer0.10-0
  libharfbuzz-dev libharfbuzz-gobject0 libhdf4-0-alt libhdf4-alt-dev
  libhdf5-103 libhdf5-cpp-103 libhdf5-dev libhdf5-mpi-dev libhdf5-openmpi-103
  libhdf5-openmpi-dev libhwloc-dev libhwloc-plugins libhwloc5 libibverbs-dev
  libjson-c-dev libjsoncpp-dev libkml-dev libkmlbase1 libkmlconvenience1
  libkmldom1 libkmlengine1 libkmlregionator1 libkmlxsd1 liblapack-dev libllvm8
  liblzo2-2 libmbim-glib4 libmbim-proxy libmicrodns0 libminizip-dev
  libminizip1 libmm-glib0 libnetcdf-c++4 libnetcdf-cxx-legacy-dev
  libnetcdf-dev libnetcdf13 libnl-3-dev libnl-route-3-dev libogdi3.2
  libogdi3.2-dev libopenmpi-dev libopenmpi3 libpixman-1-dev libpmix2
  libpng-tools libpoppler-dev libpoppler-private-dev libproj-dev libproj13
  libqhull-dev libqhull-r7 libqhull7 libqmi-glib5 libqmi-proxy
  libqt5positioning5 libqt5qml5 libqt5quick5 libqt5sensors5 libqt5webchannel5
  libqt5webkit5 libspatialite-dev libspatialite7 libsuperlu-dev libsuperlu5
  libsz2 liburiparser-dev liburiparser1 libvtk6-java libvtk6-jni libvtk6.3
  libvtk6.3-qt libxcomposite-dev libxdamage-dev libxerces-c-dev libxerces-c3.2
  libxfce4util-bin libxfce4util-common libxfce4util7 libxfconf-0-2 libzstd-dev
  lxplug-volume modemmanager mpi-default-bin mpi-default-dev openmpi-bin
  openmpi-common pango1.0-tools pimixer proj-bin proj-data python-attr
  python-autobahn python-automat python-cbor python-constantly python-future
  python-hyperlink python-incremental python-lz4 python-mpi4py python-nacl
  python-png python-pyasn1 python-pyasn1-modules python-pyqrcode
  python-service-identity python-snappy python-trie python-trollius
  python-twisted python-twisted-bin python-twisted-core python-txaio
  python-u-msgpack python-ubjson python-vtk6 python-wsaccel
  python-zope.interface rpi-eeprom-images tcl tcl-dev tcl-vtk6 tcl8.6-dev tk
  vtk6 x11proto-composite-dev x11proto-damage-dev xfconf
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  libi2c-dev
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 11.9 kB of archives.
After this operation, 31.7 kB of additional disk space will be used.
Get:1 http://mirror.ossplanet.net/raspbian/raspbian buster/main armhf libi2c-dev armhf 4.1-1 [11.9 kB]
Fetched 11.9 kB in 1s (9,253 B/s)
Selecting previously unselected package libi2c-dev.
(Reading database ... 161513 files and directories currently installed.)
Preparing to unpack .../libi2c-dev_4.1-1_armhf.deb ...
Unpacking libi2c-dev (4.1-1) ...
Setting up libi2c-dev (4.1-1) ...
```

```
ImportError: cannot import name 'ImageTk' from 'PIL' (/usr/lib/python3/dist-packages/PIL/__init__.py)
```

```
sudo apt-get install python3-pil python3-pil.imagetk
```
```
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3-pil is already the newest version (5.4.1-2+deb10u2).
python3-pil set to manually installed.
The following packages were automatically installed and are no longer required:
  alsa-base cython freetype2-doc gdal-data geoclue-2.0 gir1.2-gtk-2.0
  gir1.2-harfbuzz-0.0 gir1.2-rsvg-2.0 gstreamer0.10-alsa
  gstreamer0.10-plugins-base hdf5-helpers iio-sensor-proxy libaec-dev libaec0
  libarmadillo-dev libarmadillo9 libarpack2 libarpack2-dev libatk1.0-dev
  libblas-dev libboost-dev libcaf-openmpi-3 libcairo-script-interpreter2
  libcharls-dev libcharls2 libcoarrays-openmpi-dev libdap-dev libdap25
  libdapclient6v5 libdapserver7v5 libepsilon-dev libepsilon1
  libevent-core-2.1-6 libevent-pthreads-2.1-6 libfreexl-dev libfreexl1
  libfyba-dev libfyba0 libgdal20 libgeos-3.7.1 libgeos-c1v5 libgeos-dev
  libgeotiff-dev libgeotiff2 libgif-dev libgl2ps-dev libgl2ps1.4
  libgraphite2-dev libgstreamer-plugins-base0.10-0 libgstreamer0.10-0
  libharfbuzz-dev libharfbuzz-gobject0 libhdf4-0-alt libhdf4-alt-dev
  libhdf5-103 libhdf5-cpp-103 libhdf5-dev libhdf5-mpi-dev libhdf5-openmpi-103
  libhdf5-openmpi-dev libhwloc-dev libhwloc-plugins libhwloc5 libibverbs-dev
  libjson-c-dev libjsoncpp-dev libkml-dev libkmlbase1 libkmlconvenience1
  libkmldom1 libkmlengine1 libkmlregionator1 libkmlxsd1 liblapack-dev libllvm8
  liblzo2-2 libmbim-glib4 libmbim-proxy libmicrodns0 libminizip-dev
  libminizip1 libmm-glib0 libnetcdf-c++4 libnetcdf-cxx-legacy-dev
  libnetcdf-dev libnetcdf13 libnl-3-dev libnl-route-3-dev libogdi3.2
  libogdi3.2-dev libopenmpi-dev libopenmpi3 libpixman-1-dev libpmix2
  libpng-tools libpoppler-dev libpoppler-private-dev libproj-dev libproj13
  libqhull-dev libqhull-r7 libqhull7 libqmi-glib5 libqmi-proxy
  libqt5positioning5 libqt5qml5 libqt5quick5 libqt5sensors5 libqt5webchannel5
  libqt5webkit5 libspatialite-dev libspatialite7 libsuperlu-dev libsuperlu5
  libsz2 liburiparser-dev liburiparser1 libvtk6-java libvtk6-jni libvtk6.3
  libvtk6.3-qt libxcomposite-dev libxdamage-dev libxerces-c-dev libxerces-c3.2
  libxfce4util-bin libxfce4util-common libxfce4util7 libxfconf-0-2 libzstd-dev
  lxplug-volume modemmanager mpi-default-bin mpi-default-dev openmpi-bin
  openmpi-common pango1.0-tools pimixer proj-bin proj-data python-attr
  python-autobahn python-automat python-cbor python-constantly python-future
  python-hyperlink python-incremental python-lz4 python-mpi4py python-nacl
  python-png python-pyasn1 python-pyasn1-modules python-pyqrcode
  python-service-identity python-snappy python-trie python-trollius
  python-twisted python-twisted-bin python-twisted-core python-txaio
  python-u-msgpack python-ubjson python-vtk6 python-wsaccel
  python-zope.interface rpi-eeprom-images tcl tcl-dev tcl-vtk6 tcl8.6-dev tk
  vtk6 x11proto-composite-dev x11proto-damage-dev xfconf
Use 'sudo apt autoremove' to remove them.
Suggested packages:
  python-pil-doc python3-pil.imagetk-dbg
The following NEW packages will be installed:
  python3-pil.imagetk
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 65.0 kB of archives.
After this operation, 92.2 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.ossplanet.net/raspbian/raspbian buster/main armhf python3-pil.imagetk armhf 5.4.1-2+deb10u2 [65.0 kB]
Fetched 65.0 kB in 2s (28.3 kB/s)        
Selecting previously unselected package python3-pil.imagetk:armhf.
(Reading database ... 161522 files and directories currently installed.)
Preparing to unpack .../python3-pil.imagetk_5.4.1-2+deb10u2_armhf.deb ...
Unpacking python3-pil.imagetk:armhf (5.4.1-2+deb10u2) ...
Setting up python3-pil.imagetk:armhf (5.4.1-2+deb10u2) ...
```
```
pip3 install matplotlib
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting matplotlib
  Downloading https://www.piwheels.org/simple/matplotlib/matplotlib-3.3.4-cp37-cp37m-linux_armv7l.whl (11.5MB)
    100% |████████████████████████████████| 11.5MB 38kB/s 
Requirement already satisfied: numpy>=1.15 in /usr/lib/python3/dist-packages (from matplotlib) (1.16.2)
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Downloading https://www.piwheels.org/simple/kiwisolver/kiwisolver-1.3.1-cp37-cp37m-linux_armv7l.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 163kB/s 
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/8a/bb/488841f56197b13700afd5658fc279a2025a39e22449b7cf29864669b15d/pyparsing-2.4.7-py2.py3-none-any.whl (67kB)
    100% |████████████████████████████████| 71kB 2.7MB/s 
Collecting python-dateutil>=2.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl (227kB)
    100% |████████████████████████████████| 235kB 726kB/s 
Collecting pillow>=6.2.0 (from matplotlib)
  Downloading https://www.piwheels.org/simple/pillow/Pillow-8.1.0-cp37-cp37m-linux_armv7l.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 283kB/s 
Collecting cycler>=0.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.1->matplotlib) (1.12.0)
Installing collected packages: kiwisolver, pyparsing, python-dateutil, pillow, cycler, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.3.1 matplotlib-3.3.4 pillow-8.1.0 pyparsing-2.4.7 python-dateutil-2.8.1
```
[https://tikzplotlib.readthedocs.io/](https://tikzplotlib.readthedocs.io/)

```
pip3 install tikzplotlib
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting tikzplotlib
  Downloading https://files.pythonhosted.org/packages/e7/92/8c988a21d71cc773a63d5d25814cbdce16bf064899242d14e03d6a4f5df3/tikzplotlib-0.9.8-py3-none-any.whl (53kB)
    100% |████████████████████████████████| 61kB 666kB/s 
Requirement already satisfied: numpy in /home/pi/.local/lib/python3.7/site-packages (from tikzplotlib) (1.20.0)
Requirement already satisfied: matplotlib>=1.4.0 in /home/pi/.local/lib/python3.7/site-packages (from tikzplotlib) (3.3.4)
Requirement already satisfied: Pillow in /home/pi/.local/lib/python3.7/site-packages (from tikzplotlib) (8.1.0)
Collecting importlib-metadata; python_version < "3.8" (from tikzplotlib)
  Downloading https://files.pythonhosted.org/packages/f3/ed/da40116a204abb5c4dd1d929346d33e0d29cedb2cedd18ea98f0385dcd92/importlib_metadata-3.4.0-py3-none-any.whl
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in /home/pi/.local/lib/python3.7/site-packages (from matplotlib>=1.4.0->tikzplotlib) (2.4.7)
Requirement already satisfied: cycler>=0.10 in /home/pi/.local/lib/python3.7/site-packages (from matplotlib>=1.4.0->tikzplotlib) (0.10.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /home/pi/.local/lib/python3.7/site-packages (from matplotlib>=1.4.0->tikzplotlib) (1.3.1)
Requirement already satisfied: python-dateutil>=2.1 in /home/pi/.local/lib/python3.7/site-packages (from matplotlib>=1.4.0->tikzplotlib) (2.8.1)
Collecting zipp>=0.5 (from importlib-metadata; python_version < "3.8"->tikzplotlib)
  Downloading https://files.pythonhosted.org/packages/41/ad/6a4f1a124b325618a7fb758b885b68ff7b058eec47d9220a12ab38d90b1f/zipp-3.4.0-py3-none-any.whl
Collecting typing-extensions>=3.6.4; python_version < "3.8" (from importlib-metadata; python_version < "3.8"->tikzplotlib)
  Downloading https://files.pythonhosted.org/packages/60/7a/e881b5abb54db0e6e671ab088d079c57ce54e8a01a3ca443f561ccadb37e/typing_extensions-3.7.4.3-py3-none-any.whl
Requirement already satisfied: six in /home/pi/.local/lib/python3.7/site-packages (from cycler>=0.10->matplotlib>=1.4.0->tikzplotlib) (1.15.0)
Installing collected packages: zipp, typing-extensions, importlib-metadata, tikzplotlib
Successfully installed importlib-metadata-3.4.0 tikzplotlib-0.9.8 typing-extensions-3.7.4.3 zipp-3.4.0

```
```
pip3 install scipy
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting scipy
  Downloading https://www.piwheels.org/simple/scipy/scipy-1.6.0-cp37-cp37m-linux_armv7l.whl (61.9MB)
    100% |████████████████████████████████| 61.9MB 7.3kB/s 
Collecting numpy>=1.16.5 (from scipy)
  Downloading https://www.piwheels.org/simple/numpy/numpy-1.20.0-cp37-cp37m-linux_armv7l.whl (11.5MB)
    100% |████████████████████████████████| 11.6MB 37kB/s 
Installing collected packages: numpy, scipy
  The scripts f2py, f2py3 and f2py3.7 are installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-1.20.0 scipy-1.6.0
```
