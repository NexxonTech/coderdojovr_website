# CoderDojo Verona

Questa repo contiene i sorgenti del nuovo sito web ufficiale del CoderDojo di Verona (ancora in versione beta).

Il codice del CMS custom è da considerarsi open source (licenza GNU GPLv3 o successiva) mentre per testi, immagini e
altri contenuti si ritengono tutti i diritti.

## Architettura

Il sito utilizza un leggerissimo CMS custom scritto in Python che si appoggia ad AppWrite per memorizzare i contenuti.
Lo scopo finale del progetto sarebbe fare sì che ogni mentor possa contribuire alle risorse pubblicate semplicemente
caricando del Markdown in una area riservata.

Per quanto riguarda l'interfaccia in sè, questa è costruita interamente con Tailwind+DaisyUI senza partire da nessun
template preconfezionato.

## Deployment

Il progetto può essere pacchettizzato in una immagine Docker pronta da caricare sul server in cui fare il deployment;
per fare ciò, l'unica dipendenza richiesta è Nix (si veda https://nixos.org/download/):

```bash
nix build .#dockerimg
```

Per garantire il supporto a vecchi Raspberry PI o altri single-board computer con processore ARM a 32bit:

```bash
nix build .#dockerimg_armv7
```

L'immagine così prodotta (`result`) può essere caricata in Docker con il comando

```bash
docker load -i result
```

e avviata con

```bash
docker run -it -v $"/path/to/config:/var/coderdojo_config" -p 8000:8000 --rm coderdojo_portal:0.1.0
```

dopo aver salvato un file di configurazione `Settings.toml` che segue il template qui sotto nella cartella
`/path/to/config` (ovviamente popolato con le proprie informazioni):

```toml
[appwrite]
endpoint = "<AppWrite Endpoint>"
project = "<AppWrite Project>"
key = "<AppWrite Key>"
```

A oggi il sistema non esegue ancora le migrazioni necessarie, quindi è necessario ricostruire il proprio setup di
AppWrite basandosi sui sorgenti disponibili in questa repo.