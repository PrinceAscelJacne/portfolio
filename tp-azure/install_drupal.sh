#!/bin/bash
# TP Azure - Exercice 2 : installe Drupal sur la VM existante (tpazurePrince)
# et le relie à la base PostgreSQL Azure (baseprince).
# Usage, sur la VM : bash install_drupal.sh   (on peut le relancer sans risque)
set -e
if ! command -v apt-get >/dev/null 2>&1 || [ "$(uname -s)" != "Linux" ]; then
  echo "Ce script doit être lancé sur la VM Azure, pas sur votre Mac."
  echo "Connectez-vous d'abord : ssh nprince"
  exit 1
fi
if [ ! -f ~/.pg_service.conf ]; then
  echo "Fichier ~/.pg_service.conf introuvable : relancez d'abord installer_site.sh (exercice 1)."
  exit 1
fi
PGH=$(grep '^host=' ~/.pg_service.conf | cut -d= -f2)
WEB=/var/www/html/drupal

echo "== 1/6 Paquets Apache / PHP pour Drupal =="
sudo apt-get update -q
sudo apt-get install -y -q apache2 php libapache2-mod-php php-cli php-mbstring php-xml \
  php-zip php-gd php-curl php-pgsql php-opcache unzip wget netcat-openbsd postgresql-client
php -v | head -1

echo "== 2/6 Téléchargement de Drupal =="
if [ ! -f "$WEB/index.php" ]; then
  cd /tmp
  wget -q https://www.drupal.org/download-latest/tar.gz -O drupal-latest.tar.gz
  tar xzf drupal-latest.tar.gz
  sudo rm -rf "$WEB"
  sudo mv /tmp/drupal-1*/ "$WEB"
  rm -f drupal-latest.tar.gz
else
  echo "Drupal déjà présent dans $WEB, on garde."
fi
sudo mkdir -p "$WEB/sites/default/files"
[ -f "$WEB/sites/default/settings.php" ] || sudo cp "$WEB/sites/default/default.settings.php" "$WEB/sites/default/settings.php"
sudo chown -R www-data:www-data "$WEB"
sudo chmod -R 755 "$WEB"
grep -o "VERSION = '[^']*'" "$WEB/core/lib/Drupal.php" || true

echo "== 3/6 Configuration d'Apache (drupal-leo.conf) =="
sudo tee /etc/apache2/sites-available/drupal-leo.conf > /dev/null <<'CONF'
# Le site est servi à l'adresse http://<IP-Publique-VM>/drupal
<Directory /var/www/html/drupal>
  AllowOverride All
  Require all granted
</Directory>

<VirtualHost *:80>
  ServerName drupal-leo.azure.com
  DocumentRoot /var/www/html/drupal
</VirtualHost>
CONF
sudo a2enmod -q rewrite
sudo a2ensite -q drupal-leo.conf
sudo apache2ctl configtest
sudo systemctl reload apache2

echo "== 4/6 Base 'drupal' et utilisateur 'drupaluser' sur $PGH =="
read -s -p "Choisissez un mot de passe pour drupaluser (rien ne s'affiche) : " DPW; echo
if psql service=portfolio -tAc "SELECT 1 FROM pg_roles WHERE rolname='drupaluser'" | grep -q 1; then
  psql service=portfolio -q -v pw="$DPW" <<'SQL'
ALTER USER drupaluser WITH PASSWORD :'pw';
SQL
else
  psql service=portfolio -q -v pw="$DPW" <<'SQL'
CREATE USER drupaluser WITH PASSWORD :'pw';
SQL
fi
psql service=portfolio -tAc "SELECT 1 FROM pg_database WHERE datname='drupal'" | grep -q 1 \
  || psql service=portfolio -c "CREATE DATABASE drupal;"
psql "service=portfolio dbname=drupal" -q -c "GRANT ALL PRIVILEGES ON DATABASE drupal TO drupaluser;" \
  -c "GRANT ALL ON SCHEMA public TO drupaluser;"
# Drupal 11 exige l'extension pg_trgm
if ! psql "service=portfolio dbname=drupal" -q -c "CREATE EXTENSION IF NOT EXISTS pg_trgm;"; then
  echo
  echo "!! Azure bloque l'extension pg_trgm. Dans Azure Cloud Shell, tapez :"
  echo "   az postgres flexible-server parameter set -g basePrince -s baseprince -n azure.extensions -v PG_TRGM"
  echo "   puis relancez : bash install_drupal.sh"
  exit 1
fi

echo "== 5/6 Test de communication VM -> base PostgreSQL =="
echo "(Azure ne répond pas au ping : on teste le port 5432 à la place)"
nc -zv -w 5 "$PGH" 5432
PGPASSWORD="$DPW" psql "host=$PGH port=5432 dbname=drupal user=drupaluser sslmode=require" \
  -c "SELECT current_user, current_database(), inet_server_addr() AS ip_base;"

echo "== 6/6 Vérification de la page d'installation =="
CODE=$(curl -s -o /dev/null -w '%{http_code}' -L http://localhost/drupal/)
echo "Réponse HTTP de http://localhost/drupal/ : $CODE"
IP=$(curl -s -4 ifconfig.me || echo 68.221.26.250)
echo
echo "Terminé. Ouvrez http://$IP/drupal sur votre Mac et suivez l'assistant."
echo "Base de données : PostgreSQL | nom : drupal | utilisateur : drupaluser"
echo "Options avancées > Hôte : $PGH | Port : 5432"
