// NAMUNA YECHIM (faqat mentor uchun)
export const MAX_TICKETS = 10;
export const WEEKEND_SURCHARGE = 0.2;
export const BULK_THRESHOLD = 5;
export const BULK_DISCOUNT = 0.1;

export const TICKET_PRICES = {
  adult: 40_000,
  child: 25_000,
  student: 30_000,
};

const SATURDAY = 6;
const SUNDAY = 0;
const isWeekend = (day) => day === SATURDAY || day === SUNDAY;

function validate(film, type, count) {
  if (!film) throw new Error("film yo'q");
  if (!(count > 0)) throw new Error("son xato");
  if (count > MAX_TICKETS) throw new Error("ko'p");
  if (!(type in TICKET_PRICES)) throw new Error("tur xato");
}

export function bookTickets(film, type, count, dayOfWeek) {
  validate(film, type, count);
  let total = TICKET_PRICES[type] * count;
  if (isWeekend(dayOfWeek)) total *= 1 + WEEKEND_SURCHARGE;
  if (count >= BULK_THRESHOLD) total *= 1 - BULK_DISCOUNT;
  return { film, total: Math.round(total) };
}

export const b = bookTickets; // eski nom bilan moslik
