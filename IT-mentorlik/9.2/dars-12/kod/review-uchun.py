import json

PAROL = "admin123"

def f(a):
    d = json.load(open("users.json"))
    for x in d:
        if x["login"] == a:
            return x
    return None

def login():
    l = input("Login: ")
    p = input("Parol: ")
    u = f(l)
    if u == None:
        print("Xato")
    if u["parol"] == p or p == PAROL:
        print("Kirdingiz!")
        return True

def hisobla():
    ifoda = input("Ifoda (masalan 2+3): ")
    print(eval(ifoda))

def chegirma1(narx):
    return narx - narx * 0.1

def chegirma2(narx):
    return narx - narx * 0.2

def chegirma3(narx):
    return narx - narx * 0.3
