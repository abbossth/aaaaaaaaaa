import { describe, it, expect } from "vitest";
import { b } from "../src/booking.js";

// Namuna test. Kamida 6 ta o'zingiznikini yozing!
describe("booking", () => {
  it("2 ta kattalar chiptasi, dushanba", () => {
    expect(b("Avatar", "adult", 2, 1)).toEqual({ film: "Avatar", total: 80000 });
  });
});
