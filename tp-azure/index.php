<?php
// Identifiants lus hors de la racine web
$cfg = require '/etc/portfolio/db.php';
$erreur = null;
$experiences = $competences = $projets = [];
try {
    $dsn = "pgsql:host={$cfg['host']};port={$cfg['port']};dbname={$cfg['dbname']};sslmode=require";
    $pdo = new PDO($dsn, $cfg['user'], $cfg['password'], [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    $experiences = $pdo->query("SELECT * FROM experiences ORDER BY ordre")->fetchAll(PDO::FETCH_ASSOC);
    foreach ($pdo->query("SELECT categorie, nom FROM competences ORDER BY ordre") as $c) {
        $competences[$c['categorie']][] = $c['nom'];
    }
    $projets = $pdo->query("SELECT * FROM projets ORDER BY ordre")->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    error_log($e->getMessage());
    $erreur = "Connexion à la base de données impossible.";
}
function e($t) { return htmlspecialchars((string)$t, ENT_QUOTES, 'UTF-8'); }
?>
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Prince Ascel DJIBODE | Ingénieur Études &amp; Développement</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#1f2937;line-height:1.6;background:#fff}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
nav{position:sticky;top:0;z-index:10;background:rgba(15,42,68,.97);border-bottom:1px solid #1e4a72}
nav .wrap{display:flex;justify-content:space-between;align-items:center;height:64px}
.logo{color:#fff;font-weight:700;font-size:1.1rem;letter-spacing:.02em}.logo span{color:#5fa8e8}
nav ul{display:flex;gap:26px;list-style:none}
nav ul a{color:#c9d6e3;font-size:.92rem}nav ul a:hover{color:#fff}
.hero{background:linear-gradient(135deg,#0f2a44 0%,#16395c 60%,#1e4a72 100%);color:#fff;padding:110px 0 120px}
.tag{display:inline-block;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:#8fc4f2;border:1px solid #2f5f8c;padding:5px 12px;border-radius:999px;margin-bottom:22px}
.hero h1{font-size:3rem;line-height:1.15;font-weight:700;margin-bottom:14px}
.hero h1 span{color:#5fa8e8}
.hero p{font-size:1.15rem;color:#c9d6e3;max-width:620px;margin-bottom:34px}
.btn{display:inline-block;padding:12px 26px;border-radius:6px;font-weight:600;font-size:.95rem;margin-right:12px}
.btn-primary{background:#3b8fd9;color:#fff}.btn-primary:hover{background:#2f7cc0}
.btn-ghost{border:1px solid #5f86ad;color:#fff}.btn-ghost:hover{background:rgba(255,255,255,.08)}
section{padding:80px 0}
section.alt{background:#f4f7fa}
h2{font-size:1.9rem;color:#0f2a44;margin-bottom:8px}
.sub{color:#6b7280;margin-bottom:40px}
.about{display:grid;grid-template-columns:1.4fr 1fr;gap:40px;align-items:start}
.about p{color:#374151;margin-bottom:14px}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.stat{background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:20px;text-align:center}
.stat b{display:block;font-size:1.7rem;color:#1e4a72}.stat span{font-size:.85rem;color:#6b7280}
.timeline{border-left:2px solid #c8d6e5;padding-left:28px}
.job{position:relative;margin-bottom:34px}
.job:before{content:'';position:absolute;left:-36px;top:6px;width:14px;height:14px;border-radius:50%;background:#3b8fd9;border:3px solid #f4f7fa}
.job small{color:#3b8fd9;font-weight:600;font-size:.82rem;letter-spacing:.04em}
.job h3{font-size:1.1rem;color:#111827}.job .org{color:#1e4a72;font-weight:500;font-size:.95rem}
.job p{color:#4b5563;font-size:.93rem;margin-top:4px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:26px;transition:.2s}
.card:hover{box-shadow:0 12px 28px rgba(15,42,68,.1);transform:translateY(-3px)}
.card h3{color:#0f2a44;font-size:1.05rem;margin-bottom:10px}
.card p{color:#4b5563;font-size:.92rem}
.chips{margin-top:14px}
.chips span{display:inline-block;font-size:.78rem;background:#e8f1fa;color:#1e4a72;padding:3px 10px;border-radius:999px;margin:0 6px 6px 0}
.card a{display:inline-block;margin-top:12px;color:#3b8fd9;font-weight:600;font-size:.9rem}
.contact{text-align:center}
.contact p{color:#4b5563;max-width:560px;margin:0 auto 30px}
.contact .btn-ghost{color:#0f2a44;border-color:#0f2a44}
footer{background:#0f2a44;color:#9fb3c8;font-size:.85rem;padding:26px 0}
footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
@media(max-width:760px){nav ul{display:none}.hero{padding:70px 0 80px}.hero h1{font-size:2.1rem}.about{grid-template-columns:1fr}section{padding:60px 0}}
.db{display:inline-block;margin-top:10px;font-size:.8rem;padding:4px 10px;border-radius:999px;background:#e8f5ec;color:#1d6b3a}
.db.ko{background:#fdecec;color:#a12626}
</style>
</head>
<body>
<nav><div class="wrap">
<a href="#accueil" class="logo">Prince<span>.</span>Ascel</a>
<ul><li><a href="#apropos">À propos</a></li><li><a href="#experience">Expérience</a></li><li><a href="#competences">Compétences</a></li><li><a href="#projets">Projets</a></li><li><a href="#contact">Contact</a></li></ul>
</div></nav>

<header class="hero" id="accueil"><div class="wrap">
<span class="tag">Ingénieur Études &amp; Développement</span>
<h1>Bonjour, je suis<br><span>Prince Ascel DJIBODE</span></h1>
<p>Je conçois et développe des applications métier en C#, avec une attention particulière à l'automatisation des tests et à la qualité logicielle.</p>
<a href="#projets" class="btn btn-primary">Voir mes projets</a>
<a href="#contact" class="btn btn-ghost">Me contacter</a>
</div></header>


<section id="experience" class="alt"><div class="wrap">
<h2>Expérience &amp; formation</h2>
<p class="sub">Données lues dans la table <code>experiences</code></p>
<div class="timeline">
<?php foreach ($experiences as $x): ?>
<div class="job"><small><?= e($x['periode']) ?></small><h3><?= e($x['titre']) ?></h3><div class="org"><?= e($x['organisme']) ?></div><?php if ($x['description']): ?><p><?= e($x['description']) ?></p><?php endif; ?></div>
<?php endforeach; ?>
</div>
</div></section>

<section id="competences"><div class="wrap">
<h2>Compétences</h2>
<p class="sub">Données lues dans la table <code>competences</code></p>
<div class="grid">
<?php foreach ($competences as $cat => $noms): ?>
<div class="card"><h3><?= e($cat) ?></h3><div class="chips"><?php foreach ($noms as $n): ?><span><?= e($n) ?></span><?php endforeach; ?></div></div>
<?php endforeach; ?>
</div>
</div></section>

<section id="projets" class="alt"><div class="wrap">
<h2>Projets</h2>
<p class="sub">Données lues dans la table <code>projets</code></p>
<div class="grid">
<?php foreach ($projets as $p): ?>
<div class="card"><h3><?= e($p['titre']) ?></h3><p><?= e($p['description']) ?></p>
<div class="chips"><?php foreach (array_filter(explode(',', (string)$p['technologies'])) as $t): ?><span><?= e(trim($t)) ?></span><?php endforeach; ?></div>
<?php if ($p['lien']): ?><a href="<?= e($p['lien']) ?>"><?= e($p['libelle_lien']) ?></a><?php endif; ?></div>
<?php endforeach; ?>
</div>
</div></section>

<section id="contact" class="contact"><div class="wrap">
<h2>Contact</h2>
<p>Un projet, une question ou une opportunité ? Écrivez-moi, je réponds rapidement.</p>
<a href="mailto:djibodeprinceascel@gmail.com" class="btn btn-primary">M'écrire un e-mail</a>
<a href="https://github.com/PrinceAscelJacne" class="btn btn-ghost">Mon GitHub</a>
</div></section>

<footer><div class="wrap">
<span>© 2026 Prince Ascel DJIBODE</span>
<span>Hébergé sur une VM Microsoft Azure<br>
<?php if ($erreur): ?><span class="db ko"><?= e($erreur) ?></span>
<?php else: ?><span class="db">Données chargées depuis Azure Database for PostgreSQL</span><?php endif; ?></span>
</div></footer>
</body>
</html>
