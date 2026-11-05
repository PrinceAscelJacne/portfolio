import nodemailer from 'nodemailer';

// Configuration lue dans les variables d'environnement (Vercel ou .env local).
function getConfig() {
  const user = String(process.env.SMTP_USER || '').trim();
  return {
    host: process.env.SMTP_HOST || 'smtp.gmail.com',
    port: Number(process.env.SMTP_PORT || 465),
    secure: String(process.env.SMTP_SECURE || 'true').toLowerCase() === 'true',
    user,
    // Les mots de passe d'application Google s'affichent avec des espaces : on les retire.
    pass: String(process.env.SMTP_PASS || '').replace(/\s+/g, ''),
    from: String(process.env.SMTP_FROM || user).trim(),
    receiver: String(process.env.CONTACT_RECEIVER || user).trim(),
    sendConfirmation: String(process.env.CONTACT_SEND_CONFIRMATION || 'true').toLowerCase() !== 'false',
  };
}

const LIMITS = { nom: 120, email: 200, sujet: 200, message: 5000 };

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function oneLine(value) {
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

function layout(title, subtitle, body) {
  return `
<div style="margin:0;padding:24px;background:#f3eee5;font-family:Arial,sans-serif;color:#2a2016;">
  <div style="max-width:640px;margin:0 auto;background:#fbf7f0;border:1px solid rgba(131,93,52,.26);border-radius:14px;overflow:hidden;">
    <div style="padding:18px 22px;background:linear-gradient(135deg,#805531,#ab7648);color:#fff9f0;">
      <h2 style="margin:0;font-size:20px;">${title}</h2>
      <p style="margin:6px 0 0;font-size:13px;opacity:.92;">${subtitle}</p>
    </div>
    <div style="padding:20px 22px;">${body}</div>
  </div>
</div>`;
}

function ownerMail({ nom, email, sujet, message }) {
  return {
    subject: `[Portfolio] ${sujet}`,
    text: [
      'Nouveau message du formulaire de contact',
      '',
      `Nom: ${nom}`,
      `Email: ${email}`,
      `Sujet: ${sujet}`,
      '',
      'Message:',
      message,
    ].join('\n'),
    html: layout(
      'Nouveau message de contact',
      'Portfolio DJIBODE Prince Ascel Jacne',
      `
      <p style="margin:0 0 10px;"><strong>Nom :</strong> ${escapeHtml(nom)}</p>
      <p style="margin:0 0 10px;"><strong>Email :</strong> <a href="mailto:${escapeHtml(email)}">${escapeHtml(email)}</a></p>
      <p style="margin:0 0 14px;"><strong>Sujet :</strong> ${escapeHtml(sujet)}</p>
      <div style="padding:14px;background:#f0e7da;border:1px solid rgba(131,93,52,.24);border-radius:10px;white-space:pre-wrap;line-height:1.5;">${escapeHtml(message)}</div>
      <p style="margin:14px 0 0;font-size:13px;color:#6f5f50;">Clique sur « Répondre » pour écrire directement à ${escapeHtml(nom)}.</p>`
    ),
  };
}

function confirmationMail({ nom, sujet }) {
  return {
    subject: 'Confirmation de réception de votre message',
    text: [
      `Bonjour ${nom},`,
      '',
      'Votre message a bien été reçu.',
      `Sujet : ${sujet}`,
      '',
      'Je reviens vers vous rapidement.',
      '',
      '--',
      'DJIBODE Prince Ascel Jacne',
    ].join('\n'),
    html: layout(
      'Message bien reçu',
      'Merci pour votre message',
      `
      <p style="margin:0 0 10px;">Bonjour ${escapeHtml(nom)},</p>
      <p style="margin:0 0 10px;line-height:1.6;">Votre message a bien été reçu. Je vous réponds rapidement.</p>
      <p style="margin:0 0 14px;"><strong>Sujet :</strong> ${escapeHtml(sujet)}</p>
      <p style="margin:18px 0 0;">DJIBODE Prince Ascel Jacne</p>`
    ),
  };
}

/*
 * Traite une soumission du formulaire. Renvoie { status, body } pour que
 * la fonction Vercel et le serveur Express local répondent de la même façon.
 */
export async function handleContact(input) {
  const data = input && typeof input === 'object' ? input : {};

  // Champ piège invisible : les robots le remplissent, les humains non.
  if (String(data.website || '').trim()) {
    return { status: 200, body: { ok: true } };
  }

  const nom = oneLine(data.nom || '');
  const email = oneLine(data.email || '');
  const sujet = oneLine(data.sujet || '');
  const message = String(data.message || '').trim();

  if (!nom || !email || !sujet || !message) {
    return { status: 400, body: { error: 'Champs requis manquants.' } };
  }
  if (!isValidEmail(email)) {
    return { status: 400, body: { error: 'Email invalide.' } };
  }
  const fields = { nom, email, sujet, message };
  for (const [key, max] of Object.entries(LIMITS)) {
    if (fields[key].length > max) {
      return { status: 400, body: { error: `Le champ « ${key} » est trop long.` } };
    }
  }

  const config = getConfig();
  if (!config.user || !config.pass || !config.receiver) {
    console.error('Contact: variables SMTP_USER / SMTP_PASS / CONTACT_RECEIVER manquantes.');
    return { status: 500, body: { error: 'Configuration email incomplète.' } };
  }

  const transporter = nodemailer.createTransport({
    host: config.host,
    port: config.port,
    secure: config.secure,
    auth: { user: config.user, pass: config.pass },
    connectionTimeout: 8000,
    greetingTimeout: 8000,
    socketTimeout: 8000,
  });

  const from = { name: 'Portfolio Prince Ascel', address: config.from };

  try {
    await transporter.sendMail({
      from,
      to: config.receiver,
      replyTo: { name: nom, address: email },
      ...ownerMail(fields),
    });
  } catch (error) {
    console.error('Contact: envoi du message impossible:', error);
    return { status: 502, body: { error: "Envoi de l'email impossible." } };
  }

  // L'accusé de réception est un bonus : s'il échoue, le message est quand même arrivé.
  if (config.sendConfirmation) {
    try {
      await transporter.sendMail({ from, to: email, ...confirmationMail(fields) });
    } catch (error) {
      console.error('Contact: accusé de réception non envoyé:', error);
    }
  }

  return { status: 200, body: { ok: true } };
}
