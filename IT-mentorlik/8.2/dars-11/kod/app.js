// 1. O'zgaruvchilar
const ism = "Aziz";
let yosh = 14;
console.log(`Salom, ${ism}! Siz ${yosh} yoshdasiz.`);

// 2. Turlar
console.log(typeof ism, typeof yosh, typeof true, typeof undefined, typeof null);

// 3. Operatorlar
console.log(10 / 3, 10 % 3, 2 ** 10);
yosh += 1;
console.log("Keyingi yil:", yosh);

// 4. Tuzoqlar
console.log("5" + 5, "5" - 5, 5 == "5", 5 === "5");
console.log(0.1 + 0.2);             // 0.30000000000000004
console.log((0.1 + 0.2).toFixed(2)); // "0.30"

// 5. Foydalanuvchi bilan muloqot
const tugilganYil = Number(prompt("Tug'ilgan yilingiz?"));
alert(`Siz 2030-yilda ${2030 - tugilganYil} yoshda bo'lasiz!`);
