// Mening funksiyalar kutubxonam 🧰

export const isEven = (n) => n % 2 === 0;

export function isPrime(n) {
  if (n < 2) return false;
  for (let d = 2; d * d <= n; d++) {
    if (n % d === 0) return false;
  }
  return true;
}

export const reverseString = (s) => s.split("").reverse().join("");

export const isPalindrome = (s) => {
  const clean = s.toLowerCase().replaceAll(" ", "");
  return clean === reverseString(clean);
};

export function formatPrice(sum) {
  return sum.toLocaleString("ru-RU") + " so'm"; // 1 250 000 so'm
}

export const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

export function bmi(weightKg, heightCm) {
  const h = heightCm / 100;
  const value = weightKg / (h * h);
  let category = "Normal";
  if (value < 18.5) category = "Ozg'in";
  else if (value >= 25) category = "Ortiqcha vazn";
  return { value: Number(value.toFixed(1)), category };
}
