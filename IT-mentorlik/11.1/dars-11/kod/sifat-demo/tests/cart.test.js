import { describe, it, expect } from "vitest";
import { calculateTotal, isValidPhone } from "../src/cart.js";

describe("calculateTotal", () => {
  it("bo'sh savat uchun 0", () => {
    expect(calculateTotal([])).toBe(0);
  });

  it("narx x son yig'indisi", () => {
    expect(
      calculateTotal([
        { price: 1000, qty: 3 },
        { price: 500, qty: 2 },
      ]),
    ).toBe(4000);
  });

  it("chegaradan bir so'm kam bo'lsa chegirma yo'q", () => {
    expect(calculateTotal([{ price: 499_999, qty: 1 }])).toBe(499_999);
  });

  it("chegarada 5% chegirma", () => {
    expect(calculateTotal([{ price: 500_000, qty: 1 }])).toBe(475_000);
  });

  it("massiv bo'lmasa xato", () => {
    expect(() => calculateTotal(null)).toThrow(TypeError);
  });

  it("manfiy narx xato", () => {
    expect(() => calculateTotal([{ price: -1, qty: 1 }])).toThrow(RangeError);
  });
});

describe("isValidPhone", () => {
  it.each([
    ["+998 90 123 45 67", true],
    ["998901234567", true],
    ["90 123 45 67", false],
    ["+7 900 123 45 67", false],
    ["", false],
  ])("%s -> %s", (input, expected) => {
    expect(isValidPhone(input)).toBe(expected);
  });
});
