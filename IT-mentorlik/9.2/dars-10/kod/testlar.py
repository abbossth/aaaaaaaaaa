# Funksiyalarni yozing, testlarga TEGMANG!

def sozlar_soni(matn):
    """Matndagi so'zlar sonini qaytaradi."""
    pass

def eng_uzun_soz(matn):
    """Eng uzun so'zni qaytaradi (teng bo'lsa, birinchisini)."""
    pass

def unli_soni(matn):
    """a, e, i, o, u harflari sonini qaytaradi (katta-kichik farqsiz)."""
    pass

def ortacha(*sonlar):
    """O'rtacha qiymat. Son berilmasa, 0 qaytaradi."""
    pass

def baho(ball):
    """86+ -> 5, 71+ -> 4, 56+ -> 3, qolgani -> 2. 0..100 dan tashqari -> None."""
    pass

def saralash(oquvchilar):
    """[(ism, ball), ...] ni ball bo'yicha kamayish tartibida saralaydi."""
    pass


# ======= TESTLAR =======
assert sozlar_soni("Salom dunyo") == 2
assert sozlar_soni("  bir   ikki  uch ") == 3
assert eng_uzun_soz("men dasturchi bo'laman") == "dasturchi"
assert unli_soni("Salom Dunyo") == 4
assert ortacha(2, 4, 6) == 4
assert ortacha() == 0
assert baho(95) == 5 and baho(86) == 5 and baho(85) == 4 and baho(56) == 3 and baho(10) == 2
assert baho(101) is None and baho(-1) is None
assert saralash([("A", 50), ("B", 90), ("C", 70)]) == [("B", 90), ("C", 70), ("A", 50)]
print("✅ Hammasi o'tdi!")
