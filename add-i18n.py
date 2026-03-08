path = "/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro"
content = open(path).read()

# 1. Add translations script before </script> closing of theme script
old_script_end = """  // Init
  applyTheme(getTheme());
  if (toggle1) toggle1.addEventListener('click', toggleTheme);
  if (toggle2) toggle2.addEventListener('click', toggleTheme);
</script>"""

new_script = """  // Init
  applyTheme(getTheme());
  if (toggle1) toggle1.addEventListener('click', toggleTheme);
  if (toggle2) toggle2.addEventListener('click', toggleTheme);
</script>

<script>
const LANG_KEY = 'pad-lang';

const translations = {
  fr: {
    badge: "Disponible pour un stage · 3 mois",
    role: "Étudiant en Licence 3 MIAGE — Développeur Full Stack",
    school: "@ Université de Haute-Alsace",
    description: "Étudiant en L3 MIAGE à FST UHA, je suis à la recherche d'un stage de 3 mois en tant que Développeur Full Stack. Passionné par la création d'applications web complètes, je maîtrise les environnements Front-end et Back-end. Rigoureux et curieux, je souhaite mettre mes compétences au service d'un projet concret au sein de votre équipe.",
    btnProjects: "Voir mes projets",
    btnCv: "↓ Télécharger CV",
    location: "📍 Mulhouse, France · Mobilité",
    nav: { about: "À propos", skills: "Compétences", formations: "Formations", experience: "Expériences", projects: "Projets", cv: "Télécharger CV", contact: "Contact" },
    dividers: ["Compétences techniques", "Parcours académique", "Expérience professionnelle", "Réalisations personnelles", "Profil complet"],
    sec1title: ["Domaines d'", "expertise"],
    sec2title: ["Formations & ", "diplômes"],
    sec3title: ["Expériences ", "terrain"],
    sec4title: ["Projets ", "GitHub"],
    sec5title: ["Langues, ", "atouts", " & intérêts"],
    expType: "Stage",
    aside: ["Langues", "Atouts", "Centres d'intérêt"],
    footer: "DJIBODE Prince Ascel Jacné — Portfolio 2025",
    cvBtn: "↓ CV",
  },
  en: {
    badge: "Available for internship · 3 months",
    role: "Bachelor's student in MIAGE — Full Stack Developer",
    school: "@ University of Upper Alsace",
    description: "L3 MIAGE student at FST UHA, I am looking for a 3-month internship as a Full Stack Developer. Passionate about building complete web applications, I master both Front-end and Back-end environments. Rigorous and curious, I want to put my skills to work on a concrete project within your team.",
    btnProjects: "See my projects",
    btnCv: "↓ Download CV",
    location: "📍 Mulhouse, France · Mobility",
    nav: { about: "About", skills: "Skills", formations: "Education", experience: "Experience", projects: "Projects", cv: "Download CV", contact: "Contact" },
    dividers: ["Technical skills", "Academic background", "Professional experience", "Personal projects", "Full profile"],
    sec1title: ["Areas of ", "expertise"],
    sec2title: ["Education & ", "degrees"],
    sec3title: ["Work ", "experience"],
    sec4title: ["GitHub ", "projects"],
    sec5title: ["Languages, ", "strengths", " & interests"],
    expType: "Internship",
    aside: ["Languages", "Strengths", "Interests"],
    footer: "DJIBODE Prince Ascel Jacné — Portfolio 2025",
    cvBtn: "↓ CV",
  },
  de: {
    badge: "Verfügbar für Praktikum · 3 Monate",
    role: "Bachelor-Student MIAGE — Full Stack Entwickler",
    school: "@ Universität Oberelsass",
    description: "L3-MIAGE-Student an der FST UHA, ich suche ein 3-monatiges Praktikum als Full-Stack-Entwickler. Ich beherrsche sowohl Front-end- als auch Back-end-Umgebungen und möchte meine Fähigkeiten in Ihrem Team einsetzen.",
    btnProjects: "Meine Projekte",
    btnCv: "↓ Lebenslauf herunterladen",
    location: "📍 Mulhouse, Frankreich · Mobilität",
    nav: { about: "Über mich", skills: "Kenntnisse", formations: "Ausbildung", experience: "Erfahrung", projects: "Projekte", cv: "Lebenslauf", contact: "Kontakt" },
    dividers: ["Technische Kenntnisse", "Akademischer Werdegang", "Berufserfahrung", "Eigene Projekte", "Vollständiges Profil"],
    sec1title: ["Fachgebiete ", "Expertise"],
    sec2title: ["Ausbildung & ", "Abschlüsse"],
    sec3title: ["Berufliche ", "Erfahrung"],
    sec4title: ["GitHub ", "Projekte"],
    sec5title: ["Sprachen, ", "Stärken", " & Interessen"],
    expType: "Praktikum",
    aside: ["Sprachen", "Stärken", "Interessen"],
    footer: "DJIBODE Prince Ascel Jacné — Portfolio 2025",
    cvBtn: "↓ CV",
  }
};

function getLang() {
  return localStorage.getItem(LANG_KEY) || 'fr';
}

function applyLang(lang) {
  const t = translations[lang];
  if (!t) return;
  localStorage.setItem(LANG_KEY, lang);

  // Update lang selector buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  // Badge
  const badge = document.querySelector('.badge');
  if (badge) badge.childNodes[badge.childNodes.length - 1].textContent = t.badge;

  // Hero role
  const roleSpans = document.querySelectorAll('.hero-role span');
  if (roleSpans[0]) roleSpans[0].textContent = t.role;
  if (roleSpans[1]) roleSpans[1].textContent = t.school;

  // Hero desc
  const desc = document.querySelector('.hero-desc');
  if (desc) desc.textContent = t.description;

  // Buttons
  const btnMain = document.querySelector('.btn-main');
  if (btnMain) btnMain.textContent = t.btnProjects;
  const btnOutline = document.querySelector('.btn-outline');
  if (btnOutline) btnOutline.textContent = t.btnCv;

  // Location
  const metaSpans = document.querySelectorAll('.hero-meta span');
  if (metaSpans[0]) metaSpans[0].textContent = t.location;

  // Navbar links
  const navLinks = document.querySelectorAll('.nav-links a:not(.nav-cta):not(.nav-cv)');
  const keys = ['about','skills','formations','experience','projects'];
  navLinks.forEach((a, i) => { if (keys[i]) a.textContent = t.nav[keys[i]]; });
  const navCv = document.querySelector('.nav-cv');
  if (navCv) navCv.textContent = t.nav.cv;
  const navCta = document.querySelector('.nav-cta');
  if (navCta) navCta.textContent = t.nav.contact;
  const navMobileCv = document.querySelector('.nav-mobile-cv');
  if (navMobileCv) navMobileCv.textContent = t.cvBtn;
  const navMobileContact = document.querySelector('.nav-mobile-contact');
  if (navMobileContact) navMobileContact.textContent = t.nav.contact;

  // Dividers
  document.querySelectorAll('.divider-label').forEach((el, i) => {
    if (t.dividers[i]) el.textContent = t.dividers[i];
  });

  // Aside titles
  document.querySelectorAll('.aside-card h3').forEach((el, i) => {
    if (t.aside[i]) el.textContent = t.aside[i];
  });

  // Exp type badges
  document.querySelectorAll('.exp-type').forEach(el => {
    el.textContent = t.expType;
  });

  // Footer
  const footerLeft = document.querySelector('.footer-left');
  if (footerLeft) footerLeft.textContent = t.footer;
}

// Build lang selector
function buildLangSelector() {
  const langs = [
    { code: 'fr', label: 'FR' },
    { code: 'en', label: 'EN' },
    { code: 'de', label: 'DE' },
  ];
  const container = document.getElementById('langSelector');
  const containerMobile = document.getElementById('langSelectorMobile');
  [container, containerMobile].forEach(c => {
    if (!c) return;
    langs.forEach(l => {
      const btn = document.createElement('button');
      btn.className = 'lang-btn';
      btn.dataset.lang = l.code;
      btn.textContent = l.label;
      btn.addEventListener('click', () => applyLang(l.code));
      c.appendChild(btn);
    });
  });
}

buildLangSelector();
applyLang(getLang());
</script>"""

if old_script_end in content:
    content = content.replace(old_script_end, new_script, 1)
    print("OK - script i18n ajouté")
else:
    print("ERREUR - fin script non trouvée")

# 2. Add lang selector CSS
old_theme_toggle_css = """\t/* Theme toggle button */
\t.theme-toggle {"""

new_lang_css = """\t/* Lang selector */
\t.lang-selector {
\t\tdisplay: flex;
\t\talign-items: center;
\t\tgap: 0.2rem;
\t}
\t.lang-btn {
\t\tbackground: none;
\t\tborder: 1px solid transparent;
\t\tcolor: var(--text-dim);
\t\tcursor: pointer;
\t\tpadding: 0.3rem 0.5rem;
\t\tfont-family: 'DM Mono', monospace;
\t\tfont-size: 0.6rem;
\t\tletter-spacing: 0.1em;
\t\ttransition: color 0.2s, border-color 0.2s;
\t}
\t.lang-btn:hover { color: var(--text); }
\t.lang-btn.active {
\t\tcolor: var(--gold);
\t\tborder-color: var(--border);
\t}
\t/* Theme toggle button */
\t.theme-toggle {"""

if old_theme_toggle_css in content:
    content = content.replace(old_theme_toggle_css, new_lang_css, 1)
    print("OK - CSS lang ajouté")
else:
    print("ERREUR - CSS theme-toggle non trouvé")

# 3. Add lang selector in desktop navbar
old_nav_toggle = '\t\t<button class="theme-toggle" id="themeToggle" title="Changer le thème">☀️</button>'
new_nav_toggle = '\t\t<div class="lang-selector" id="langSelector"></div>\n\t\t<button class="theme-toggle" id="themeToggle" title="Changer le thème">☀️</button>'
if old_nav_toggle in content:
    content = content.replace(old_nav_toggle, new_nav_toggle, 1)
    print("OK - lang selector ajouté navbar desktop")
else:
    print("ERREUR - themeToggle desktop non trouvé")

# 4. Add lang selector in mobile navbar
old_mobile_toggle = '\t\t<button class="theme-toggle" id="themeToggleMobile" title="Changer le thème">☀️</button>'
new_mobile_toggle = '\t\t<div class="lang-selector" id="langSelectorMobile"></div>\n\t\t<button class="theme-toggle" id="themeToggleMobile" title="Changer le thème">☀️</button>'
if old_mobile_toggle in content:
    content = content.replace(old_mobile_toggle, new_mobile_toggle, 1)
    print("OK - lang selector ajouté navbar mobile")
else:
    print("ERREUR - themeToggleMobile non trouvé")

open(path, 'w').write(content)
print("✅ Fichier mis à jour !")
