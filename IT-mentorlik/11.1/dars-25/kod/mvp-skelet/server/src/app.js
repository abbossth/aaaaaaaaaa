import express from "express";
import fs from "node:fs/promises";

const DB_FILE = new URL("../db.json", import.meta.url);

async function readDb() {
  try {
    return JSON.parse(await fs.readFile(DB_FILE, "utf-8"));
  } catch {
    return { items: [] };
  }
}

async function writeDb(db) {
  await fs.writeFile(DB_FILE, JSON.stringify(db, null, 2));
}

export function createApp() {
  const app = express();
  app.use(express.json());

  app.get("/api/health", (req, res) => res.json({ status: "ok", time: new Date().toISOString() }));

  app.get("/api/items", async (req, res) => {
    const db = await readDb();
    res.json(db.items);
  });

  app.post("/api/items", async (req, res) => {
    const title = String(req.body.title ?? "").trim();
    if (title.length < 2) return res.status(400).json({ error: { code: "VALIDATION_ERROR", message: "title >= 2" } });
    const db = await readDb();
    const item = { id: Date.now(), title, createdAt: new Date().toISOString() };
    db.items.push(item);
    await writeDb(db);
    res.status(201).json(item);
  });

  return app;
}
