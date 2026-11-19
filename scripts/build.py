#!/usr/bin/env python3
"""Valida i tip in tips/ e rigenera la lista nel README.

Uso:
    python scripts/build.py           valida e riscrive il README
    python scripts/build.py --check   valida soltanto (usato nelle PR)

Nessuna dipendenza esterna: basta Python 3.9+.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIPS_DIR = ROOT / "tips"
README = ROOT / "README.md"
START = "<!-- TIPS:START -->"
END = "<!-- TIPS:END -->"

# slug -> titolo mostrato nel README (l'ordine qui e' l'ordine nel README)
CATEGORIE = {
    "prompt": "Prompt",
    "coding": "Coding",
    "studio": "Studio",
    "immagini-video": "Immagini e video",
    "automazione": "Automazione",
    "altro": "Altro",
}
CAMPI = ["titolo", "tool", "categoria", "autore"]
NOME_FILE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
USERNAME = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")
MIN_TESTO = 40
MAX_TITOLO = 80


def leggi_tip(path):
    """Ritorna (dati, errori) per un file tip."""
    errori = []
    testo = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", testo, re.S)
    if not m:
        return None, ["manca l'intestazione tra le due righe '---' in cima al file"]

    dati = {}
    for riga in m.group(1).splitlines():
        if not riga.strip():
            continue
        if ":" not in riga:
            errori.append(f"riga non valida nell'intestazione: '{riga}'")
            continue
        chiave, valore = riga.split(":", 1)
        dati[chiave.strip().lower()] = valore.strip().strip("\"'")
    dati["testo"] = m.group(2).strip()

    for campo in CAMPI:
        if not dati.get(campo):
            errori.append(f"manca il campo '{campo}'")

    if not NOME_FILE.match(path.name):
        errori.append("il nome del file deve essere minuscolo con trattini, es. 'fatti-fare-le-domande.md'")
    if path.name == "tuo-tip.md":
        errori.append("rinomina il file: 'tuo-tip.md' e' il nome di esempio")

    titolo = dati.get("titolo", "")
    if "scrivi qui" in titolo.lower():
        errori.append("il titolo e' ancora quello di esempio")
    if len(titolo) > MAX_TITOLO:
        errori.append(f"titolo troppo lungo (max {MAX_TITOLO} caratteri)")

    categoria = dati.get("categoria", "")
    if categoria and categoria not in CATEGORIE:
        errori.append(f"categoria '{categoria}' non valida, scegli tra: {', '.join(CATEGORIE)}")

    autore = dati.get("autore", "").lstrip("@")
    dati["autore"] = autore
    if autore and not USERNAME.match(autore):
        errori.append("'autore' deve essere il tuo username GitHub, senza spazi")
    if autore.lower() == "tuo-username":
        errori.append("metti il tuo username GitHub in 'autore'")

    if len(dati["testo"]) < MIN_TESTO:
        errori.append(f"il testo del tip e' troppo corto (minimo {MIN_TESTO} caratteri)")
    if "spiega qui il tip" in dati["testo"].lower():
        errori.append("il testo e' ancora quello di esempio")

    return dati, errori


def cella(s):
    return s.replace("|", "\\|").replace("\n", " ")


def genera_lista(tips):
    autori = {t["autore"].lower() for t in tips}
    persone = "persona" if len(autori) == 1 else "persone"
    righe = [f"**{len(tips)} tip da {len(autori)} {persone}.**", ""]
    for slug, nome in CATEGORIE.items():
        gruppo = sorted((t for t in tips if t["categoria"] == slug), key=lambda t: t["titolo"].lower())
        if not gruppo:
            continue
        righe += [f"### {nome}", "", "| Tip | Tool | Da |", "| --- | --- | --- |"]
        for t in gruppo:
            righe.append(
                f"| [{cella(t['titolo'])}](tips/{t['file']}) | {cella(t['tool'])} "
                f"| [@{t['autore']}](https://github.com/{t['autore']}) |"
            )
        righe.append("")
    return "\n".join(righe).rstrip()


def main():
    solo_check = "--check" in sys.argv
    tips, problemi = [], 0

    for path in sorted(TIPS_DIR.glob("*")):
        if path.name.startswith("."):
            continue
        if path.is_dir() or path.suffix != ".md":
            print(f"ERRORE tips/{path.name}: in tips/ vanno solo file .md")
            problemi += 1
            continue
        dati, errori = leggi_tip(path)
        for e in errori:
            print(f"ERRORE tips/{path.name}: {e}")
        problemi += len(errori)
        if dati and not errori:
            dati["file"] = path.name
            tips.append(dati)

    if problemi:
        print(f"\n{problemi} problema/i da sistemare. Guarda CONTRIBUTING.md per il formato.")
        return 1

    print(f"OK: {len(tips)} tip validi.")
    if solo_check:
        return 0

    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        print("ERRORE: nel README mancano i marcatori TIPS:START / TIPS:END")
        return 1
    prima, resto = readme.split(START, 1)
    _, dopo = resto.split(END, 1)
    nuovo = f"{prima}{START}\n{genera_lista(tips)}\n{END}{dopo}"
    if nuovo != readme:
        README.write_text(nuovo, encoding="utf-8")
        print("README aggiornato.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
