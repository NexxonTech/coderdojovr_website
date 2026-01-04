# CoderDojo Verona

Questa repo contiene i sorgenti del nuovo sito web ufficiale del CoderDojo di Verona (ancora in versione beta).

Il codice utile alla compilazione e al funzionamento del sito è da considerarsi open source (licenza GNU GPLv3 o successiva)
mentre per testi, immagini e altri contenuti si ritengono tutti i diritti.

## Architettura

Il portale di CoderDojo Verona è un sito web statico compilabile con [Zola](https://www.getzola.org/), un generatore di siti
statici scritto in Rust.

La repository è organizzata in tre cartelle principali:
- `content`: contiene tutti i contenuti del sito web in formato [Markdown](https://www.markdownguide.org/), organizzati in sezioni
  e pagine secondo la struttura gerarchica del sito stesso;
- `templates`: contiene i template HTML usati da Zola per generare le pagine del sito tramite l'uso del linguaggio di templating
  [Tera](https://keats.github.io/tera/);
- `static`: contiene le risorse statiche (immagini, CSS, JS, font, ecc.) usate dal sito web.

Per quanto riguarda il design delle pagine, questo è costruito interamente con Tailwind+DaisyUI senza partire da alcun
template preconfezionato.

## Deployment

Il sito generato dal codice contenuto in questa repo è pensato per essere ospitato su GitHub Pages, quindi il deployment
avviene automaticamente ad ogni push sul branch `main` tramite GitHub Actions.

Per ottenere una copia locale del sito da installare sul proprio server, tuttavia, è sufficiente eseguire il comando:

```bash
nix build
```

una volta installato [Nix](https://nixos.org/download.html) sulla propria macchina e clonata la repository; questo si occuperà
di installare tutte le dipendenze necessarie (incluso Zola) e generare il sito web nella cartella `./result/`.

In alternativa, è sempre possibile procedere manualmente alla compilazione seguendo le seguenti istruzioni:

1. Installare [Zola](https://www.getzola.org/documentation/getting-started/installation/) sulla propria macchina;
2. Installare la [CLI di TailwindCSS](https://tailwindcss.com/docs/installation/tailwind-cli) per poter compilare i file CSS;
3. Scaricare la distribuzione [MJS di DaisyUI](https://github.com/saadeghi/daisyui/releases/tag/v5.5.14) e copiarla nella
   cartella `static/assets/styles/`;
4. Eseguire il comando `tailwindcss -m -i ./static/assets/styles/main.src.css -o ./static/assets/styles/main.min.css`
   per generare il file CSS finale usato dal sito web;
5. Eseguire il comando `zola build` per generare il sito web statico nella cartella `./public/`.

Si noti che per ospitare il sito su un dominio diverso da quello di CoderDojo Verona (es. in locale o su un server
personale) sarà necessario modificare il file `config.toml` aggiornando il campo `base_url` con l'URL corretto.
