#!/bin/bash
# Loyiha papkasining zaxira nusxasini (backup) yaratadi.
# Foydalanish: ./backup.sh <papka> [saqlash_joyi]
set -euo pipefail

MANBA=${1:?"Foydalanish: $0 <papka> [saqlash_joyi]"}
MANZIL=${2:-"$HOME/backups"}
VAQT=$(date +%Y-%m-%d_%H-%M)
NOM="$(basename "$MANBA")_$VAQT.tar.gz"

if [ ! -d "$MANBA" ]; then
  echo "❌ Papka topilmadi: $MANBA"
  exit 1
fi

mkdir -p "$MANZIL"
tar --exclude='.venv' --exclude='__pycache__' --exclude='.env' -czf "$MANZIL/$NOM" -C "$(dirname "$MANBA")" "$(basename "$MANBA")"
echo "✅ Backup: $MANZIL/$NOM ($(du -h "$MANZIL/$NOM" | cut -f1))"

# Faqat oxirgi 5 ta backup qolsin
ls -1t "$MANZIL"/*.tar.gz | tail -n +6 | xargs -r rm --
echo "📦 Jami backuplar: $(ls -1 "$MANZIL"/*.tar.gz | wc -l)"
