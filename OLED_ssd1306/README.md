[https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/](https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/)
```
sudo pip3 install luma.oled
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting luma.oled
  Downloading https://files.pythonhosted.org/packages/d5/3c/2a464be33c7a29633506b75c579cb50356a1e788609db809bf7999c74511/luma.oled-3.8.1-py2.py3-none-any.whl
Collecting luma.core>=2.0.0 (from luma.oled)
  Downloading https://files.pythonhosted.org/packages/b0/cb/a163a2b3b4adc3232163257fb39bf5e5aa03f7791d6ce06b595088f692a7/luma.core-2.2.0-py2.py3-none-any.whl (67kB)
    100% |████████████████████████████████| 71kB 812kB/s 
Requirement already satisfied: spidev; platform_system == "Linux" in /usr/lib/python3/dist-packages (from luma.core>=2.0.0->luma.oled) (3.4)
Collecting deprecated (from luma.core>=2.0.0->luma.oled)
  Downloading https://files.pythonhosted.org/packages/d4/56/7d4774533d2c119e1873993d34d313c9c9efc88c5e4ab7e33bdf915ad98c/Deprecated-1.2.11-py2.py3-none-any.whl
Requirement already satisfied: pillow>=4.0.0 in /usr/local/lib/python3.7/dist-packages (from luma.core>=2.0.0->luma.oled) (8.1.0)
Requirement already satisfied: pyftdi in /usr/local/lib/python3.7/dist-packages (from luma.core>=2.0.0->luma.oled) (0.52.9)
Requirement already satisfied: RPI.GPIO; platform_system == "Linux" in /usr/lib/python3/dist-packages (from luma.core>=2.0.0->luma.oled) (0.7.0)
Collecting smbus2 (from luma.core>=2.0.0->luma.oled)
  Downloading https://files.pythonhosted.org/packages/c8/bf/62ef029fb7077fc87c3539f7365859bccc6cedb2bb20796b737b788c8d09/smbus2-0.4.1-py2.py3-none-any.whl
Collecting cbor2 (from luma.core>=2.0.0->luma.oled)
  Downloading https://www.piwheels.org/simple/cbor2/cbor2-5.2.0-cp37-cp37m-linux_armv7l.whl (156kB)
    100% |████████████████████████████████| 163kB 246kB/s 
Requirement already satisfied: wrapt<2,>=1.10 in /usr/lib/python3/dist-packages (from deprecated->luma.core>=2.0.0->luma.oled) (1.10.11)
Requirement already satisfied: pyusb>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from pyftdi->luma.core>=2.0.0->luma.oled) (1.1.1)
Requirement already satisfied: pyserial>=3.0 in /usr/lib/python3/dist-packages (from pyftdi->luma.core>=2.0.0->luma.oled) (3.4)
Installing collected packages: deprecated, smbus2, cbor2, luma.core, luma.oled
Successfully installed cbor2-5.2.0 deprecated-1.2.11 luma.core-2.2.0 luma.oled-3.8.1 smbus2-0.4.1

```
```
sudo pip3 install Adafruit-SSD1306
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting Adafruit-SSD1306
  Downloading https://www.piwheels.org/simple/adafruit-ssd1306/Adafruit_SSD1306-1.6.2-py3-none-any.whl
Requirement already satisfied: Adafruit-GPIO>=0.6.5 in /usr/local/lib/python3.7/dist-packages (from Adafruit-SSD1306) (1.0.3)
Requirement already satisfied: adafruit-pureio in /usr/local/lib/python3.7/dist-packages (from Adafruit-GPIO>=0.6.5->Adafruit-SSD1306) (1.1.8)
Requirement already satisfied: spidev in /usr/lib/python3/dist-packages (from Adafruit-GPIO>=0.6.5->Adafruit-SSD1306) (3.4)
Installing collected packages: Adafruit-SSD1306
Successfully installed Adafruit-SSD1306-1.6.2
```
```
sudo pip3 install Adafruit-BBIO
```
```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting Adafruit-BBIO
  Downloading https://www.piwheels.org/simple/adafruit-bbio/Adafruit_BBIO-1.2.0-cp37-cp37m-linux_armv7l.whl (298kB)
    100% |████████████████████████████████| 307kB 229kB/s 
Installing collected packages: Adafruit-BBIO
Successfully installed Adafruit-BBIO-1.2.0
```
