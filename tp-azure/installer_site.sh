#!/bin/bash
# Installe le site PHP relié à Azure Database for PostgreSQL sur la VM (Ubuntu + Apache).
# Usage : bash installer_site.sh
set -e
BASE=https://raw.githubusercontent.com/PrinceAscelJacne/portfolio/claude/project-thread-feigon/tp-azure

echo "== 1/5 Installation de PHP, php-pgsql et psql =="
sudo apt-get update -q
sudo apt-get install -y -q php libapache2-mod-php php-pgsql postgresql-client
sudo systemctl restart apache2

echo "== 2/5 Identifiants de la base =="
read -p "Nom du serveur PostgreSQL [baseprince] : " PGSRV; PGSRV=${PGSRV:-baseprince}
read -p "Utilisateur administrateur de la base : " PGU
read -s -p "Mot de passe (rien ne s'affiche, c'est normal) : " PGPW; echo
PGH="$PGSRV.postgres.database.azure.com"
PW_PHP=$(printf '%s' "$PGPW" | sed -e 's/\\/\\\\/g' -e "s/'/\\\\'/g")

# Fichier lu par la page PHP, hors de la racine web
sudo mkdir -p /etc/portfolio
printf "<?php\nreturn [\n  'host' => '%s',\n  'port' => 5432,\n  'dbname' => 'portfolio',\n  'user' => '%s',\n  'password' => '%s',\n];\n" "$PGH" "$PGU" "$PW_PHP" | sudo tee /etc/portfolio/db.php > /dev/null
sudo chown root:www-data /etc/portfolio/db.php
sudo chmod 640 /etc/portfolio/db.php

# Raccourci pour psql : psql service=portfolio
printf "[portfolio]\nhost=%s\nport=5432\nuser=%s\ndbname=postgres\nsslmode=require\n" "$PGH" "$PGU" > ~/.pg_service.conf
printf "%s:5432:*:%s:%s\n" "$PGH" "$PGU" "$PGPW" > ~/.pgpass
chmod 600 ~/.pgpass ~/.pg_service.conf

echo "== 3/5 Test de connexion =="
psql service=portfolio -c "SELECT version();"

echo "== 4/5 Création de la base, des tables et des données =="
psql service=portfolio -tc "SELECT 1 FROM pg_database WHERE datname='portfolio'" | grep -q 1 \
  || psql service=portfolio -c "CREATE DATABASE portfolio;"
curl -fsSL "$BASE/portfolio.sql" -o ~/portfolio.sql
psql "service=portfolio dbname=portfolio" -q -v ON_ERROR_STOP=1 -f ~/portfolio.sql
psql "service=portfolio dbname=portfolio" -c "SELECT (SELECT count(*) FROM experiences) AS experiences, (SELECT count(*) FROM competences) AS competences, (SELECT count(*) FROM projets) AS projets;"

echo "== 5/5 Mise en place de la page PHP =="
if [ -f /var/www/html/index.html ]; then sudo mv /var/www/html/index.html /var/www/html/index_statique.html; fi
sudo curl -fsSL "$BASE/index.php" -o /var/www/html/index.php
php -l /var/www/html/index.php
curl -s http://localhost | grep -o "Données chargées[^<]*\|Connexion à la base[^<]*"
echo "Terminé : ouvrez http://nprince sur votre Mac."
