path = '/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro'
lines = open(path).read().split('\n')
lines[235] = '\t\tbackground: none !important; color: var(--gold) !important; border: 1px solid var(--border) !important;'
lines[236] = '\t\tpadding: 0.55rem 1.2rem !important; cursor: pointer; transition: background 0.25s !important;'
open(path, 'w').write('\n'.join(lines))
print('OK')
