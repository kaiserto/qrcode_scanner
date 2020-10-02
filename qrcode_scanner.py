#!/usr/bin/python3

import sys
import hid

CHARCODES_LOWER = {
    4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k',
    15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v',
    26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7',
    37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';',
    52: '\'', 53: '~', 54: ',', 55: '.', 56: '/', 86: '-'
}

CHARCODES_UPPER = {
    4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K',
    15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V',
    26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&',
    37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"',
    53: '~', 54: '<', 55: '>', 56: '?'
}

DEBUG = False # True or False
SHIFT_CODE = 2
CR_CODE = 40

def qrcode_scanner(idVendor, idProduct):

    h = hid.device()
    h.open(idVendor, idProduct)
    __debug("Manufacturer: %s\n" % h.get_manufacturer_string())
    __debug("Product: %s\n" % h.get_product_string())
    __debug("Serial No: %s\n" % h.get_serial_number_string())

    qrcode_output = ''
    CHARCODES = CHARCODES_LOWER
    while True:
        buffer = h.read(8)
        for char_code in [item for item in buffer if item > 0]:
            if char_code == CR_CODE:
                h.close()
                return qrcode_output
            if char_code == SHIFT_CODE:
                CHARCODES = CHARCODES_UPPER
            else:
                char = CHARCODES.get(char_code, '?')
                if char == '?':
                    __debug("Char code %u not found!\n" % char_code)
                qrcode_output += char
                CHARCODES = CHARCODES_LOWER

def __debug(message):
    sys.stderr.write(message) if DEBUG else None



if __name__ == '__main__':
    VENDOR_ID = 0xac90
    PRODUCT_ID = 0x3002
    if len(sys.argv) == 3:
        VENDOR_ID = int(sys.argv[1], 0)
        PRODUCT_ID = int(sys.argv[2], 0)
    qrcode = qrcode_scanner(VENDOR_ID, PRODUCT_ID)
    print(qrcode)

