#!/bin/bash -e
for i in `grep -l 'dip links start' *.md` ; do 
    python _dip_links.py $i
    mv $i.out $i
done
