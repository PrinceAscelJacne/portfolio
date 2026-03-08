path = "/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro"
content = open(path).read()

# Find and replace the entire i18n script block
import re

old_script = re.search(r'<script>\s*const LANG_KEY.*?</script>', content, re.DOTALL)
if not old_script:
    print("ERREUR - script i18n non trouvé")
    exit()

new_script = """<script>
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
    phone: "📞 07 45 36 03 07",
    linkedin: "🔗 linkedin: Prince_Ascel_Jacne_DJIBODE",
    nav: { about: "À propos", skills: "Compétences", formations: "Formations", experience: "Expériences", projects: "Projets", cv: "Télécharger CV", contact: "Contact", lang: "Langue" },
    dividers: ["Compétences techniques", "Parcours académique", "Expérience professionnelle", "Réalisations personnelles", "Profil complet"],
    sec1: ["Domaines d'", "expertise"],
    sec2: ["Formations & ", "diplômes"],
    sec3: ["Expériences ", "terrain"],
    sec4: ["Projets ", "GitHub"],
    sec5: ["Langues, ", "atouts", " & intérêts"],
    expType: "Stage",
    aside: ["Langues", "Atouts", "Centres d'intérêt"],
    footer: "DJIBODE Prince Ascel Jacné — Portfolio 2025",
    cvBtn: "↓ CV",
    skillCats: ["Web & Frameworks", "Langages & Mobile", "Analyse & BD", "Outils"],
    formations: [
      { degree: "Licence 3 MIAGE", school: "FST UHA — Mulhouse", period: "Depuis 2025" },
      { degree: "Licence Pro. Analyse Informatique & Programmation", school: "ENEAM — Cotonou, Bénin", period: "2023 — 2024" },
      { degree: "Baccalauréat Série D", school: "Sainte Jeanne d'Arc — Bénin", period: "2020 — 2021" },
      { degree: "Brevet d'Étude du Premier Cycle", school: "CEG 1 Allada — Bénin", period: "2016 — 2017" },
    ],
    experiences: [
      {
        role: "Développeur web", type: "Stage", company: "ASTUS CITEE", location: "Cotonou, Bénin", date: "Mai — Août 2024",
        details: ["Développement d'une application de gestion des fichiers (centralisation, sécurisation, accès documents)", "Création d'un site web vitrine pour renforcer la visibilité de l'entreprise", "Intégration d'une interface moderne et ergonomique", "Collaboration avec l'équipe interne pour recueillir les besoins et tester les fonctionnalités"]
      },
      {
        role: "Analyste programmeur", type: "Stage", company: "Super U Erevan", location: "Bénin", date: "Juil. — Sept. 2023",
        details: ["Participation à la conception et au développement d'applications web", "Contribution à l'analyse des besoins et à la rédaction des cahiers des charges", "Intégration d'interfaces utilisateurs en HTML, CSS et JavaScript", "Collaboration avec l'équipe technique pour les tests et le déploiement"]
      }
    ],
    projects: [
      { title: "Crypto — Chiffrement de messages", desc: "Application de chiffrement polyalphabétique : l'utilisateur saisit un mot, une phrase ou un paragraphe, et le programme retourne le message codé en tenant compte des espaces." },
      { title: "Astus Citée — Gestion de fichiers", desc: "Application web de gestion documentaire développée en stage : centralisation, sécurisation et accès aux fichiers internes de l'entreprise, avec interface moderne et ergonomique." },
      { title: "Astus Citée — Site vitrine", desc: "Site web vitrine développé en stage chez Astus Citée pour présenter l'entreprise et renforcer sa visibilité en ligne." }
    ],
    githubBtn: "Voir sur GitHub →",
    langNames: ["Français", "Anglais", "Allemand"],
    softSkills: ["Esprit d'équipe", "Dynamique & motivé", "Sens de l'analyse", "Capacité d'adaptation"],
    interests: ["Football", "Jeux vidéos", "Voyage", "Musique"],
  },
  en: {
    badge: "Available for internship · 3 months",
    role: "Bachelor's student MIAGE — Full Stack Developer",
    school: "@ University of Upper Alsace",
    description: "L3 MIAGE student at FST UHA, I am looking for a 3-month internship as a Full Stack Developer. Passionate about building complete web applications, I master both Front-end and Back-end environments. Rigorous and curious, I want to put my skills to work on a concrete project within your team.",
    btnProjects: "See my projects",
    btnCv: "↓ Download CV",
    location: "📍 Mulhouse, France · Mobility",
    phone: "📞 +33 7 45 36 03 07",
    linkedin: "🔗 linkedin: Prince_Ascel_Jacne_DJIBODE",
    nav: { about: "About", skills: "Skills", formations: "Education", experience: "Experience", projects: "Projects", cv: "Download CV", contact: "Contact", lang: "Language" },
    dividers: ["Technical skills", "Academic background", "Professional experience", "Personal projects", "Full profile"],
    sec1: ["Areas of ", "expertise"],
    sec2: ["Education & ", "degrees"],
    sec3: ["Work ", "experience"],
    sec4: ["GitHub ", "projects"],
    sec5: ["Languages, ", "strengths", " & interests"],
    expType: "Internship",
    aside: ["Languages", "Strengths", "Interests"],
    footer: "DJIBODE Prince Ascel Jacné — Portfolio 2025",
    cvBtn: "↓ CV",
    skillCats: ["Web & Frameworks", "Languages & Mobile", "Analysis & DB", "Tools"],
    formations: [
      { degree: "Bachelor's in MIAGE", school: "FST UHA — Mulhouse", period: "Since 2025" },
      { degree: "Professional Bachelor in Computer Analysis & Programming", school: "ENEAM — Cotonou, Benin", period: "2023 — 2024" },
      { degree: "High School Diploma (Science)", school: "Sainte Jeanne d'Arc — Benin", period: "2020 — 2021" },
      { degree: "Middle School Certificate", school: "CEG 1 Allada — Benin", period: "2016 — 2017" },
    ],
    experiences: [
      {
        role: "Web Developer", type: "Internship", company: "ASTUS CITEE", location: "Cotonou, Benin", date: "May — Aug. 2024",
        details: ["Development of a file management application (centralization, security, document access)", "Creation of a showcase website to strengthen company visibility", "Integration of a modern and ergonomic interface", "Collaboration with the internal team to gather requirements and test features"]
      },
      {
        role: "Programmer Analyst", type: "Internship", company: "Super U Erevan", location: "Benin", date: "Jul. — Sep. 2023",
        details: ["Participation in the design and development of web applications", "Contribution to requirements analysis and specification writing", "Integration of user interfaces in HTML, CSS and JavaScript", "Collaboration with the technical team for testing and deployment"]
      }
    ],
    projects: [
      { title: "Crypto — Message Encryption", desc: "Polyalphabetic encryption application: the user enters a word, phrase or paragraph, and the program returns the encoded message while preserving spaces." },
      { title: "Astus Citée — File Management", desc: "Web document management application developed during internship: centralization, security and access to internal company files, with a modern ergonomic interface." },
      { title: "Astus Citée — Showcase Website", desc: "Showcase website developed during internship at Astus Citée to present the company and strengthen its online visibility." }
    ],
    githubBtn: "View on GitHub →",
    langNames: ["French", "English", "German"],
    softSkills: ["Team spirit", "Dynamic & motivated", "Analytical mindset", "Adaptability"],
    interests: ["Football", "Video games", "Travel", "Music"],
  },
  de: {
    badge: "Verfügbar für Praktikum · 3 Monate",
    role: "Bachelor-Student MIAGE — Full Stack Entwickler",
    school: "@ Universität Oberelsass",
    description: "L3-MIAGE-Student an der FST UHA, ich suche ein 3-monatiges Praktikum als Full-Stack-Entwickler. Ich beherrsche sowohl Front-end- als auch Back-end-Umgebungen und möchte meine Fähigkeiten in einem konkreten Projekt Ihres Teams einsetzen.",
    btnProjects: "Meine Projekte ansehen",
    btnCv: "↓ Lebenslauf herunterladen",
    location: "📍 Mulhouse, Frankreich · Mobilität",
    phone: "📞 +33 7 45 36 03 07",
    linkedin: "🔗 linkedin: Prince_Ascel_Jacne_DJIBODE",
    nav: { about: "Über mich", skills: "Kenntnisse", formations: "Ausbildung", experience: "Erfahrung", projects: "Projekte", cv: "Lebenslauf", contact: "Kontakt", lang: "Sprache" },
    dividers: ["Technische Kenntnisse", "Akademischer Werdegang", "Berufserfahrung", "Eigene Projekte", "Vollständiges Profil"],
    sec1: ["Fachliche ", "Expertise"],
    sec2: ["Ausbildung & ", "Abschlüsse"],
    sec3: ["Berufliche ", "Erfahrung"],
    sec4: ["GitHub ", "Projekte"],
    sec5: ["Sprachen, ", "Stärken", " & Interessen"],
    expType: "Praktikum",
    aside: ["Sprachen", "Stärken", "Interessen"],
    footer: "DJIBODE Prince Ascel Jacné — Portfolio 2025",
    cvBtn: "↓ CV",
    skillCats: ["Web & Frameworks", "Sprachen & Mobile", "Analyse & DB", "Werkzeuge"],
    formations: [
      { degree: "Bachelor MIAGE", school: "FST UHA — Mulhouse", period: "Seit 2025" },
      { degree: "Beruflicher Bachelor Informatik & Programmierung", school: "ENEAM — Cotonou, Benin", period: "2023 — 2024" },
      { degree: "Abitur (Naturwissenschaften)", school: "Sainte Jeanne d'Arc — Benin", period: "2020 — 2021" },
      { degree: "Mittlere Reife", school: "CEG 1 Allada — Benin", period: "2016 — 2017" },
    ],
    experiences: [
      {
        role: "Web-Entwickler", type: "Praktikum", company: "ASTUS CITEE", location: "Cotonou, Benin", date: "Mai — Aug. 2024",
        details: ["Entwicklung einer Dateiverwaltungsanwendung (Zentralisierung, Sicherheit, Dokumentenzugriff)", "Erstellung einer Unternehmenswebsite zur Stärkung der Online-Präsenz", "Integration einer modernen und ergonomischen Benutzeroberfläche", "Zusammenarbeit mit dem internen Team zur Anforderungserhebung und zum Testen"]
      },
      {
        role: "Programmierer-Analyst", type: "Praktikum", company: "Super U Erevan", location: "Benin", date: "Jul. — Sep. 2023",
        details: ["Mitwirkung bei Konzeption und Entwicklung von Webanwendungen", "Beitrag zur Anforderungsanalyse und Pflichtenhefterstellung", "Integration von Benutzeroberflächen in HTML, CSS und JavaScript", "Zusammenarbeit mit dem technischen Team für Tests und Deployment"]
      }
    ],
    projects: [
      { title: "Crypto — Nachrichtenverschlüsselung", desc: "Polyalphabetische Verschlüsselungsanwendung: Der Benutzer gibt ein Wort, einen Satz oder einen Absatz ein und erhält die kodierte Nachricht mit Leerzeichen." },
      { title: "Astus Citée — Dateiverwaltung", desc: "Web-Dokumentenverwaltung im Praktikum entwickelt: Zentralisierung, Sicherung und Zugriff auf interne Unternehmensdateien mit moderner Oberfläche." },
      { title: "Astus Citée — Unternehmenswebsite", desc: "Unternehmenswebsite im Praktikum bei Astus Citée entwickelt, um das Unternehmen zu präsentieren und seine Online-Sichtbarkeit zu stärken." }
    ],
    githubBtn: "Auf GitHub ansehen →",
    langNames: ["Französisch", "Englisch", "Deutsch"],
    softSkills: ["Teamgeist", "Dynamisch & motiviert", "Analytisches Denken", "Anpassungsfähigkeit"],
    interests: ["Fußball", "Videospiele", "Reisen", "Musik"],
  }
};

function getLang() { return localStorage.getItem(LANG_KEY) || 'fr'; }

function applyLang(lang) {
  const t = translations[lang];
  if (!t) return;
  localStorage.setItem(LANG_KEY, lang);

  // Update active lang button
  document.querySelectorAll('.lang-option').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  // Update dropdown label
  const labels = { fr: '🇫🇷 Français', en: '🇬🇧 English', de: '🇩🇪 Deutsch' };
  document.querySelectorAll('.lang-toggle-label').forEach(el => el.textContent = labels[lang]);

  // Badge
  const badge = document.querySelector('.badge');
  if (badge) { const dot = badge.querySelector('span') || badge; badge.lastChild.textContent = t.badge; }

  // Hero
  const roleSpans = document.querySelectorAll('.hero-role span');
  if (roleSpans[0]) roleSpans[0].textContent = t.role;
  if (roleSpans[1]) roleSpans[1].textContent = t.school;
  const desc = document.querySelector('.hero-desc');
  if (desc) desc.textContent = t.description;
  const btnMain = document.querySelector('.btn-main');
  if (btnMain) btnMain.textContent = t.btnProjects;
  const btnOutline = document.querySelector('.btn-outline');
  if (btnOutline) btnOutline.textContent = t.btnCv;
  const metaSpans = document.querySelectorAll('.hero-meta span');
  if (metaSpans[0]) metaSpans[0].textContent = t.location;
  if (metaSpans[1]) metaSpans[1].textContent = t.phone;
  if (metaSpans[2]) metaSpans[2].textContent = t.linkedin;

  // Navbar
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

  // Section titles
  const secTitles = document.querySelectorAll('.section-title');
  const secs = [t.sec1, t.sec2, t.sec3, t.sec4, t.sec5];
  secTitles.forEach((el, i) => {
    if (!secs[i]) return;
    el.childNodes[0].textContent = secs[i][0];
    const em = el.querySelector('em');
    if (em) em.textContent = secs[i][1];
    if (el.childNodes[2]) el.childNodes[2].textContent = secs[i][2] || '';
  });

  // Skill category labels
  document.querySelectorAll('.skill-card h3').forEach((el, i) => {
    if (t.skillCats[i]) el.textContent = t.skillCats[i];
  });

  // Formations
  document.querySelectorAll('.formation-item').forEach((item, i) => {
    if (!t.formations[i]) return;
    const period = item.querySelector('.formation-period');
    const degree = item.querySelector('.formation-degree');
    const school = item.querySelector('.formation-school');
    if (period) period.textContent = t.formations[i].period;
    if (degree) degree.textContent = t.formations[i].degree;
    if (school) school.textContent = t.formations[i].school;
  });

  // Experiences
  document.querySelectorAll('.exp-card').forEach((card, i) => {
    if (!t.experiences[i]) return;
    const exp = t.experiences[i];
    const type = card.querySelector('.exp-type');
    const date = card.querySelector('.exp-date');
    const role = card.querySelector('.exp-main h3');
    const details = card.querySelectorAll('.exp-details li');
    if (type) type.textContent = exp.type;
    if (date) date.textContent = exp.date;
    if (role) role.textContent = exp.role;
    details.forEach((li, j) => {
      if (exp.details[j]) li.childNodes[li.childNodes.length-1].textContent = exp.details[j];
    });
  });

  // Projects
  document.querySelectorAll('.project-card').forEach((card, i) => {
    if (!t.projects[i]) return;
    const title = card.querySelector('.project-title');
    const desc2 = card.querySelector('.project-desc');
    const link = card.querySelector('.project-link');
    if (title) title.textContent = t.projects[i].title;
    if (desc2) desc2.textContent = t.projects[i].desc;
    if (link) link.textContent = t.githubBtn;
  });

  // Aside titles
  document.querySelectorAll('.aside-card h3').forEach((el, i) => {
    if (t.aside[i]) el.textContent = t.aside[i];
  });

  // Lang bar names
  document.querySelectorAll('.lang-name').forEach((el, i) => {
    if (t.langNames[i]) el.textContent = t.langNames[i];
  });

  // Soft skills
  document.querySelectorAll('.pill:not(.interest)').forEach((el, i) => {
    if (t.softSkills[i]) el.textContent = t.softSkills[i];
  });

  // Interests
  document.querySelectorAll('.pill.interest').forEach((el, i) => {
    if (t.interests[i]) el.textContent = t.interests[i];
  });

  // Footer
  const footerLeft = document.querySelector('.footer-left');
  if (footerLeft) footerLeft.textContent = t.footer;
}

// Build dropdown lang selector
function buildLangSelector() {
  ['langDropdown', 'langDropdownMobile'].forEach((id, isMobile) => {
    const container = document.getElementById(id);
    if (!container) return;
    const currentLang = getLang();
    const labels = { fr: '🇫🇷 Français', en: '🇬🇧 English', de: '🇩🇪 Deutsch' };
    const navLabel = { fr: 'Langue', en: 'Language', de: 'Sprache' };

    container.innerHTML = \`
      <div class="lang-dropdown-wrapper">
        <button class="lang-toggle-btn">
          <span class="lang-toggle-label">\${labels[currentLang]}</span>
          <span class="lang-toggle-arrow">▾</span>
        </button>
        <div class="lang-dropdown-menu" id="langMenu\${id}">
          \${Object.entries(labels).map(([code, label]) =>
            \`<button class="lang-option\${code === currentLang ? ' active' : ''}" data-lang="\${code}">\${label}</button>\`
          ).join('')}
        </div>
      </div>
    \`;

    const toggleBtn = container.querySelector('.lang-toggle-btn');
    const menu = container.querySelector('.lang-dropdown-menu');

    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      menu.classList.toggle('open');
    });

    container.querySelectorAll('.lang-option').forEach(btn => {
      btn.addEventListener('click', () => {
        applyLang(btn.dataset.lang);
        menu.classList.remove('open');
      });
    });

    document.addEventListener('click', () => menu.classList.remove('open'));
  });
}

buildLangSelector();
applyLang(getLang());
</script>"""

content = content[:old_script.start()] + new_script + content[old_script.end():]
print("OK - script i18n remplacé")

# Replace lang-selector divs with lang-dropdown divs in navbar
content = content.replace(
    '<div class="lang-selector" id="langSelector"></div>',
    '<div id="langDropdown"></div>'
)
content = content.replace(
    '<div class="lang-selector" id="langSelectorMobile"></div>',
    '<div id="langDropdownMobile"></div>'
)
print("OK - divs navbar mis à jour")

# Replace old lang CSS with new dropdown CSS
old_lang_css = """\t/* Lang selector */
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
\t}"""

new_lang_css = """\t/* Lang dropdown */
\t.lang-dropdown-wrapper { position: relative; }
\t.lang-toggle-btn {
\t\tbackground: none;
\t\tborder: 1px solid var(--border-subtle);
\t\tcolor: var(--text-dim);
\t\tcursor: pointer;
\t\tpadding: 0.45rem 0.9rem;
\t\tfont-family: 'DM Mono', monospace;
\t\tfont-size: 0.65rem;
\t\tletter-spacing: 0.1em;
\t\tdisplay: flex; align-items: center; gap: 0.4rem;
\t\ttransition: color 0.2s, border-color 0.2s;
\t\twhite-space: nowrap;
\t}
\t.lang-toggle-btn:hover { color: var(--text); border-color: var(--border); }
\t.lang-toggle-arrow { font-size: 0.5rem; opacity: 0.6; }
\t.lang-dropdown-menu {
\t\tdisplay: none;
\t\tposition: absolute;
\t\ttop: calc(100% + 0.5rem);
\t\tright: 0;
\t\tbackground: var(--surface);
\t\tborder: 1px solid var(--border);
\t\tmin-width: 130px;
\t\tz-index: 200;
\t\tflex-direction: column;
\t}
\t.lang-dropdown-menu.open { display: flex; }
\t.lang-option {
\t\tbackground: none;
\t\tborder: none;
\t\tcolor: var(--text-dim);
\t\tcursor: pointer;
\t\tpadding: 0.65rem 1rem;
\t\tfont-family: 'DM Mono', monospace;
\t\tfont-size: 0.65rem;
\t\tletter-spacing: 0.08em;
\t\ttext-align: left;
\t\ttransition: background 0.15s, color 0.15s;
\t}
\t.lang-option:hover { background: var(--gold-dim); color: var(--text); }
\t.lang-option.active { color: var(--gold); }"""

if old_lang_css in content:
    content = content.replace(old_lang_css, new_lang_css, 1)
    print("OK - CSS dropdown mis à jour")
else:
    print("ERREUR - ancien CSS lang non trouvé")

open(path, 'w').write(content)
print("✅ Fichier mis à jour !")
