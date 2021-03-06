#!/usr/bin/env python3
"""
Usage:
  clash_entry [options]

Options:
  --server-host=<host>  
  --server-port=<port>      [default: 9999]
  --server-method=<method>  [default: aes-256-cfb]
  --server-password=<pwd>
  --http-port=<port>        [default: 1080]
  --socks-port=<port>       [default: 1060]
"""
from docopt import docopt as docoptinit
from pathlib import Path
import re
import os
docopt = docoptinit(__doc__)
print(docopt)


def get_new_txt():
    for p in ['./clash_config.template', '/clash_config.template']:
        p = Path(p)
        if not p.exists():
            continue
        txt = p.read_text()
        new_txt = txt
        for x in re.findall('{{.*}}', txt):
            docopt_key = '--' + \
                x.replace('{{', '').replace('}}', '').lower().replace('_', '-')
            print(x, docopt_key)
            new_txt = new_txt.replace(x, docopt.get(docopt_key, ''))
        return new_txt


def main():
    Path('/clash_config.yml').write_text(get_new_txt())
    os.system('clash -f /clash_config.yml')


if __name__ == '__main__':
    main()
