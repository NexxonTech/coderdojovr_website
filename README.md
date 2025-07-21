# CoderDojo Verona

Questa repo contiene i sorgenti del nuovo sito web ufficiale del CoderDojo di Verona (ancora in versione beta).

Il codice del CMS basato su [Wagtail](https://wagtail.org/) è da considerarsi open source (licenza GNU GPLv3 o successiva)
mentre per testi, immagini e altri contenuti si ritengono tutti i diritti.

## Architettura

Il sito utilizza un leggerissimo CMS custom basato su Wagtail e (in produzione) si appoggia su PostgreSQL per
memorizzare i dati.
Lo scopo finale del progetto sarebbe fare sì che ogni mentor possa contribuire alle risorse pubblicate interagendo
con una semplice Area Riservata.

Per quanto riguarda il sito web in sè, questo è costruito interamente con Tailwind+DaisyUI senza partire da nessun
template preconfezionato.

## Deployment

Il progetto può essere pacchettizzato in una immagine Docker pronta da caricare sul server in cui fare il deployment;
per fare ciò, l'unica dipendenza richiesta è Nix (si veda https://nixos.org/download/):

```bash
nix build .#dockerimg
```

Oppure, per garantire il supporto a vecchi Raspberry PI o altri single-board computer con processore ARM a 32bit:

```bash
nix build .#dockerimg_armv7
```

L'immagine così prodotta (`result`) può essere caricata in Docker con il comando

```bash
docker load -i result
```

e avviata con

```bash
docker run -it -p 8000:8000 -v "/path/to/config:/etc/coderdojo_portal" -v "/path/to/media:/var/coderdojo_portal" coderdojo_portal:0.1.0
```

dopo aver salvato un file di configurazione `Settings.toml` che segue il template qui sotto nella cartella
`/path/to/config` (ovviamente popolato con le proprie informazioni):

```toml
secret_key = "<Chiave di firma dei token>"

[database]
name = "<Nome del database>"
host = "<Host del database>"
port = <Porta del database>
user = "<Utente del database>"
password = "<Password del database>"
```
