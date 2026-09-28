#!/bin/bash
# Git qutqaruv holatlarini tayyorlaydi: bash qutqaruv.sh
set -e
yarat() { rm -rf "$1"; mkdir "$1"; cd "$1"; git init -q -b main; git config user.name "O'quvchi"; git config user.email "o@maktab.uz"; }

(yarat holat1; echo "<h1>Yaxshi sahifa</h1>" > index.html; git add .; git commit -qm "feat: sahifa"; echo "BUZILDI!!!" > index.html)
(yarat holat2; echo "# Loyiha" > README.md; git add .; git commit -qm "asdf")
(yarat holat3; echo 1 > a.txt; git add .; git commit -qm "feat: a"; echo 2 >> a.txt; git commit -qam "xato 1"; echo 3 >> a.txt; git commit -qam "xato 2")
(yarat holat4; echo "v1" > app.js; git add .; git commit -qm "init"; git switch -qc feature; echo "yarim ish" >> app.js)
(yarat holat5; for i in 1 2 3 4; do echo $i > f$i.txt; git add .; git commit -qm "commit $i"; done; git reset -q --hard HEAD~3)
(yarat holat6; echo "ok" > app.js; git add .; git commit -qm "feat: app"; echo "console.log(parol)" >> app.js; git commit -qam "feat: debug log (xato!)")
echo "6 ta holat tayyor: holat1 ... holat6"
