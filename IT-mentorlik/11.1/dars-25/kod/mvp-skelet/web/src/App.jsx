import { useEffect, useState } from "react";

export default function App() {
  const [items, setItems] = useState([]);
  const [title, setTitle] = useState("");
  const [status, setStatus] = useState("⏳");
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("/api/health").then((r) => r.json()).then((d) => setStatus(d.status === "ok" ? "🟢" : "🔴")).catch(() => setStatus("🔴"));
    fetch("/api/items").then((r) => r.json()).then(setItems).catch(() => setError("API ishlamayapti"));
  }, []);

  async function add(e) {
    e.preventDefault();
    setError("");
    const res = await fetch("/api/items", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });
    const data = await res.json();
    if (!res.ok) return setError(data.error?.message ?? "Xato");
    setItems((prev) => [...prev, data]);
    setTitle("");
  }

  return (
    <main style={{ maxWidth: 600, margin: "40px auto", fontFamily: "system-ui" }}>
      <h1>🚀 Startap MVP {status}</h1>
      <form onSubmit={add} style={{ display: "flex", gap: 8 }}>
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Yangi element" style={{ flex: 1, padding: 8 }} />
        <button>Qo'shish</button>
      </form>
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      <ul>{items.map((i) => <li key={i.id}>{i.title}</li>)}</ul>
    </main>
  );
}
