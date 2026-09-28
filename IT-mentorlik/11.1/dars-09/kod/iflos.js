// Bu funksiya nima qiladi? 🤔
function f(d, t) {
  let r = 0;
  for (let i = 0; i < d.length; i++) {
    if (d[i].t == t) {
      if (d[i].q > 0) {
        if (d[i].p > 0) {
          let x = d[i].p * d[i].q;
          if (x > 500000) {
            x = x - x * 0.05;
          }
          if (d[i].c == "UZ") {
            x = x + x * 0.12;
          } else {
            x = x + x * 0.2;
          }
          r = r + x;
        }
      }
    }
  }
  // yaxlitlash
  r = Math.round(r * 100) / 100;
  return r;
}
