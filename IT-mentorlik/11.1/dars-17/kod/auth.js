// 16-darsdagi todo-api'ga qo'shiladi: npm i jsonwebtoken bcrypt cors
import express from "express";
import jwt from "jsonwebtoken";
import bcrypt from "bcrypt";
import cors from "cors";

const JWT_SECRET = process.env.JWT_SECRET || "faqat-dev-uchun-sir"; // production'da .env'dan!
const users = []; // hozircha xotirada

export const authRouter = express.Router();

authRouter.post("/register", async (req, res) => {
  const { email, password } = req.body;
  if (!email?.includes("@") || !password || password.length < 8) {
    return res.status(400).json({ error: { code: "VALIDATION_ERROR", message: "Email yoki parol noto'g'ri (parol >= 8)" } });
  }
  if (users.some((u) => u.email === email)) {
    return res.status(409).json({ error: { code: "EMAIL_TAKEN", message: "Bu email band" } });
  }
  const passwordHash = await bcrypt.hash(password, 10);
  const user = { id: users.length + 1, email, passwordHash, role: "user" };
  users.push(user);
  res.status(201).json({ id: user.id, email: user.email });
});

authRouter.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const user = users.find((u) => u.email === email);
  // Qaysi biri xato ekanini aytmaymiz — xavfsizlik uchun
  if (!user || !(await bcrypt.compare(password ?? "", user.passwordHash))) {
    return res.status(401).json({ error: { code: "INVALID_CREDENTIALS", message: "Email yoki parol xato" } });
  }
  const token = jwt.sign({ userId: user.id, role: user.role }, JWT_SECRET, { expiresIn: "1h" });
  res.json({ token });
});

export function auth(req, res, next) {
  const token = req.headers.authorization?.split(" ")[1];
  if (!token) return res.status(401).json({ error: { code: "NO_TOKEN", message: "Token kerak" } });
  try {
    req.user = jwt.verify(token, JWT_SECRET);
    next();
  } catch {
    res.status(401).json({ error: { code: "INVALID_TOKEN", message: "Token yaroqsiz yoki muddati o'tgan" } });
  }
}

export function requireRole(role) {
  return (req, res, next) =>
    req.user?.role === role ? next() : res.status(403).json({ error: { code: "FORBIDDEN", message: "Ruxsat yo'q" } });
}

// app.js da ulash:
// app.use(cors({ origin: "http://localhost:5173" }));
// app.use("/auth", authRouter);
// app.use("/api/todos", auth);               // hamma todo route'lar himoyalangan
// app.get("/api/me", auth, (req, res) => res.json(req.user));
export { cors };
