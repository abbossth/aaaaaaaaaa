// Kinoteatr bron qilish. Ishlaydi, lekin... 🙈
export function b(s, t, n, d) {
  let r = 0;
  if (s) {
    if (s.length > 0) {
      if (n > 0) {
        if (n <= 10) {
          for (let i = 0; i < n; i++) {
            if (t == "adult") {
              r = r + 40000;
            } else if (t == "child") {
              r = r + 25000;
            } else if (t == "student") {
              r = r + 30000;
            } else {
              throw new Error("tur xato");
            }
          }
          // hafta oxiri
          if (d == 6 || d == 0) {
            r = r + r * 0.2;
          }
          // ko'p chipta
          if (n >= 5) {
            r = r - r * 0.1;
          }
          return { film: s, total: Math.round(r) };
        } else {
          throw new Error("ko'p");
        }
      } else {
        throw new Error("son xato");
      }
    }
  }
  throw new Error("film yo'q");
}
