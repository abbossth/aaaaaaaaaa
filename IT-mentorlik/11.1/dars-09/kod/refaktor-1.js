// 🟢 Oson: nomlarni tuzating va sehrli sonlarni konstantaga chiqaring
function calc(a, b) {
  let res = a * b;
  if (res > 1000000) {
    res = res * 0.9;
  }
  return res * 1.12;
}

function chk(s) {
  if (s.length >= 8) {
    return true;
  } else {
    return false;
  }
}
