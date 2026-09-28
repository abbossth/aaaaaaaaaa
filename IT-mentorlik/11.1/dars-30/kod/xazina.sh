#!/bin/bash
# "Terminal xazinasi" o'yinini tayyorlaydi: bash xazina.sh
set -e
rm -rf xazina && mkdir -p xazina && cd xazina
mkdir -p orol/{shimol,janub,sharq,garb}/{g1,g2,g3} orol/.yashirin_gor
for d in orol/*/g*; do echo "Bu yerda hech narsa yo'q 🌴" > "$d/eslatma.txt"; done
echo "1-maslahat: janubga bor, 2-g'orni tekshir" > orol/xarita.txt
echo "2-maslahat: orolda YASHIRIN g'or bor. ls -la yordam beradi" > orol/janub/g2/eslatma.txt
echo "3-maslahat: kalit so'z 'KALIT' bo'lgan faylni grep bilan butun orol bo'ylab qidir" > orol/.yashirin_gor/sir.txt
for i in $(seq 1 50); do echo "tosh $i" > "orol/sharq/g3/tosh_$i.txt"; done
echo "KALIT: 4-maslahat — .sh bilan tugaydigan faylni top (find), unga bajarish ruxsatini ber va ishga tushir" > orol/sharq/g3/tosh_37.txt
cat > orol/garb/g1/sandiq.sh <<'EOF'
#!/bin/bash
echo "🎉 TABRIKLAYMAN! Xazina topildi! Mentorga ayting: KOD = LINUX-2026"
EOF
echo "O'yin tayyor! Boshlash: cd xazina && cat orol/xarita.txt"
