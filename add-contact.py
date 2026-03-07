path = '/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro'
content = open(path).read()

# Add CSS for contact dropdown
old = '\t/* Lang dropdown */'
new = (
    '\t/* Contact dropdown */\n'
    '\t.contact-dropdown-wrapper { position: relative; }\n'
    '\t.contact-menu {\n'
    '\t\tdisplay: none; flex-direction: column;\n'
    '\t\tposition: absolute; top: calc(100% + 0.5rem); right: 0;\n'
    '\t\tbackground: var(--surface); border: 1px solid var(--border);\n'
    '\t\tmin-width: 150px; z-index: 200;\n'
    '\t}\n'
    '\t.contact-menu.open { display: flex; }\n'
    '\t.contact-option {\n'
    '\t\tpadding: 0.65rem 1rem; font-family: "DM Mono", monospace;\n'
    '\t\tfont-size: 0.65rem; letter-spacing: 0.08em;\n'
    '\t\tcolor: var(--text-dim); text-decoration: none;\n'
    '\t\ttransition: background 0.15s, color 0.15s;\n'
    '\t}\n'
    '\t.contact-option:hover { background: var(--gold-dim); color: var(--text); }\n'
    '\t/* Lang dropdown */'
)

if old in content:
    content = content.replace(old, new, 1)
    print('OK CSS')
else:
    print('ERREUR CSS')

# Add contact script
old2 = '// Build dropdown lang selector'
new2 = (
    '// Contact dropdown\n'
    'function buildContactDropdown() {\n'
    '  var pairs = [["contactToggle","contactMenu"],["contactToggleMobile","contactMenuMobile"]];\n'
    '  pairs.forEach(function(pair) {\n'
    '    var btn = document.getElementById(pair[0]);\n'
    '    var menu = document.getElementById(pair[1]);\n'
    '    if (!btn || !menu) return;\n'
    '    btn.addEventListener("click", function(e) {\n'
    '      e.stopPropagation();\n'
    '      menu.classList.toggle("open");\n'
    '    });\n'
    '    document.addEventListener("click", function() { menu.classList.remove("open"); });\n'
    '  });\n'
    '}\n'
    'buildContactDropdown();\n'
    '// Build dropdown lang selector'
)

if old2 in content:
    content = content.replace(old2, new2, 1)
    print('OK script')
else:
    print('ERREUR script')

open(path, 'w').write(content)
print('Fichier sauvegarde')
