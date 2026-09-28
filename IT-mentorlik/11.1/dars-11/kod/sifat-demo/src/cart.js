export const DISCOUNT_THRESHOLD = 500_000;
export const DISCOUNT_RATE = 0.05;

export function calculateTotal(items) {
  if (!Array.isArray(items)) throw new TypeError("items massiv bo'lishi kerak");
  const subtotal = items.reduce((sum, item) => {
    if (item.price < 0 || item.qty < 0) throw new RangeError("Narx va son manfiy bo'lmaydi");
    return sum + item.price * item.qty;
  }, 0);
  return subtotal >= DISCOUNT_THRESHOLD ? subtotal * (1 - DISCOUNT_RATE) : subtotal;
}

export function isValidPhone(phone) {
  const digits = String(phone).replace(/\D/g, "");
  return digits.length === 12 && digits.startsWith("998");
}
