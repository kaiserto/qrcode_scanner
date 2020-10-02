#!/bin/bash

VENDOR_ID=0xac90
PRODUCT_ID=0x3002

while true; do
  # QR_CODE=`./qrcode_scanner.py "$VENDOR_ID" "$PRODUCT_ID"`
  QR_CODE=`python qrcode_scanner.py "$VENDOR_ID" "$PRODUCT_ID"`
  echo "$QR_CODE"
done

