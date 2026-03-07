path = '/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro'
lines = open(path).read().split('\n')
# Fix lines 234-238 (index 233-237)
lines[233] = '\t.nav-cta {'
lines[234] = '\t\tbackground: none !important; color: var(--gold) !important;'
lines[235] = '\t\tborder: 1px solid var(--border) !important;'
lines[236] = '\t\tpadding: 0.55rem 1.2rem !important; cursor: pointer; transition: background 0.25s !important;'
lines[237] = '\t}'
lines[238] = '\t.nav-cta:hover { background: var(--gold-dim) !important; }'
open(path, 'w').write('\n'.join(lines))
print('OK')
