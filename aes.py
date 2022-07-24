#!/usr/bin/env python3

import argparse
import sys
import uuid
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt(data, padding):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(data, AES.block_size))
    print("IV: ", fmt_output(cipher.iv, padding))
    print("KEY: ", fmt_output(key, padding))
    return ct


def fmt_output(ct, padding):
    p = '02x' if padding == True else '1x'
    fmt_data = '0x' + ',0x'.join(format(x, p) for x in ct)
    return fmt_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='aes.py')
    parser.add_argument(
        '-f', help='bin file to encrypt'
    )
    parser.add_argument(
        '--pad', dest='pad', help='Pad with 0 so all output is 2 chars wide 0x0 => 0x00', action=argparse.BooleanOptionalAction, default='--no-pad'
    )
    parser.add_argument(
        '-w', help="File to write encrypted binary payload to. If omitted, output it formatted into byte array and saved to as random uuid filename."
    )
    args = parser.parse_args()
    if args.f == None:
        parser.print_help()
        sys.exit()

    with open(args.f, mode='rb') as file:
        buf = file.read()
        file.close()
        
        ciphertext = encrypt(buf, args.pad)

    if args.w != None:
        with open(args.w, mode='wb') as file:
            file.write(ciphertext)
            file.close
    else:
        f_name = uuid.uuid4()
        file = open(f"{f_name}.txt", "w") 
        file.write(fmt_output(ciphertext, args.pad))
        file.close()
        print(f"[+] Encrypted payload saved as {f_name}.txt!")
        