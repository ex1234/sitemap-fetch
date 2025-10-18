import sys, urllib.request, pathlib
if len(sys.argv)<2: print("Usage: sitemap.py <url>"); raise SystemExit
data = urllib.request.urlopen(sys.argv[1], timeout=10).read()
pathlib.Path('sitemap.xml').write_bytes(data)
print('Saved sitemap.xml')
