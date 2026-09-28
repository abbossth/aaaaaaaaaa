import express from "express";
import pg from "pg";

export function createApp(pool = new pg.Pool({ connectionString: process.env.DATABASE_URL })) {
  const app = express();
  app.use(express.json());

  app.get("/api/health", async (req, res) => {
    try {
      await pool.query("SELECT 1");
      res.json({ status: "ok", db: "ok", time: new Date().toISOString() });
    } catch (err) {
      res.status(503).json({ status: "error", db: err.message });
    }
  });

  app.get("/api/items", async (req, res) => {
    const { rows } = await pool.query("SELECT id, title, created_at FROM items ORDER BY id");
    res.json(rows);
  });

  app.post("/api/items", async (req, res) => {
    const title = String(req.body.title ?? "").trim();
    if (title.length < 2) {
      return res.status(400).json({ error: { code: "VALIDATION_ERROR", message: "title >= 2" } });
    }
    const { rows } = await pool.query(
      "INSERT INTO items (title) VALUES ($1) RETURNING id, title, created_at",
      [title],
    );
    res.status(201).json(rows[0]);
  });

  return app;
}

export async function initDb(pool) {
  await pool.query(`CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
  )`);
}
