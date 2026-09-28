const select = document.querySelector("#shahar");
const natija = document.querySelector("#natija");

const KODLAR = {
  0: "☀️ Ochiq", 1: "🌤 Asosan ochiq", 2: "⛅ Qisman bulutli", 3: "☁️ Bulutli",
  45: "🌫 Tuman", 51: "🌦 Mayda yomg'ir", 61: "🌧 Yomg'ir", 63: "🌧 Yomg'ir", 65: "🌧 Kuchli yomg'ir",
  71: "🌨 Qor", 73: "🌨 Qor", 75: "❄️ Kuchli qor", 80: "🌦 Jala", 95: "⛈ Momaqaldiroq",
};
const tavsif = (kod) => KODLAR[kod] ?? "🌡";

async function yukla() {
  const [lat, lon] = select.value.split(",");
  const url =
    `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}` +
    `&current=temperature_2m,weather_code,wind_speed_10m` +
    `&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto`;

  natija.innerHTML = "<p>⏳ Yuklanmoqda...</p>";
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Server javobi: ${res.status}`);
    const data = await res.json();

    const kunlar = data.daily.time.slice(1, 6).map((sana, i) => `
      <div class="kun">
        <div>${new Date(sana).toLocaleDateString("uz-UZ", { weekday: "short" })}</div>
        <div>${tavsif(data.daily.weather_code[i + 1]).split(" ")[0]}</div>
        <div>${Math.round(data.daily.temperature_2m_max[i + 1])}° / ${Math.round(data.daily.temperature_2m_min[i + 1])}°</div>
      </div>`).join("");

    natija.innerHTML = `
      <div class="harorat">${Math.round(data.current.temperature_2m)}°C</div>
      <div>${tavsif(data.current.weather_code)} · 💨 ${data.current.wind_speed_10m} km/soat</div>
      <div class="kunlar">${kunlar}</div>`;
  } catch (err) {
    natija.innerHTML = `<p class="xato">❌ Ma'lumot olinmadi: ${err.message}</p>`;
  }
}

select.addEventListener("change", yukla);
yukla();
