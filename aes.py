#!/usr/bin/env python3

import argparse
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt(data, padding):
    key = get_random_bytes(16)
    cipher = AES.new(hashlib.sha256(key).digest(), AES.MODE_CBC)
    ct = cipher.encrypt(pad(data, AES.block_size))

    p = '02x' if padding == True else '1x'
    print('char key[] = { 0x' + ', 0x'.join(format(x, p) for x in key) + '};')
    print('{ 0x' + ', 0x'.join(format(x, p) for x in ct) + '};')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='aes.py')
    parser.add_argument(
        '-f', help='bin file to encrypt'
    )
    parser.add_argument(
        '--pad', dest='pad', help='Pad with 0 so all output is 2 chars wide 0x0 => 0x00', action=argparse.BooleanOptionalAction, default='--no-pad'
    )
    args = parser.parse_args()

    if args.f != None:
        with open(args.f, mode='rb') as file:
            buf = file.read()
            file.close()
        
        encrypt(buf, args.pad)