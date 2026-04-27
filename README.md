# Spustenie projektu (verzia v1.0)

Tento návod Vás prevedie celým procesom – od stiahnutia projektu až po jeho spustenie.

---

## 1. Stiahnutie release verzie z GitHubu

1. Prejdite na GitHub repozitár projektu
2. Kliknite na sekciu **Releases** (na pravej strane alebo v hornej lište)
3. Nájdite verziu **v1.0**
4. Stiahnite súbor:

   * najčastejšie **Source code (ZIP)**
5. Po stiahnutí:

   * rozbaľte ZIP súbor do priečinka vo Vašom počítači

---

## 2. Inštalácia Pythonu

Ak ešte nemáte Python:

1. Prejdite na oficiálnu stránku: https://www.python.org/downloads/
2. Stiahnite najnovšiu verziu Pythonu
3. Pri inštalácii:

   * ✅ zaškrtnite možnosť **"Add Python to PATH"**
4. Dokončite inštaláciu

### Overenie inštalácie

Otvorte terminál (CMD / PowerShell) a zadajte:

```
python --version
```

Ak sa zobrazí verzia (napr. `Python 3.x.x`), inštalácia prebehla správne.

---

## 3. Inštalácia knižnice Pygame

V termináli spustite:

```
pip install pygame
```

Počkajte, kým sa inštalácia dokončí.

---

## 4. Spustenie projektu

1. V termináli sa presuňte do priečinka projektu:

```
cd cesta/k/vasmu/priecinku
```

2. Spustite hlavný súbor (napr.):

```
python main.py
```

---

## Hotovo

Ak všetko prebehlo správne, projekt by sa mal spustiť 🎮

---

## Časté problémy

**Python nefunguje:**

* Skontrolujte, či ste zaškrtli *Add to PATH*

**pip nefunguje:**

* Skúste:

```
python -m pip install pygame
```

**Chyba pri spustení:**

* Uistite sa, že ste v správnom priečinku
* Skontrolujte názov súboru (napr. `main.py`)

---

Ak sa vyskytne problém, najčastejšie ide o jednu z týchto príčin:

* Python nie je správne nainštalovaný
* Pygame nie je nainštalovaný
* Projekt spúšťate z nesprávneho priečinka
