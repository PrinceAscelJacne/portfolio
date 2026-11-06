DROP TABLE IF EXISTS experiences, competences, projets;

CREATE TABLE experiences (
  id SERIAL PRIMARY KEY,
  periode VARCHAR(20) NOT NULL,
  titre VARCHAR(150) NOT NULL,
  organisme VARCHAR(150) NOT NULL,
  description TEXT,
  ordre INT NOT NULL
);

CREATE TABLE competences (
  id SERIAL PRIMARY KEY,
  categorie VARCHAR(50) NOT NULL,
  nom VARCHAR(50) NOT NULL,
  ordre INT NOT NULL
);

CREATE TABLE projets (
  id SERIAL PRIMARY KEY,
  titre VARCHAR(100) NOT NULL,
  description TEXT NOT NULL,
  technologies VARCHAR(200),
  lien VARCHAR(255),
  libelle_lien VARCHAR(50),
  ordre INT NOT NULL
);

INSERT INTO experiences (periode, titre, organisme, description, ordre) VALUES
('2026 - 2028', 'Ingénieur Études & Développement (alternance)', 'Malakoff Humanis, MH TECH', 'Développement C# et automatisation des tests avec Gherkin, domaine Gestion Santé / Prévoyance / Cotisation.', 1),
('2026 - 2028', 'Mastère Manager Architecture et applications logicielles des SI', 'CESI École d''Ingénieurs, Orléans', NULL, 2),
('2026', 'Stage développeur web', 'Kery Assistance Médicale, Paris', 'Site du groupe Kery et back-office d''administration, du cahier des charges à la mise en production.', 3),
('2025 - 2026', 'Licence 3 MIAGE', 'FST, Université de Haute-Alsace, Mulhouse', NULL, 4),
('2024', 'Stage développeur web', 'ASTUS CITEE, Cotonou', 'Application de gestion documentaire et site vitrine.', 5);

INSERT INTO competences (categorie, nom, ordre) VALUES
('Langages','C#',1),('Langages','Java',2),('Langages','C++',3),('Langages','Python',4),('Langages','PHP',5),('Langages','JavaScript',6),
('Tests & qualité','Tests unitaires',7),('Tests & qualité','Gherkin',8),('Tests & qualité','PHPUnit',9),('Tests & qualité','Refactorisation',10),
('Conception & données','UML',11),('Conception & données','Merise',12),('Conception & données','PostgreSQL',13),('Conception & données','MySQL',14),
('Web & outils','Laravel',15),('Web & outils','Livewire',16),('Web & outils','Tailwind CSS',17),('Web & outils','Git',18),('Web & outils','Azure',19);

INSERT INTO projets (titre, description, technologies, lien, libelle_lien, ordre) VALUES
('Kery Group', 'Site des cinq entités du groupe avec back-office, rôles et permissions. En production.', 'Laravel,MySQL,Alpine.js', 'https://kerygroupsarl.com', 'Voir le site', 1),
('Graphe et Algorithmes', 'Visualisation de graphes, Dijkstra, Kruskal, Tarjan, ordonnancement et diagramme de Gantt.', 'Java,Swing,MVC', 'https://github.com/PrinceAscelJacne/MonProjetDeGrapheEtAlgo', 'Voir le code', 2),
('Astus Citée', 'Gestion documentaire interne par département, génération de documents Word.', 'Laravel,Livewire,PHPWord', 'https://github.com/PrinceAscelJacne/Astus-Cit-e', 'Voir le code', 3),
('GestiLoc', 'Gestion locative en ligne : biens, locataires, contrats et paiements.', 'Laravel,MySQL', 'https://gestiloc-rho.vercel.app', 'Voir la démo', 4),
('Portfolio sur Azure', 'Ce site : VM Linux Apache + PHP, données lues dans Azure Database for PostgreSQL.', 'Azure,PHP,PostgreSQL', NULL, NULL, 5);
