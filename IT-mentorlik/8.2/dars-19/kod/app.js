const forma = document.querySelector("#forma");
const input = document.querySelector("#matn");
const royxat = document.querySelector("#royxat");
const xato = document.querySelector("#xato");
const hisob = document.querySelector("#hisob");

let todos = JSON.parse(localStorage.getItem("todos")) || [];
let filtr = "hammasi";

const save = () => localStorage.setItem("todos", JSON.stringify(todos));

function render() {
  const korinadigan = todos.filter((t) =>
    filtr === "faol" ? !t.bajarildi : filtr === "bajarilgan" ? t.bajarildi : true
  );

  royxat.innerHTML = "";
  for (const t of korinadigan) {
    const li = document.createElement("li");
    li.dataset.id = t.id;
    li.classList.toggle("bajarildi", t.bajarildi);

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "toggle";
    checkbox.checked = t.bajarildi;

    const span = document.createElement("span");
    span.className = "matn";
    span.textContent = t.matn; // textContent — XSS'dan himoya

    const del = document.createElement("button");
    del.className = "delete";
    del.textContent = "✕";

    li.append(checkbox, span, del);
    royxat.append(li);
  }

  const qolgan = todos.filter((t) => !t.bajarildi).length;
  hisob.textContent = `${qolgan} ta vazifa qoldi`;
}

forma.addEventListener("submit", (e) => {
  e.preventDefault();
  const matn = input.value.trim();
  xato.textContent = "";

  if (matn.length < 2) return (xato.textContent = "Kamida 2 ta belgi kiriting");
  if (todos.some((t) => t.matn.toLowerCase() === matn.toLowerCase())) {
    return (xato.textContent = "Bu vazifa allaqachon bor");
  }

  todos.push({ id: Date.now(), matn, bajarildi: false });
  save();
  render();
  input.value = "";
});

royxat.addEventListener("click", (e) => {
  const li = e.target.closest("li");
  if (!li) return;
  const id = Number(li.dataset.id);

  if (e.target.matches(".toggle")) {
    const t = todos.find((t) => t.id === id);
    t.bajarildi = !t.bajarildi;
  } else if (e.target.matches(".delete")) {
    todos = todos.filter((t) => t.id !== id);
  } else {
    return;
  }
  save();
  render();
});

// Ikki marta bosib tahrirlash
royxat.addEventListener("dblclick", (e) => {
  if (!e.target.matches(".matn")) return;
  const id = Number(e.target.closest("li").dataset.id);
  const t = todos.find((t) => t.id === id);
  const yangi = prompt("Tahrirlash:", t.matn)?.trim();
  if (yangi && yangi.length >= 2) {
    t.matn = yangi;
    save();
    render();
  }
});

document.querySelectorAll("[data-filtr]").forEach((btn) =>
  btn.addEventListener("click", () => {
    document.querySelector("[data-filtr].faol").classList.remove("faol");
    btn.classList.add("faol");
    filtr = btn.dataset.filtr;
    render();
  })
);

document.querySelector("#tozala").addEventListener("click", () => {
  todos = todos.filter((t) => !t.bajarildi);
  save();
  render();
});

render();
