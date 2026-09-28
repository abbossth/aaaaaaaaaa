import { describe, it, expect, beforeEach } from "vitest";
import request from "supertest";
import { createApp } from "../src/app.js";

let app;
beforeEach(() => {
  app = createApp();
});

describe("Todo API", () => {
  it("bo'sh ro'yxat qaytaradi", async () => {
    const res = await request(app).get("/api/todos");
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ data: [], total: 0 });
  });

  it("yangi todo yaratadi (201)", async () => {
    const res = await request(app).post("/api/todos").send({ title: "Express o'rganish" });
    expect(res.status).toBe(201);
    expect(res.body).toMatchObject({ id: 1, title: "Express o'rganish", done: false });
  });

  it("noto'g'ri title uchun 400", async () => {
    const res = await request(app).post("/api/todos").send({ title: "a" });
    expect(res.status).toBe(400);
    expect(res.body.error.code).toBe("VALIDATION_ERROR");
  });

  it("mavjud bo'lmagan todo uchun 404", async () => {
    const res = await request(app).get("/api/todos/999");
    expect(res.status).toBe(404);
  });

  it("todo'ni bajarilgan deb belgilaydi va o'chiradi", async () => {
    await request(app).post("/api/todos").send({ title: "Test" });
    const patched = await request(app).patch("/api/todos/1").send({ done: true });
    expect(patched.body.done).toBe(true);
    const deleted = await request(app).delete("/api/todos/1");
    expect(deleted.status).toBe(204);
  });
});
