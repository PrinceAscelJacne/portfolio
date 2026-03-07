path = '/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro'
lines = open(path).read().split('\n')

# Find the orphan lines after nav-cta:hover and fix nav-cv
for i, line in enumerate(lines):
    if 'nav-cta:hover' in line:
        print(f"nav-cta:hover at line {i+1}")
        print(f"  next: {repr(lines[i+1])}")
        print(f"  next2: {repr(lines[i+2])}")
        print(f"  next3: {repr(lines[i+3])}")
        # Fix: insert .nav-cv { before the orphan lines
        if 'color: var(--text-dim)' in lines[i+1]:
            lines[i+1] = '\t.nav-cv {'
            print("Fixed: inserted .nav-cv {")
        break

open(path, 'w').write('\n'.join(lines))
print('Done')
