abc = input()
magazine = dict()
abc = abc.strip()
for f in abc.split(' '):
    magazine.update({f: abc.count(f)})
for n, w in magazine.items():
    print(f'All words "{n}" in line: {w}')
