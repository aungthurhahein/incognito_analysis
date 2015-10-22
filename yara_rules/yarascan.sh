#! /bin/bash

python ~atrx/volatility-2.4/vol.py -f ~atrx/forensictools/2.memExp11112014/memdump/youtube.dump --profile=Win8SP0x64 -p 600 yarascan --yara-file=yara.rules > youtube.out
python ~atrx/volatility-2.4/vol.py -f ~atrx/forensictools/2.memExp11112014/memdump/9gag.dump --profile=Win8SP0x64 -p 2562,2700 yarascan --yara-file=yara.rules > 9gag.out
python ~atrx/volatility-2.4/vol.py -f ~atrx/forensictools/2.memExp11112014/memdump/soundcloud.dump --profile=Win8SP0x64 -p 2876,1176 yarascan --yara-file=yara.rules > soundcloud.out
python ~atrx/volatility-2.4/vol.py -f ~atrx/forensictools/2.memExp11112014/memdump/twitter.dump --profile=Win8SP0x64 -p 2304 yarascan --yara-file=yara.rules > twitter.out
python ~atrx/volatility-2.4/vol.py -f ~atrx/forensictools/2.memExp11112014/memdump/amazon.dump --profile=Win8SP0x64 -p 1620 yarascan --yara-file=yara.rules > amazon.out
