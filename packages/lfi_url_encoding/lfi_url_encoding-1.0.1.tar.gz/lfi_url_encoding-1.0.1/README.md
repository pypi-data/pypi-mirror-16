# LFI URL Encoding

A tool to encode URLs for LFI vulnerability.

**Note**: this tool does not intend to encode all ASCII or UTF-8 characters but only those which are usefull for LFI testing.

## Requirements

This software was designed for Python 3, it mays work under Python 2.

This software was tested with Python 3.4.1 and 3.5.2.

This software uses those python libraries:
- [argparse](https://docs.python.org/3/library/argparse.html)

## Usage

```
usage: LFI-encoding.py [-h] (-s <string> | -d <string>) [-a] [-n]

LFI-encoding - Encoding url for LFI

optional arguments:
  -h, --help            show this help message and exit
  -s <string>, --simple <string>
                        Simple encoding
  -d <string>, --double <string>
                        Double encoding
  -a, --advanced        Advanced encoding ('&', '+', '=')
  -n, --null_byte       Append a null byte
```

## Examples

Simple encoding:
```
./LFI-encoding.py -s ../../../../etc/passwd
%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2Fetc%2Fpasswd
```

Double encoding:
```
./LFI-encoding.py -d ../../../../etc/passwd
%252E%252E%252F%252E%252E%252F%252E%252E%252F%252E%252E%252Fetc%252Fpasswd
```

Null byte:
```
./LFI-encoding.py -s ../../etc/passwd -n
%2E%2E%2F%2E%2E%2Fetc%2Fpasswd%00
```

Advanced encoding vs normal:
```
./LFI-encoding.py -s 'context=config&file=conf.inc.php~' -a
context%3Dconfig%26file%3Dconf%2Einc%2Ephp%7E

./LFI-encoding.py -s 'context=config&file=conf.inc.php~'
context=config&file=conf%2Einc%2Ephp~
```

## Install

- **Online**: run `pip install lfi_url_encoding`
- **Offline**:
  + Download [the archive](https://pypi.python.org/pypi?:action=display&name=lfi_url_encoding&version=1.0)
  + Unpack the archive
  + Go into the folder and run `python setup.py install`
