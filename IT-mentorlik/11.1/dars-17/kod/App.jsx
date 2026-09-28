// React (Vite): npm create vite@latest todo-web -- --template react
import { useEffect, useState } from "react";

const API = "http://localhost:3000";

export default function App() {
  const [token, setToken] = useState(() => localStorage.getItem("token"));
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");

  async function api(path, options = {}) {
    const res = await fetch(API + path, {
      ...options,
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}`, ...options.headers },
    });
    if (res.status === 401) {
      localStorage.removeItem("token");
      setToken(null);
      throw new Error("Qayta kiring");
    }
    if (!res.ok) throw new Error((await res.json()).error?.message ?? "Xato");
    return res.status === 204 ? null : res.json();
  }

  useEffect(() => {
    if (token) api("/api/todos").then((d) => setTodos(d.data)).catch((e) => setError(e.message));
  }, [token]);

  async function login(e) {
    e.preventDefault();
    const form = new FormData(e.target);
    try {
      const { token } = await api("/auth/login", { method: "POST", body: JSON.stringify(Object.fromEntries(form)) });
      localStorage.setItem("token", token);
      setToken(token);
    } catch (err) {
      setError(err.message);
    }
  }

  async function addTodo(e) {
    e.preventDefault();
    const todo = await api("/api/todos", { method: "POST", body: JSON.stringify({ title }) });
    setTodos((prev) => [...prev, todo]);
    setTitle("");
  }

  if (!token) {
    return (
      <form onSubmit={login}>
        <h1>Kirish</h1>
        <input name="email" placeholder="Email" />
        <input name="password" type="password" placeholder="Parol" />
        <button>Kirish</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    );
  }

  return (
    <main>
      <h1>Mening vazifalarim</h1>
      <form onSubmit={addTodo}>
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Yangi vazifa" />
        <button>Qo'shish</button>
      </form>
      <ul>{todos.map((t) => <li key={t.id}>{t.done ? "✅" : "⬜"} {t.title}</li>)}</ul>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </main>
  );
}
