import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import { SMTPClient } from 'smtp-client';

const app = express();

const PORT = Number(process.env.PORT || 4000);
const FRONTEND_ORIGIN = process.env.FRONTEND_ORIGIN || 'http://localhost:4321';

const SMTP_HOST = process.env.SMTP_HOST || 'smtp.gmail.com';
const SMTP_PORT = Number(process.env.SMTP_PORT || 465);
const SMTP_SECURE = String(process.env.SMTP_SECURE || 'true').toLowerCase() === 'true';
const SMTP_USER = process.env.SMTP_USER || '';
const SMTP_PASS = process.env.SMTP_PASS || '';
const SMTP_FROM = process.env.SMTP_FROM || SMTP_USER;
const CONTACT_RECEIVER = process.env.CONTACT_RECEIVER || SMTP_USER;

app.use(cors({ origin: FRONTEND_ORIGIN }));
app.use(express.json({ limit: '1mb' }));

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function escapeHeader(value) {
  return String(value).replace(/[\r\n]+/g, ' ').trim();
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function buildMime({ from, to, subject, text, html }) {
  const safeFrom = escapeHeader(from);
  const safeTo = escapeHeader(to);
  const safeSubject = escapeHeader(subject);
  const safeText = String(text).replace(/\r?\n/g, '\r\n');

  if (html) {
    return [
      `From: ${safeFrom}`,
      `To: ${safeTo}`,
      `Subject: ${safeSubject}`,
      'MIME-Version: 1.0',
      'Content-Type: text/html; charset=UTF-8',
      'Content-Transfer-Encoding: 8bit',
      '',
      String(html).replace(/\r?\n/g, '\r\n'),
    ].join('\r\n');
  }

  return [
    `From: ${safeFrom}`,
    `To: ${safeTo}`,
    `Subject: ${safeSubject}`,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
    '',
    safeText,
  ].join('\r\n');
}

async function sendEmail({ from, to, subject, text, html }) {
  const client = new SMTPClient({
    host: SMTP_HOST,
    port: SMTP_PORT,
    secure: SMTP_SECURE,
    timeout: 10_000,
  });

  try {
    await client.connect();
    await client.greet({ hostname: 'localhost' });
    await client.authPlain({ username: SMTP_USER, password: SMTP_PASS });
    await client.mail({ from });
    await client.rcpt({ to });
    await client.data(buildMime({ from, to, subject, text, html }));
    await client.quit();
  } catch (error) {
    try { await client.quit(); } catch {}
    throw error;
  }
}

app.get('/api/health', (_req, res) => {
  res.json({ ok: true });
});

app.post('/api/contact', async (req, res) => {
  const nom = String(req.body?.nom || '').trim();
  const email = String(req.body?.email || '').trim();
  const sujet = String(req.body?.sujet || '').trim();
  const message = String(req.body?.message || '').trim();

  if (!nom || !email || !sujet || !message) {
    return res.status(400).json({ error: 'Champs requis manquants.' });
  }
  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Email invalide.' });
  }
  if (!SMTP_USER || !SMTP_PASS || !CONTACT_RECEIVER || !SMTP_FROM) {
    return res.status(500).json({ error: 'Configuration SMTP incomplète.' });
  }

  const ownerSubject = `[Portfolio] ${sujet}`;
  const ownerText = [
    `Nouveau message du formulaire de contact`,
    ``,
    `Nom: ${nom}`,
    `Email: ${email}`,
    `Sujet: ${sujet}`,
    ``,
    `Message:`,
    message,
  ].join('\n');

  const ownerHtml = `
<div style="margin:0;padding:24px;background:#f3eee5;font-family:Arial,sans-serif;color:#2a2016;">
  <div style="max-width:640px;margin:0 auto;background:#fbf7f0;border:1px solid rgba(131,93,52,.26);border-radius:14px;overflow:hidden;">
    <div style="padding:18px 22px;background:linear-gradient(135deg,#805531,#ab7648);color:#fff9f0;">
      <h2 style="margin:0;font-size:20px;">Nouveau message de contact</h2>
      <p style="margin:6px 0 0;font-size:13px;opacity:.92;">Portfolio DJIBODE Prince Ascel Jacne</p>
    </div>
    <div style="padding:20px 22px;">
      <p style="margin:0 0 10px;"><strong>Nom:</strong> ${escapeHtml(nom)}</p>
      <p style="margin:0 0 10px;"><strong>Email:</strong> ${escapeHtml(email)}</p>
      <p style="margin:0 0 14px;"><strong>Sujet:</strong> ${escapeHtml(sujet)}</p>
      <div style="padding:14px;background:#f0e7da;border:1px solid rgba(131,93,52,.24);border-radius:10px;white-space:pre-wrap;line-height:1.5;">
        ${escapeHtml(message)}
      </div>
    </div>
  </div>
</div>`;

  const confirmSubject = 'Confirmation de réception de votre message';
  const confirmText = [
    `Bonjour ${nom},`,
    ``,
    `Votre message a bien été reçu.`,
    `Sujet: ${sujet}`,
    ``,
    `Je reviens vers vous rapidement.`,
    ``,
    `--`,
    'DJIBODE Prince Ascel Jacne',
  ].join('\n');

  const confirmHtml = `
<div style="margin:0;padding:24px;background:#f3eee5;font-family:Arial,sans-serif;color:#2a2016;">
  <div style="max-width:640px;margin:0 auto;background:#fbf7f0;border:1px solid rgba(131,93,52,.26);border-radius:14px;overflow:hidden;">
    <div style="padding:18px 22px;background:linear-gradient(135deg,#805531,#ab7648);color:#fff9f0;">
      <h2 style="margin:0;font-size:20px;">Message bien reçu</h2>
      <p style="margin:6px 0 0;font-size:13px;opacity:.92;">Merci pour ton message</p>
    </div>
    <div style="padding:20px 22px;">
      <p style="margin:0 0 10px;">Bonjour ${escapeHtml(nom)},</p>
      <p style="margin:0 0 10px;line-height:1.6;">Ton message a bien été reçu. Je te répondrai rapidement avec un retour clair.</p>
      <p style="margin:0 0 14px;"><strong>Sujet:</strong> ${escapeHtml(sujet)}</p>
      <div style="padding:12px;background:#f0e7da;border:1px solid rgba(131,93,52,.24);border-radius:10px;font-size:13px;color:#6f5f50;">
        Résumé envoyé depuis le formulaire du portfolio.
      </div>
      <p style="margin:18px 0 0;">DJIBODE Prince Ascel Jacne</p>
    </div>
  </div>
</div>`;

  try {
    await sendEmail({
      from: SMTP_FROM,
      to: CONTACT_RECEIVER,
      subject: ownerSubject,
      text: ownerText,
      html: ownerHtml,
    });

    await sendEmail({
      from: SMTP_FROM,
      to: email,
      subject: confirmSubject,
      text: confirmText,
      html: confirmHtml,
    });

    return res.json({ ok: true });
  } catch (error) {
    console.error('SMTP error:', error);
    return res.status(502).json({ error: 'Envoi SMTP impossible.' });
  }
});

app.listen(PORT, () => {
  console.log(`SMTP contact backend running on http://localhost:${PORT}`);
});
