import express from "express";

export function createApp() {
  const app = express();
  app.use(express.json());

  // Oddiy logger middleware
  app.use((req, res, next) => {
    const start = Date.now();
    res.on("finish", () => console.log(`${req.method} ${req.originalUrl} ${res.statusCode} ${Date.now() - start}ms`));
    next();
  });

  // Hozircha xotirada (keyinroq — PostgreSQL)
  let todos = [];
  let nextId = 1;

  const httpError = (status, code, message) => Object.assign(new Error(message), { status, code });

  const findTodo = (id) => {
    const todo = todos.find((t) => t.id === Number(id));
    if (!todo) throw httpError(404, "NOT_FOUND", `Todo #${id} topilmadi`);
    return todo;
  };

  const validateTitle = (title) => {
    if (typeof title !== "string" || title.trim().length < 2) {
      throw httpError(400, "VALIDATION_ERROR", "title kamida 2 belgidan iborat satr bo'lishi kerak");
    }
    return title.trim();
  };

  app.get("/api/todos", (req, res) => {
    let result = todos;
    if (req.query.done !== undefined) result = result.filter((t) => t.done === (req.query.done === "true"));
    res.json({ data: result, total: result.length });
  });

  app.get("/api/todos/:id", (req, res) => {
    res.json(findTodo(req.params.id));
  });

  app.post("/api/todos", (req, res) => {
    const todo = { id: nextId++, title: validateTitle(req.body.title), done: false, createdAt: new Date().toISOString() };
    todos.push(todo);
    res.status(201).json(todo);
  });

  app.patch("/api/todos/:id", (req, res) => {
    const todo = findTodo(req.params.id);
    if (req.body.title !== undefined) todo.title = validateTitle(req.body.title);
    if (req.body.done !== undefined) todo.done = Boolean(req.body.done);
    res.json(todo);
  });

  app.delete("/api/todos/:id", (req, res) => {
    findTodo(req.params.id);
    todos = todos.filter((t) => t.id !== Number(req.params.id));
    res.status(204).end();
  });

  // 404 — hech bir route mos kelmasa
  app.use((req, res) => {
    res.status(404).json({ error: { code: "ROUTE_NOT_FOUND", message: `${req.method} ${req.path} mavjud emas` } });
  });

  // Yagona xato ishlovchisi
  app.use((err, req, res, next) => {
    const status = err.status || 500;
    res.status(status).json({ error: { code: err.code || "INTERNAL_ERROR", message: status === 500 ? "Server xatosi" : err.message } });
  });

  return app;
}
