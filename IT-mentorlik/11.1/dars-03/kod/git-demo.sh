# Mentor ekranda bosqichma-bosqich ko'rsatadi
mkdir git-demo && cd git-demo
git init
echo "# Mening loyiham" > README.md
git status                     # qizil: untracked
git add README.md
git status                     # yashil: staged
git commit -m "docs: README qo'shildi"
git log --oneline

git switch -c feature/salom    # yangi branch
echo "console.log('Salom!')" > app.js
git add . && git commit -m "feat: salom skripti"
git switch main                # app.js "yo'qoldi"!
ls
git merge feature/salom        # qaytdi!
ls
git log --oneline --graph --all
