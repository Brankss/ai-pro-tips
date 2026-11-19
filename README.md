# AI Pro Tips

I trucchi che usi davvero con le AI, raccolti da chi le usa tutti i giorni. Un tip per file, scritto in due minuti, in italiano.

Niente guide da 40 pagine: solo cose concrete che ti cambiano il risultato.

## ➕ Aggiungi il tuo tip

Ti serve un account GitHub con l'email verificata. Apri i link da un browser vero (Chrome, Safari), non da dentro WhatsApp o Instagram.

1. **[Fai il fork](https://github.com/brankss/ai-pro-tips/fork)** e premi **Create fork**. È la tua copia della repo, si fa una volta sola.
2. **[Apri il tip già pronto da compilare](https://github.com/brankss/ai-pro-tips/new/main?filename=tips/tuo-tip.md&value=---%0Atitolo%3A%20Scrivi%20qui%20il%20tip%20in%20una%20frase%0Atool%3A%20Qualsiasi%0Acategoria%3A%20prompt%0Aautore%3A%20tuo-username%0A---%0A%0ASpiega%20qui%20il%20tip%3A%20cosa%20fare%2C%20quando%20serve%20e%2C%20se%20puoi%2C%20un%20esempio.%0A%0A%28categorie%20possibili%3A%20prompt%2C%20coding%2C%20studio%2C%20immagini-video%2C%20automazione%2C%20altro%29%0A)**
3. Cambia il nome del file (in alto) con un nome tuo, tipo `fatti-fare-le-domande.md`, compila i campi e scrivi il tip
4. Premi **Commit changes**, poi **Propose changes**
5. Premi **Create pull request**

Fine. Un controllo automatico ti dice se manca qualcosa. Se il link del passo 2 ti dà errore, in [CONTRIBUTING.md](CONTRIBUTING.md) c'è la strada alternativa.

## I tip

<!-- TIPS:START -->
**6 tip da 1 persona.**

### Prompt

| Tip | Tool | Da |
| --- | --- | --- |
| [Cambi argomento? Apri una chat nuova](tips/nuova-chat-nuovo-argomento.md) | Qualsiasi | [@brankss](https://github.com/brankss) |
| [Chiedi dove fa acqua, non se va bene](tips/chiedi-i-buchi-non-il-parere.md) | Qualsiasi | [@brankss](https://github.com/brankss) |
| [Fatti fare le domande prima della risposta](tips/fatti-fare-le-domande.md) | Qualsiasi | [@brankss](https://github.com/brankss) |
| [Incolla un esempio di quello che vuoi](tips/incolla-un-esempio.md) | Qualsiasi | [@brankss](https://github.com/brankss) |

### Coding

| Tip | Tool | Da |
| --- | --- | --- |
| [Fai scrivere prima i test, poi il codice](tips/prima-i-test-poi-il-codice.md) | Qualsiasi | [@brankss](https://github.com/brankss) |

### Immagini e video

| Tip | Tool | Da |
| --- | --- | --- |
| [Specifica sempre il dispositivo di ripresa](tips/specifica-il-dispositivo-di-ripresa.md) | Qualsiasi | [@brankss](https://github.com/brankss) |
<!-- TIPS:END -->

## Come funziona

Ogni file in `tips/` è un tip. A ogni merge, `scripts/build.py` rigenera la lista qui sopra. Per provarlo in locale:

```
python scripts/build.py
```

## Licenza

[MIT](LICENSE)
