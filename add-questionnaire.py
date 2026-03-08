path = '/Users/djibodeprinceasceljacne/princeascel/src/pages/index.astro'
content = open(path).read()

# 1. Add project in Astro data
old = """    {
title: "Astus Citée — Site vitrine","""
new = """    {
title: "Gestionnaire de questionnaires",
description: "Application en C++ permettant de gérer des questionnaires interactifs pour l'apprentissage ou l'évaluation. Prend en charge plusieurs types de questions (texte, numérique, QCM), la sauvegarde/lecture depuis un fichier texte, et propose différents modes d'évaluation (test, seconde chance, adaptatif).",
tech: ["C++"],
github: "https://github.com/PrinceAscelJacne/Questionnaire-Cpp",
placeholder: true
    },
    {
title: "Astus Citée — Site vitrine","""

if old in content:
    content = content.replace(old, new, 1)
    print("OK projet ajouté")
else:
    print("ERREUR - pattern non trouvé")

# 2. Add translation FR
old_fr = """      { title: "Astus Citée — Site vitrine", desc: "Site web vitrine développé en stage chez Astus Citée pour présenter l'entreprise et renforcer sa visibilité en ligne." }"""
new_fr = """      { title: "Gestionnaire de questionnaires", desc: "Application C++ de gestion de questionnaires interactifs : questions texte, numérique et QCM, sauvegarde en fichier texte, et trois modes d'évaluation (test, seconde chance, adaptatif)." },
      { title: "Astus Citée — Site vitrine", desc: "Site web vitrine développé en stage chez Astus Citée pour présenter l'entreprise et renforcer sa visibilité en ligne." }"""

if old_fr in content:
    content = content.replace(old_fr, new_fr, 1)
    print("OK traduction FR")
else:
    print("ERREUR traduction FR")

# 3. Add translation EN
old_en = """      { title: "Astus Citée — Showcase Website", desc: "Showcase website developed during internship at Astus Citée to present the company and strengthen its online visibility." }"""
new_en = """      { title: "Quiz Manager", desc: "C++ application for managing interactive quizzes: text, numeric and multiple-choice questions, file-based save/load, and three evaluation modes (test, second chance, adaptive)." },
      { title: "Astus Citée — Showcase Website", desc: "Showcase website developed during internship at Astus Citée to present the company and strengthen its online visibility." }"""

if old_en in content:
    content = content.replace(old_en, new_en, 1)
    print("OK traduction EN")
else:
    print("ERREUR traduction EN")

# 4. Add translation DE
old_de = """      { title: "Astus Citée — Unternehmenswebsite", desc: "Unternehmenswebsite im Praktikum bei Astus Citée entwickelt, um das Unternehmen zu präsentieren und seine Online-Sichtbarkeit zu stärken." }"""
new_de = """      { title: "Fragebogen-Manager", desc: "C++-Anwendung zur Verwaltung interaktiver Fragebögen: Text-, Zahlen- und Multiple-Choice-Fragen, Datei-Speicherung und drei Auswertungsmodi (Test, zweite Chance, adaptiv)." },
      { title: "Astus Citée — Unternehmenswebsite", desc: "Unternehmenswebsite im Praktikum bei Astus Citée entwickelt, um das Unternehmen zu präsentieren und seine Online-Sichtbarkeit zu stärken." }"""

if old_de in content:
    content = content.replace(old_de, new_de, 1)
    print("OK traduction DE")
else:
    print("ERREUR traduction DE")

open(path, 'w').write(content)
print("✅ Fichier mis à jour !")
