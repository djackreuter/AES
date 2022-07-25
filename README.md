# AES
Python3 AES Encryption
Writes encrypted data to a random uuid filename.

```bash
usage: aes.py [-h] [-f F] [--pad | --no-pad] [--raw | --no-raw] [-k K]

optional arguments:
  -h, --help       show this help message and exit
  -f F             bin file to encrypt
  --pad, --no-pad  Pad with 0 so all output is 2 chars wide 0x0 => 0x00 (default: --no-pad)
  --raw, --no-raw  Data will be saved as raw binary file. (default: --no-raw)
  -k K             Key size. Can be 16, 24 or 32 bytes long (respectively for AES-128, AES-192 or AES-256).
```
