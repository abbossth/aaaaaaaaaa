# GitHub Flow demo
git switch main && git pull
git switch -c feature/team-cards

# ... team.html ga kartochkalar qo'shiladi ...
git add team.html
git commit -m "feat(team): add member cards layout"

# ... style.css ga stil ...
git add style.css
git commit -m "style(team): add card hover effect"

# ... README yangilanadi ...
git add README.md
git commit -m "docs: add team section to README"

git push -u origin feature/team-cards
# GitHub'da "Compare & pull request" tugmasi paydo bo'ladi -> 6-dars
