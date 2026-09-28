const DISCOUNT_THRESHOLD = 500_000;
const DISCOUNT_RATE = 0.05;
const VAT_RATES = { UZ: 0.12, DEFAULT: 0.2 };

const roundMoney = (amount) => Math.round(amount * 100) / 100;

function applyDiscount(amount) {
  return amount > DISCOUNT_THRESHOLD ? amount * (1 - DISCOUNT_RATE) : amount;
}

function applyVat(amount, country) {
  const rate = VAT_RATES[country] ?? VAT_RATES.DEFAULT;
  return amount * (1 + rate);
}

function calculateItemTotal(item) {
  const subtotal = item.price * item.quantity;
  return applyVat(applyDiscount(subtotal), item.country);
}

function isValidItem(item) {
  return item.quantity > 0 && item.price > 0;
}

export function calculateCategoryTotal(items, category) {
  const total = items
    .filter((item) => item.category === category)
    .filter(isValidItem)
    .reduce((sum, item) => sum + calculateItemTotal(item), 0);
  return roundMoney(total);
}
