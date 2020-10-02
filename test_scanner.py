#!/usr/bin/python3

from qrcode_scanner import qrcode_scanner

VENDOR_ID = 0xac90
PRODUCT_ID = 0x3002

while True:
    qrcode = qrcode_scanner(VENDOR_ID, PRODUCT_ID)
    print(qrcode)

