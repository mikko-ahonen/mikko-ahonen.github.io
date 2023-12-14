import sys
import re

start_tag = '<!-- dip links start -->'
end_tag = '<!-- dip links end -->'

def dip_links():
    with open('_dip_links.in') as f:
        d = f.read()
        return d

def replace_links(dip_links, fn):
    with open(fn) as inf:
        with open(fn + '.out', 'w') as outf:
            ind = inf.read()
            outd = re.sub(re.escape(start_tag) + '.*' + re.escape(end_tag), start_tag + dip_links + end_tag, ind, flags=re.MULTILINE|re.DOTALL)
            outf.write(outd)

for fn in sys.argv[1:]:
    print(fn)
    dl = dip_links()
    replace_links(dl, fn)

sys.exit(0)
