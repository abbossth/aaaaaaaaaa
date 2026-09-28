const oquvchilar = [
  { ism: "Aziz", baholar: [5, 4, 5, 5], sinf: "8.2" },
  { ism: "Malika", baholar: [5, 5, 5, 4], sinf: "8.2" },
  { ism: "Bobur", baholar: [3, 4, 3, 4], sinf: "8.2" },
  { ism: "Dilnoza", baholar: [4, 4, 5, 4], sinf: "8.2" },
  { ism: "Sardor", baholar: [3, 3, 2, 4], sinf: "8.2" },
  { ism: "Nigora", baholar: [5, 5, 5, 5], sinf: "8.2" },
];

const ortacha = (arr) => arr.reduce((s, x) => s + x, 0) / arr.length;

// 1. Har bir o'quvchining o'rtacha bahosi
const natijalar = oquvchilar.map((o) => ({ ism: o.ism, ortacha: ortacha(o.baholar) }));
console.table(natijalar);

// 2. A'lochilar (o'rtacha >= 4.75)
console.log("A'lochilar:", natijalar.filter((n) => n.ortacha >= 4.75).map((n) => n.ism));

// 3. Birinchi "3" olgan o'quvchi
console.log("Birinchi 3:", oquvchilar.find((o) => o.baholar.includes(3))?.ism);

// 4. Hech kim "2" olmaganmi?
console.log("2 yo'qmi:", oquvchilar.every((o) => !o.baholar.includes(2)));

// 5. Reyting
const reyting = [...natijalar].sort((a, b) => b.ortacha - a.ortacha);
reyting.forEach((n, i) => console.log(`${["🥇", "🥈", "🥉"][i] ?? i + 1 + "."} ${n.ism}: ${n.ortacha.toFixed(2)}`));

// 6. Sinf o'rtachasi
console.log("Sinf o'rtachasi:", ortacha(natijalar.map((n) => n.ortacha)).toFixed(2));
