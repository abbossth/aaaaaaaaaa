#!/bin/bash
# "Git vaqt mashinasi" challenge uchun repo yaratadi. Git Bash'da ishga tushiring: bash challenge-setup.sh
mkdir vaqt-mashinasi && cd vaqt-mashinasi && git init -q
git config user.name "Mentor"; git config user.email "mentor@maktab.uz"
echo "<h1>Salom</h1>" > index.html; git add .; git commit -qm "Loyiha boshlandi"
echo "body{}" > style.css; git add .; git commit -qm "Stil fayli"
echo "PAROL: kosmos2026" > sir.txt; git add .; git commit -qm "Maxfiy fayl qo'shildi"
echo "console.log(1)" > app.js; git add .; git commit -qm "JS qo'shildi"
git rm -q sir.txt; git commit -qm "Maxfiy fayl o'chirildi"
git config user.name "Aziz"
echo "<h1>Salom, Dunyo!</h1>" > index.html; git commit -qam "Sarlavha o'zgardi"
git config user.name "Mentor"
git switch -qc feature/login; echo "login" > login.html; git add .; git commit -qm "Login sahifa"
git switch -q main
git switch -qc feature/dark; echo "dark" > dark.css; git add .; git commit -qm "Dark mode"
git switch -q main; git merge -q --no-edit feature/dark
echo "Tayyor! cd vaqt-mashinasi"
