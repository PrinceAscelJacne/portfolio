import re

path = "/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro"
content = open(path).read()

# 1. Add light theme CSS variables after :root
old_root = """\t:root {
		--bg: #07080a;
		--surface: #0e1015;
		--surface2: #13161c;
		--gold: #c9a84c;
		--gold-light: #e8c97a;
		--gold-dim: rgba(201,168,76,0.15);
		--text: #eeeae3;
		--text-dim: #7a7570;
		--text-mid: #b5b0a8;
		--border: rgba(201,168,76,0.18);
		--border-subtle: rgba(255,255,255,0.06);
	}"""

new_root = """\t:root {
		--bg: #07080a;
		--surface: #0e1015;
		--surface2: #13161c;
		--gold: #c9a84c;
		--gold-light: #e8c97a;
		--gold-dim: rgba(201,168,76,0.15);
		--text: #eeeae3;
		--text-dim: #7a7570;
		--text-mid: #b5b0a8;
		--border: rgba(201,168,76,0.18);
		--border-subtle: rgba(255,255,255,0.06);
	}
	[data-theme="light"] {
		--bg: #f8f6f2;
		--surface: #ffffff;
		--surface2: #f0ece4;
		--gold: #a07828;
		--gold-light: #c9a84c;
		--gold-dim: rgba(160,120,40,0.1);
		--text: #1a1810;
		--text-dim: #8a8070;
		--text-mid: #5a5248;
		--border: rgba(160,120,40,0.25);
		--border-subtle: rgba(0,0,0,0.08);
	}
	/* Theme toggle button */
	.theme-toggle {
		background: none;
		border: 1px solid var(--border-subtle);
		color: var(--text-dim);
		cursor: pointer;
		padding: 0.5rem 0.7rem;
		font-size: 1rem;
		line-height: 1;
		transition: border-color 0.25s, color 0.25s;
		display: flex;
		align-items: center;
	}
	.theme-toggle:hover { border-color: var(--border); color: var(--text); }"""

if old_root in content:
    content = content.replace(old_root, new_root, 1)
    print("OK - variables thème ajoutées")
else:
    print("ERREUR - :root non trouvé")
    open(path, 'w').write(content)
    exit()

# 2. Add toggle button in desktop navbar (before nav-cta)
old_nav_cta = '\t\t<a href="mailto:djibodeprinceascel@gmail.com" class="nav-cta">Contact</a>'
new_nav_cta = '\t\t<button class="theme-toggle" id="themeToggle" title="Changer le thème">☀️</button>\n\t\t<a href="mailto:djibodeprinceascel@gmail.com" class="nav-cta">Contact</a>'
if old_nav_cta in content:
    content = content.replace(old_nav_cta, new_nav_cta, 1)
    print("OK - bouton ajouté dans navbar desktop")
else:
    print("ERREUR - nav-cta non trouvé")

# 3. Add toggle button in mobile navbar
old_mobile = '\t\t<a href="mailto:djibodeprinceascel@gmail.com" class="nav-mobile-contact">Contact</a>'
new_mobile = '\t\t<button class="theme-toggle" id="themeToggleMobile" title="Changer le thème">☀️</button>\n\t\t<a href="mailto:djibodeprinceascel@gmail.com" class="nav-mobile-contact">Contact</a>'
if old_mobile in content:
    content = content.replace(old_mobile, new_mobile, 1)
    print("OK - bouton ajouté dans navbar mobile")
else:
    print("ERREUR - nav-mobile-contact non trouvé")

# 4. Add script before </Layout>
old_end = '</Layout>'
new_end = """<script>
  const STORAGE_KEY = 'pad-theme';
  const toggle1 = document.getElementById('themeToggle');
  const toggle2 = document.getElementById('themeToggleMobile');

  function getTheme() {
    return localStorage.getItem(STORAGE_KEY) || 'dark';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme === 'light' ? 'light' : '');
    const icon = theme === 'light' ? '🌙' : '☀️';
    if (toggle1) toggle1.textContent = icon;
    if (toggle2) toggle2.textContent = icon;
  }

  function toggleTheme() {
    const next = getTheme() === 'dark' ? 'light' : 'dark';
    localStorage.setItem(STORAGE_KEY, next);
    applyTheme(next);
  }

  // Init
  applyTheme(getTheme());
  if (toggle1) toggle1.addEventListener('click', toggleTheme);
  if (toggle2) toggle2.addEventListener('click', toggleTheme);
</script>
</Layout>"""

if old_end in content:
    content = content.replace(old_end, new_end, 1)
    print("OK - script ajouté")
else:
    print("ERREUR - </Layout> non trouvé")

open(path, 'w').write(content)
print("✅ Fichier mis à jour !")
