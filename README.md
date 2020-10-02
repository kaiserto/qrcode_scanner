# qrcode_scanner

Usage:
--

See: test_scanner.py or test_scanner.sh

Installation
--

```
groupadd -r usbusers
vi /etc/udev/rules.d/99-usb.rules
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", MODE="0664", GROUP="usbusers"
usermod -a -G usbusers kaisert
``` 

Python 2
---

```
apt install python-pip
apt install libusb-1.0-0 libusb-1.0-0-dev
apt install libudev1 libudev-dev
pip2 install hidapi
```

Python 3
---

```
apt install python3-pip
apt install libusb-1.0-0 libusb-1.0-0-dev
apt install libudev1 libudev-dev
pip3 install hidapi
```

