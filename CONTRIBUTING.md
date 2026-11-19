# Come aggiungere un tip

Il modo più veloce è il link **Aggiungi il tuo tip** nel [README](README.md): apre il file già pronto da compilare, direttamente dal browser.

## Il formato

Un file `.md` dentro `tips/`, con questo contenuto:

```
---
titolo: Fatti fare le domande prima della risposta
tool: Qualsiasi
categoria: prompt
autore: tuo-username
---

Qui spieghi il tip: cosa fare, quando serve e, se puoi, un esempio.
```

| Campo | Cosa metterci |
| --- | --- |
| `titolo` | Il tip in una frase, massimo 80 caratteri |
| `tool` | Con cosa funziona: Claude, ChatGPT, Midjourney... oppure `Qualsiasi` |
| `categoria` | Una tra: `prompt`, `coding`, `studio`, `immagini-video`, `automazione`, `altro` |
| `autore` | Il tuo username GitHub |

Il nome del file va in minuscolo con i trattini, tipo `fatti-fare-le-domande.md`.

## Cosa rende buono un tip

- **L'hai provato tu.** Niente roba letta in giro e mai usata.
- **È specifico.** "Scrivi prompt migliori" non è un tip. "Chiedi all'AI di farti tre domande prima di rispondere" sì.
- **Uno per file.** Se ne hai tre, fai tre file.
- **Controlla che non ci sia già.** Guarda la lista nel README.

## Cosa non viene accettato

- Pubblicità, link di affiliazione, referral
- Tip per aggirare le regole dei servizi o fare danni
- Testo copiato da altri

## Dopo la pull request

Parte un controllo automatico sul formato. Se è rosso, apri i dettagli: ti dice cosa sistemare. Puoi correggere il file dalla stessa pull request, senza aprirne un'altra.
