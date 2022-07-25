# AES
Python3 AES Encryption

```bash
usage: aes.py [-h] [-f F] [--pad | --no-pad] [-w W] [-k K]

options:
  -h, --help       show this help message and exit
  -f F             bin file to encrypt
  --pad, --no-pad  Pad with 0 so all output is 2 chars wide 0x0 => 0x00 (default: --no-pad)
  -w W             File to write encrypted binary payload to. If omitted, output it formatted into byte array and
                   saved to as random uuid filename.
  -k K             Key size. Can be 16, 24 or 32 bytes long (respectively for AES-128, AES-192 or AES-256).
  ```
