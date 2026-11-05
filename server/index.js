import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import { handleContact } from '../lib/contact-mail.js';

// Serveur local uniquement (npm run server). En production, c'est api/contact.js sur Vercel.
const app = express();

const PORT = Number(process.env.PORT || 4000);
const FRONTEND_ORIGIN = process.env.FRONTEND_ORIGIN || 'http://localhost:4321';

app.use(cors({ origin: FRONTEND_ORIGIN }));
app.use(express.json({ limit: '1mb' }));

app.get('/api/health', (_req, res) => {
  res.json({ ok: true });
});

app.post('/api/contact', async (req, res) => {
  const { status, body } = await handleContact(req.body);
  res.status(status).json(body);
});

app.listen(PORT, () => {
  console.log(`Contact backend running on http://localhost:${PORT}`);
});
