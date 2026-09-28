const son = Math.floor(Math.random() * 100) + 1;
const MAX_URINISH = 7;
let urinish = 0;

while (urinish < MAX_URINISH) {
  const javob = prompt(`1-100 oralig'ida son (${MAX_URINISH - urinish} urinish qoldi):`);
  if (javob === null) break;

  const taxmin = Number(javob);
  if (!Number.isInteger(taxmin)) {
    alert("Iltimos, butun son kiriting!");
    continue;
  }

  urinish++;
  if (taxmin < son) {
    alert("Kattaroq ⬆️");
  } else if (taxmin > son) {
    alert("Kichikroq ⬇️");
  } else {
    alert(`🎉 Topdingiz! ${urinish} urinishda.`);
    break;
  }

  if (urinish === MAX_URINISH) alert(`Yutqazdingiz! Son ${son} edi.`);
}
