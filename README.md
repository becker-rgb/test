# Website-Vorlage Malerbetrieb

Statische, responsive Website-Struktur für einen Maler-/Handwerksbetrieb – reines HTML, CSS und JavaScript, ohne Framework. Läuft auf jedem Webspace (einfach hochladen) oder auf GitHub Pages.

Alle Inhalte (Firmenname „Malermeister Mustermann“, Adresse, Telefon, Texte, Bewertungen) sind **Platzhalter**.

## Seitenstruktur

```
/
├── index.html                  Startseite
│     Hero · Leistungen · Über uns · Zahlen · Ablauf · Referenzen · Kundenstimmen · CTA
├── leistungen.html             Leistungsübersicht + FAQ
├── leistungen/
│   ├── innenraumgestaltung.html
│   ├── fassadengestaltung.html
│   ├── tapezierarbeiten.html
│   ├── waermedaemmung.html
│   ├── bodenbelaege.html
│   └── kreative-techniken.html
├── ueber-uns.html              Geschichte · Werte · Team
├── referenzen.html             Galerie mit Kategorie-Filter · Kundenstimmen
├── karriere.html               Vorteile · offene Stellen / Ausbildung
├── kontakt.html                Kontaktdaten · Bürozeiten · Anfrageformular · Karte
├── impressum.html
├── datenschutz.html
├── 404.html
├── sitemap.xml / robots.txt
├── assets/
│   ├── css/style.css           Gesamtes Styling (Farben über CSS-Variablen in :root)
│   ├── js/main.js              Mobile Navigation, Referenz-Filter, Formular-Demo
│   └── img/                    Bilder (favicon.svg, hero.jpg, …)
└── tools/build.py              Generator für alle HTML-Seiten
```

## Inhalte anpassen

Header, Navigation und Footer sind auf jeder Seite identisch. Damit Änderungen nicht in 15 Dateien einzeln gemacht werden müssen, werden alle Seiten aus `tools/build.py` erzeugt:

1. In `tools/build.py` oben Firmendaten (`FIRMA`, `TEL`, `MAIL`, `DOMAIN` …) und die Liste `LEISTUNGEN` anpassen.
2. `python3 tools/build.py` ausführen – alle HTML-Dateien, `sitemap.xml` und `robots.txt` werden neu geschrieben.

Farben und Schriften: Variablen am Anfang von `assets/css/style.css` (`--color-primary`, `--color-accent`, …).

## Noch zu erledigen vor dem Livegang

- [ ] Echte Bilder in `assets/img/` ablegen (`hero.jpg` wird im Hero-Bereich automatisch verwendet) und Platzhalter `<div class="media-placeholder">` durch `<img>` ersetzen
- [ ] Kontaktformular an ein Backend anbinden (`action` setzen, `data-demo` entfernen)
- [ ] Impressum und Datenschutzerklärung mit rechtsgültigen Texten füllen
- [ ] Karte (Google Maps / OpenStreetMap) mit Einwilligungslösung einbinden
- [ ] Echte Kundenbewertungen und Referenzen eintragen

## Lokal ansehen

`index.html` direkt im Browser öffnen oder einen lokalen Server starten:

```bash
python3 -m http.server 8000
```
