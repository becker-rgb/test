#!/usr/bin/env python3
"""Erzeugt die statischen HTML-Seiten (gemeinsamer Header/Footer)."""
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIRMA = "Malermeister Mustermann"
INHABER = "Max Mustermann"
STRASSE = "Musterstraße 1"
ORT = "01234 Musterstadt"
TEL = "0123 456789"
TEL_LINK = "+49123456789"
MAIL = "info@malermeister-mustermann.de"
DOMAIN = "https://www.malermeister-mustermann.de"


def icon(name, size=28):
    paths = {
        "brush": '<path d="M18 2l4 4-9.5 9.5-4-4z"/><path d="M8.5 11.5C6 11.5 4 13.5 4 16c0 2-2 3-2 3s3 2 6 2c2.5 0 4.5-2 4.5-4.5"/>',
        "house": '<path d="M3 11l9-8 9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
        "roll": '<rect x="3" y="3" width="15" height="6" rx="1"/><path d="M18 6h3v5h-9v3"/><rect x="10" y="14" width="4" height="7" rx="1"/>',
        "layers": '<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 12l10 5 10-5"/><path d="M2 17l10 5 10-5"/>',
        "floor": '<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 9h18M3 15h18M9 3v6M15 9v6M9 15v6"/>',
        "spark": '<path d="M12 2v4M12 18v4M2 12h4M18 12h4M5 5l3 3M16 16l3 3M5 19l3-3M16 8l3-3"/>',
        "check": '<circle cx="12" cy="12" r="10"/><path d="M7 12l3.5 3.5L17 9"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
        "pin": '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')


LEISTUNGEN = [
    {
        "slug": "innenraumgestaltung", "icon": "brush", "titel": "Innenraumgestaltung",
        "kurz": "Wände und Decken streichen, Farbberatung und Lackierarbeiten für Wohn- und Geschäftsräume.",
        "intro": "Ob frischer Anstrich, neues Farbkonzept oder hochwertige Lackierung – wir gestalten Ihre Räume sauber, termingerecht und mit Liebe zum Detail.",
        "punkte": ["Wand- und Deckenanstriche", "Individuelle Farbberatung", "Lackierarbeiten an Türen, Fenstern & Heizkörpern", "Schimmelsanierung", "Abdeck- und Schutzarbeiten inklusive"],
    },
    {
        "slug": "fassadengestaltung", "icon": "house", "titel": "Fassadengestaltung",
        "kurz": "Fassadenanstrich, Putzsanierung und Reinigung – für ein gepflegtes und geschütztes Zuhause.",
        "intro": "Die Fassade ist die Visitenkarte Ihres Hauses. Wir sanieren, schützen und gestalten sie dauerhaft – inklusive Gerüststellung und Untergrundprüfung.",
        "punkte": ["Fassadenreinigung & -anstrich", "Putzausbesserung und Rissanierung", "Algen- und Pilzbehandlung", "Farbgestaltung & Bemusterung", "Sockel- und Balkonbeschichtung"],
    },
    {
        "slug": "tapezierarbeiten", "icon": "roll", "titel": "Tapezierarbeiten",
        "kurz": "Raufaser, Vlies, Mustertapeten oder Glasgewebe – fachgerecht verarbeitet.",
        "intro": "Von klassischer Raufaser bis zur exklusiven Designtapete: Wir bereiten den Untergrund sorgfältig vor und sorgen für ein perfektes Ergebnis ohne sichtbare Nähte.",
        "punkte": ["Entfernen alter Tapeten", "Untergrundvorbereitung & Spachteln", "Vlies-, Raufaser- und Designtapeten", "Glasgewebe und Renoviervlies", "Fototapeten und Akzentwände"],
    },
    {
        "slug": "waermedaemmung", "icon": "layers", "titel": "Wärmedämmung",
        "kurz": "Wärmedämmverbundsysteme (WDVS) zur Senkung Ihrer Energiekosten.",
        "intro": "Mit einem Wärmedämmverbundsystem senken Sie Heizkosten, steigern den Wohnkomfort und den Wert Ihrer Immobilie. Wir beraten Sie auch zu Fördermöglichkeiten.",
        "punkte": ["Planung & Beratung zu WDVS", "Mineralwolle- und EPS-Dämmung", "Armierung und Oberputz", "Sockel- und Perimeterdämmung", "Hinweise zu Förderprogrammen"],
    },
    {
        "slug": "bodenbelaege", "icon": "floor", "titel": "Bodenbeläge",
        "kurz": "Vinyl, Laminat, Teppich und Designbeläge – verlegt mit sauberem Abschluss.",
        "intro": "Wir verlegen Bodenbeläge passend zu Ihrem Raumkonzept – inklusive Untergrundvorbereitung, Ausgleichsmasse und Sockelleisten.",
        "punkte": ["Vinyl- und Designbeläge", "Laminat und Klick-Parkett", "Teppichböden", "Ausgleichen & Spachteln des Untergrunds", "Sockelleisten & Übergangsprofile"],
    },
    {
        "slug": "kreative-techniken", "icon": "spark", "titel": "Kreative Techniken",
        "kurz": "Spachteltechniken, Kalkputze, Lasuren und Effektbeschichtungen.",
        "intro": "Für besondere Räume: Mit Spachtel-, Wisch- und Lasurtechniken entstehen einzigartige Oberflächen mit Charakter.",
        "punkte": ["Spachtel- und Glättetechniken", "Kalk- und Lehmputze", "Lasur- und Wischtechniken", "Beton- und Metalloptik", "Dekorative Akzentflächen"],
    },
]

NAV = [
    ("Startseite", "index.html"),
    ("Leistungen", "leistungen.html"),
    ("Über uns", "ueber-uns.html"),
    ("Referenzen", "referenzen.html"),
    ("Karriere", "karriere.html"),
]


def header(root, active):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if href == active else ""
        if href == "leistungen.html":
            sub = "".join(f'<li><a href="{root}leistungen/{l["slug"]}.html">{l["titel"]}</a></li>' for l in LEISTUNGEN)
            items.append(f'<li class="nav__item"><a class="nav__link" href="{root}{href}"{cur}>{label}</a>'
                         f'<ul class="nav__sub">{sub}</ul></li>')
        else:
            items.append(f'<li class="nav__item"><a class="nav__link" href="{root}{href}"{cur}>{label}</a></li>')
    cur = ' aria-current="page"' if active == "kontakt.html" else ""
    items.append(f'<li class="nav__item nav__item--cta"><a class="nav__link" href="{root}kontakt.html"{cur}>Kontakt</a></li>')
    return f"""<a class="skip-link" href="#main">Zum Inhalt springen</a>
<div class="topbar">
  <div class="container">
    <div class="topbar__items">
      <span>{icon("phone", 14)} <a href="tel:{TEL_LINK}">{TEL}</a></span>
      <span>{icon("mail", 14)} <a href="mailto:{MAIL}">{MAIL}</a></span>
    </div>
    <span>Mo–Fr 7:00–17:00 Uhr</span>
  </div>
</div>
<header class="header">
  <div class="container">
    <a class="logo" href="{root}index.html" aria-label="{FIRMA} – Startseite">
      <span class="logo__mark" aria-hidden="true"></span>
      <span class="logo__text">{FIRMA}<small>Meisterbetrieb seit 1998</small></span>
    </a>
    <button class="nav-toggle" aria-label="Menü öffnen" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav" aria-label="Hauptnavigation">
      <ul class="nav__list">
        {"".join(items)}
      </ul>
    </nav>
  </div>
</header>"""


def footer(root):
    leist = "".join(f'<li><a href="{root}leistungen/{l["slug"]}.html">{l["titel"]}</a></li>' for l in LEISTUNGEN)
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <a class="logo" href="{root}index.html"><span class="logo__mark" aria-hidden="true"></span><span class="logo__text">{FIRMA}</span></a>
        <p class="mt-2">Ihr Malermeister für Innenraum, Fassade und Bodenbeläge in Musterstadt und Umgebung.</p>
      </div>
      <div>
        <h4>Leistungen</h4>
        <ul>{leist}</ul>
      </div>
      <div>
        <h4>Unternehmen</h4>
        <ul>
          <li><a href="{root}ueber-uns.html">Über uns</a></li>
          <li><a href="{root}referenzen.html">Referenzen</a></li>
          <li><a href="{root}karriere.html">Karriere</a></li>
          <li><a href="{root}kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li>{STRASSE}<br>{ORT}</li>
          <li><a href="tel:{TEL_LINK}">{TEL}</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span id="year">2026</span> {FIRMA}</span>
      <ul>
        <li><a href="{root}impressum.html">Impressum</a></li>
        <li><a href="{root}datenschutz.html">Datenschutz</a></li>
      </ul>
    </div>
  </div>
</footer>"""


def page(path, title, description, body, active=""):
    depth = path.count("/")
    root = "../" * depth
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | {FIRMA}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{DOMAIN}/{path}">
  <link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
{header(root, active)}
<main id="main">
{body.replace("{root}", root)}
</main>
{footer(root)}
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def page_hero(title, text, crumbs):
    trail = ' / '.join(f'<a href="{{root}}{h}">{l}</a>' if h else l for l, h in crumbs)
    return f"""<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Brotkrumen">{trail}</nav>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>"""


CTA = f"""<section class="cta">
  <div class="container">
    <div>
      <h2>Sie planen ein Projekt?</h2>
      <p>Rufen Sie uns an oder fordern Sie ein kostenloses Angebot an.</p>
    </div>
    <a class="btn btn--dark" href="{{root}}kontakt.html">Kostenloses Angebot anfordern</a>
  </div>
</section>"""


def leistungs_cards():
    return "".join(f"""
      <article class="card">
        <div class="card__icon">{icon(l["icon"])}</div>
        <h3>{l["titel"]}</h3>
        <p>{l["kurz"]}</p>
        <a class="card__link" href="{{root}}leistungen/{l["slug"]}.html">Mehr erfahren →</a>
      </article>""" for l in LEISTUNGEN)


REFERENZEN = [
    ("innen", "Wohnzimmer in Warmgrau"), ("fassade", "Fassadensanierung Einfamilienhaus"),
    ("innen", "Büroräume Kanzlei"), ("boden", "Vinylboden Altbauwohnung"),
    ("fassade", "Mehrfamilienhaus mit WDVS"), ("kreativ", "Kalkputz im Bad"),
    ("innen", "Treppenhaus Neugestaltung"), ("kreativ", "Betonoptik Akzentwand"),
    ("boden", "Designbelag Praxis"),
]
REF_LABEL = {"innen": "Innenraum", "fassade": "Fassade", "boden": "Boden", "kreativ": "Kreativtechnik"}


def gallery(items):
    out = []
    for i, (cat, txt) in enumerate(items, 1):
        out.append(f"""
      <figure class="gallery__item" data-category="{cat}">
        <div class="media-placeholder">Bild referenz-{i:02d}.jpg</div>
        <figcaption>{txt}</figcaption>
      </figure>""")
    return "".join(out)


TESTIMONIALS = f"""<div class="grid grid--3">
      <figure class="testimonial">
        <div class="testimonial__stars" aria-label="5 von 5 Sternen">★★★★★</div>
        <blockquote>„Pünktlich, sauber und super freundlich. Unser Wohnzimmer sieht aus wie neu – absolute Empfehlung!“</blockquote>
        <figcaption>Familie Beispiel, Musterstadt</figcaption>
      </figure>
      <figure class="testimonial">
        <div class="testimonial__stars" aria-label="5 von 5 Sternen">★★★★★</div>
        <blockquote>„Die Fassade unseres Hauses wurde komplett saniert. Gute Beratung und faires Angebot.“</blockquote>
        <figcaption>Herr Muster, Nachbarort</figcaption>
      </figure>
      <figure class="testimonial">
        <div class="testimonial__stars" aria-label="5 von 5 Sternen">★★★★★</div>
        <blockquote>„Schnelle Terminvergabe und hervorragende Arbeit in unseren Praxisräumen.“</blockquote>
        <figcaption>Praxis Dr. Beispiel</figcaption>
      </figure>
    </div>"""


# ---------------------------------------------------------------- Startseite
page("index.html", "Malerbetrieb in Musterstadt",
     "Ihr Meisterbetrieb für Malerarbeiten, Fassadengestaltung, Tapezierarbeiten, Wärmedämmung und Bodenbeläge in Musterstadt und Umgebung.",
     f"""<section class="hero">
  <div class="container">
    <span class="eyebrow">Ihr Malermeister in Musterstadt</span>
    <h1>Farbe, die Ihr Zuhause zum Strahlen bringt.</h1>
    <p>Malerarbeiten, Fassadengestaltung und Bodenbeläge aus Meisterhand – sauber, zuverlässig und termingerecht.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="{{root}}kontakt.html">Kostenloses Angebot</a>
      <a class="btn btn--outline" href="{{root}}leistungen.html">Unsere Leistungen</a>
    </div>
    <ul class="hero__badges">
      <li>{icon("check", 20)} Meisterbetrieb</li>
      <li>{icon("check", 20)} Über 25 Jahre Erfahrung</li>
      <li>{icon("check", 20)} Festpreisangebote</li>
    </ul>
  </div>
</section>

<section class="section" id="leistungen">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow">Leistungen</span>
      <h2>Alles aus einer Hand</h2>
      <p class="lead">Von der Farbberatung bis zur fertigen Wand – wir begleiten Ihr Projekt vom ersten Gespräch bis zur Übergabe.</p>
    </div>
    <div class="grid grid--3">{leistungs_cards()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container grid grid--2">
    <div class="media-placeholder">Bild team.jpg</div>
    <div>
      <span class="eyebrow">Über uns</span>
      <h2>Handwerk mit Leidenschaft – seit über 25 Jahren</h2>
      <p>Als inhabergeführter Meisterbetrieb stehen wir für Qualität, Sauberkeit und Verlässlichkeit. Unser eingespieltes Team setzt Ihre Wünsche fachgerecht um – für Privatkunden, Hausverwaltungen und Gewerbe.</p>
      <ul class="checklist">
        <li>Persönliche Beratung vor Ort</li>
        <li>Transparente Festpreisangebote</li>
        <li>Saubere Baustelle & termingerechte Fertigstellung</li>
        <li>Ausbildungsbetrieb der Handwerkskammer</li>
      </ul>
      <a class="btn btn--dark" href="{{root}}ueber-uns.html">Mehr über uns</a>
    </div>
  </div>
</section>

<section class="stats">
  <div class="container grid grid--4">
    <div><div class="stat__num">25+</div><div class="stat__label">Jahre Erfahrung</div></div>
    <div><div class="stat__num">1.500+</div><div class="stat__label">Abgeschlossene Projekte</div></div>
    <div><div class="stat__num">12</div><div class="stat__label">Mitarbeiter</div></div>
    <div><div class="stat__num">4,9 ★</div><div class="stat__label">Kundenbewertung</div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow">So arbeiten wir</span>
      <h2>In 4 Schritten zum Ergebnis</h2>
    </div>
    <div class="grid grid--4 steps">
      <div class="step"><h3>Anfrage</h3><p>Sie kontaktieren uns telefonisch oder über das Formular.</p></div>
      <div class="step"><h3>Beratung</h3><p>Wir besichtigen das Objekt und beraten Sie zu Material und Farbe.</p></div>
      <div class="step"><h3>Angebot</h3><p>Sie erhalten ein transparentes Festpreisangebot.</p></div>
      <div class="step"><h3>Umsetzung</h3><p>Wir arbeiten sauber, pünktlich und übergeben besenrein.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow">Referenzen</span>
      <h2>Ausgewählte Projekte</h2>
    </div>
    <div class="gallery">{gallery(REFERENZEN[:6])}
    </div>
    <p class="text-center mt-2"><a class="btn btn--dark" href="{{root}}referenzen.html">Alle Referenzen ansehen</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow">Kundenstimmen</span>
      <h2>Das sagen unsere Kunden</h2>
    </div>
    {TESTIMONIALS}
  </div>
</section>

{CTA}""", "index.html")

# ---------------------------------------------------------------- Leistungen Übersicht
page("leistungen.html", "Leistungen",
     "Malerarbeiten, Fassadengestaltung, Tapezierarbeiten, Wärmedämmung, Bodenbeläge und kreative Techniken vom Meisterbetrieb.",
     f"""{page_hero("Unsere Leistungen", "Vom Innenanstrich bis zur Fassadendämmung – fachgerecht und aus einer Hand.", [("Startseite", "index.html"), ("Leistungen", None)])}

<section class="section">
  <div class="container">
    <div class="grid grid--3">{leistungs_cards()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head"><h2>Häufige Fragen</h2></div>
    <div class="faq prose" style="margin: 0 auto;">
      <details><summary>Ist das Angebot kostenlos?</summary><p>Ja, Besichtigung und Angebot sind für Sie kostenlos und unverbindlich.</p></details>
      <details><summary>Wie schnell bekomme ich einen Termin?</summary><p>In der Regel können wir innerhalb weniger Tage einen Besichtigungstermin vereinbaren.</p></details>
      <details><summary>Arbeiten Sie auch für Gewerbekunden?</summary><p>Ja, wir sind für Privatkunden, Hausverwaltungen, Wohnungsbaugesellschaften und Gewerbe tätig.</p></details>
      <details><summary>Muss ich die Möbel selbst wegräumen?</summary><p>Nein, auf Wunsch übernehmen wir das Abdecken und Umräumen der Möbel.</p></details>
    </div>
  </div>
</section>

{CTA}""", "leistungen.html")

# ---------------------------------------------------------------- Leistungs-Detailseiten
for l in LEISTUNGEN:
    andere = "".join(f'<li><a href="{{root}}leistungen/{o["slug"]}.html">{o["titel"]}</a></li>' for o in LEISTUNGEN if o is not l)
    punkte = "".join(f"<li>{p}</li>" for p in l["punkte"])
    page(f"leistungen/{l['slug']}.html", l["titel"], l["kurz"],
         f"""{page_hero(l["titel"], l["kurz"], [("Startseite", "index.html"), ("Leistungen", "leistungen.html"), (l["titel"], None)])}

<section class="section">
  <div class="container grid grid--2">
    <div>
      <h2>{l["titel"]} vom Meisterbetrieb</h2>
      <p>{l["intro"]}</p>
      <h3>Unsere Leistungen im Überblick</h3>
      <ul class="checklist">{punkte}</ul>
      <a class="btn btn--primary" href="{{root}}kontakt.html">Angebot anfordern</a>
    </div>
    <div class="media-placeholder">Bild {l["slug"]}.jpg</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head"><h2>Weitere Leistungen</h2></div>
    <ul class="checklist" style="columns: 2; max-width: 640px; margin: 0 auto;">{andere}</ul>
  </div>
</section>

{CTA}""", "leistungen.html")

# ---------------------------------------------------------------- Über uns
page("ueber-uns.html", "Über uns",
     f"Lernen Sie {FIRMA} kennen – Ihr Meisterbetrieb mit über 25 Jahren Erfahrung.",
     f"""{page_hero("Über uns", "Ein Familienbetrieb mit Tradition, Qualität und einem starken Team.", [("Startseite", "index.html"), ("Über uns", None)])}

<section class="section">
  <div class="container grid grid--2">
    <div>
      <span class="eyebrow">Unsere Geschichte</span>
      <h2>Vom Ein-Mann-Betrieb zum starken Team</h2>
      <p>1998 gründete Malermeister {INHABER} den Betrieb in Musterstadt. Heute sind wir ein Team aus Gesellen, Auszubildenden und Meistern, das Projekte jeder Größe umsetzt.</p>
      <p>Was uns antreibt: zufriedene Kunden, nachhaltige Materialien und ehrliches Handwerk.</p>
    </div>
    <div class="media-placeholder">Bild firmengebaeude.jpg</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Werte</span><h2>Dafür stehen wir</h2></div>
    <div class="grid grid--3">
      <article class="card"><h3>Qualität</h3><p>Meisterliche Ausführung und hochwertige Markenprodukte.</p></article>
      <article class="card"><h3>Zuverlässigkeit</h3><p>Verbindliche Termine und transparente Festpreise.</p></article>
      <article class="card"><h3>Sauberkeit</h3><p>Sorgfältiges Abdecken und besenreine Übergabe.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Team</span><h2>Unser Team</h2></div>
    <div class="grid grid--4">
      <div><div class="media-placeholder">Foto</div><h3 class="mt-2">{INHABER}</h3><p>Malermeister & Inhaber</p></div>
      <div><div class="media-placeholder">Foto</div><h3 class="mt-2">Name Nachname</h3><p>Malergeselle</p></div>
      <div><div class="media-placeholder">Foto</div><h3 class="mt-2">Name Nachname</h3><p>Bodenleger</p></div>
      <div><div class="media-placeholder">Foto</div><h3 class="mt-2">Name Nachname</h3><p>Büro & Organisation</p></div>
    </div>
  </div>
</section>

{CTA}""", "ueber-uns.html")

# ---------------------------------------------------------------- Referenzen
filter_btns = '<button class="is-active" data-filter="alle">Alle</button>' + "".join(
    f'<button data-filter="{k}">{v}</button>' for k, v in REF_LABEL.items())
page("referenzen.html", "Referenzen",
     "Ausgewählte Projekte: Innenraumgestaltung, Fassaden, Bodenbeläge und kreative Wandtechniken.",
     f"""{page_hero("Referenzen", "Ein Auszug aus unseren abgeschlossenen Projekten.", [("Startseite", "index.html"), ("Referenzen", None)])}

<section class="section">
  <div class="container">
    <div class="filter" role="group" aria-label="Referenzen filtern">{filter_btns}</div>
    <div class="gallery">{gallery(REFERENZEN)}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head"><h2>Kundenstimmen</h2></div>
    {TESTIMONIALS}
  </div>
</section>

{CTA}""", "referenzen.html")

# ---------------------------------------------------------------- Karriere
page("karriere.html", "Karriere & Ausbildung",
     "Jobs und Ausbildung beim Malermeisterbetrieb: Malergeselle (m/w/d), Auszubildende (m/w/d) und mehr.",
     f"""{page_hero("Karriere", "Werde Teil unseres Teams – wir suchen Verstärkung!", [("Startseite", "index.html"), ("Karriere", None)])}

<section class="section">
  <div class="container grid grid--2">
    <div>
      <h2>Warum bei uns arbeiten?</h2>
      <ul class="checklist">
        <li>Unbefristete Festanstellung & pünktliche Bezahlung</li>
        <li>Moderne Werkzeuge und Arbeitskleidung</li>
        <li>Weiterbildung bis zum Meister</li>
        <li>Familiäres Betriebsklima</li>
        <li>Abwechslungsreiche Projekte in der Region</li>
      </ul>
    </div>
    <div class="media-placeholder">Bild team-baustelle.jpg</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head"><h2>Offene Stellen</h2></div>
    <div class="grid grid--3">
      <article class="job">
        <div class="job__meta"><span>Vollzeit</span><span>Musterstadt</span></div>
        <h3>Malergeselle (m/w/d)</h3>
        <p>Abgeschlossene Ausbildung, Führerschein Klasse B, Teamgeist.</p>
        <a class="card__link" href="mailto:{MAIL}?subject=Bewerbung%20Malergeselle">Jetzt bewerben →</a>
      </article>
      <article class="job">
        <div class="job__meta"><span>Ausbildung</span><span>3 Jahre</span></div>
        <h3>Auszubildende/r Maler/in & Lackierer/in</h3>
        <p>Spaß am Handwerk, Kreativität und Zuverlässigkeit.</p>
        <a class="card__link" href="mailto:{MAIL}?subject=Bewerbung%20Ausbildung">Jetzt bewerben →</a>
      </article>
      <article class="job">
        <div class="job__meta"><span>Vollzeit</span><span>Musterstadt</span></div>
        <h3>Bodenleger (m/w/d)</h3>
        <p>Erfahrung in der Verlegung von Vinyl, Laminat und Teppich.</p>
        <a class="card__link" href="mailto:{MAIL}?subject=Bewerbung%20Bodenleger">Jetzt bewerben →</a>
      </article>
    </div>
    <p class="text-center mt-2">Keine passende Stelle dabei? Senden Sie uns gern eine Initiativbewerbung an <a href="mailto:{MAIL}">{MAIL}</a>.</p>
  </div>
</section>""", "karriere.html")

# ---------------------------------------------------------------- Kontakt
optionen = "".join(f"<option>{l['titel']}</option>" for l in LEISTUNGEN)
page("kontakt.html", "Kontakt",
     f"Kontakt zu {FIRMA}: Telefon, E-Mail, Anfahrt und Anfrageformular für Ihr kostenloses Angebot.",
     f"""{page_hero("Kontakt", "Wir freuen uns auf Ihre Anfrage und melden uns zeitnah zurück.", [("Startseite", "index.html"), ("Kontakt", None)])}

<section class="section">
  <div class="container contact-grid">
    <div>
      <h2>So erreichen Sie uns</h2>
      <ul class="contact-info">
        <li>{icon("pin", 22)}<span><strong>{FIRMA}</strong><br>{STRASSE}<br>{ORT}</span></li>
        <li>{icon("phone", 22)}<a href="tel:{TEL_LINK}">{TEL}</a></li>
        <li>{icon("mail", 22)}<a href="mailto:{MAIL}">{MAIL}</a></li>
      </ul>
      <h3>{icon("clock", 20)} Bürozeiten</h3>
      <table class="hours">
        <tr><td>Montag – Donnerstag</td><td>7:00 – 17:00 Uhr</td></tr>
        <tr><td>Freitag</td><td>7:00 – 14:00 Uhr</td></tr>
        <tr><td>Samstag & Sonntag</td><td>geschlossen</td></tr>
      </table>
    </div>
    <div>
      <h2>Anfrage senden</h2>
      <!-- TODO: action auf Formular-Backend (z. B. PHP-Mailer, Formspree) setzen und data-demo entfernen -->
      <form class="form" action="#" method="post" data-demo>
        <div class="form__field"><label for="name">Name *</label><input id="name" name="name" required autocomplete="name"></div>
        <div class="form__field"><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel" autocomplete="tel"></div>
        <div class="form__field"><label for="email">E-Mail *</label><input id="email" name="email" type="email" required autocomplete="email"></div>
        <div class="form__field"><label for="ort">PLZ / Ort</label><input id="ort" name="ort" autocomplete="postal-code"></div>
        <div class="form__field form__field--full"><label for="leistung">Leistung</label>
          <select id="leistung" name="leistung"><option value="">Bitte wählen</option>{optionen}<option>Sonstiges</option></select></div>
        <div class="form__field form__field--full"><label for="nachricht">Ihre Nachricht *</label><textarea id="nachricht" name="nachricht" required></textarea></div>
        <label class="form__check form__field--full"><input type="checkbox" name="datenschutz" required> <span>Ich habe die <a href="{{root}}datenschutz.html">Datenschutzerklärung</a> gelesen und stimme der Verarbeitung meiner Daten zu. *</span></label>
        <div class="form__field--full"><button class="btn btn--primary" type="submit">Anfrage absenden</button></div>
        <p class="form__note form__field--full">* Pflichtfelder</p>
        <p class="form__status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>

<section class="map-placeholder">
  <p>Kartenbereich (z. B. Google Maps / OpenStreetMap) – aus Datenschutzgründen erst nach Einwilligung laden.</p>
</section>""", "kontakt.html")

# ---------------------------------------------------------------- Impressum
page("impressum.html", "Impressum", f"Impressum von {FIRMA}.",
     f"""{page_hero("Impressum", "Angaben gemäß § 5 DDG", [("Startseite", "index.html"), ("Impressum", None)])}
<section class="section">
  <div class="container prose">
    <p><strong>Hinweis:</strong> Platzhaltertext – bitte durch die echten Pflichtangaben ersetzen.</p>
    <h2>Anbieter</h2>
    <p>{FIRMA}<br>Inhaber: {INHABER}<br>{STRASSE}<br>{ORT}</p>
    <h2>Kontakt</h2>
    <p>Telefon: {TEL}<br>E-Mail: {MAIL}</p>
    <h2>Umsatzsteuer-ID</h2>
    <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE000000000</p>
    <h2>Berufsbezeichnung und berufsrechtliche Regelungen</h2>
    <p>Berufsbezeichnung: Maler- und Lackierermeister (verliehen in Deutschland)<br>
    Zuständige Kammer: Handwerkskammer Musterstadt<br>
    Eintragung in die Handwerksrolle: Nr. 000000</p>
    <h2>Verbraucherstreitbeilegung</h2>
    <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
  </div>
</section>""")

# ---------------------------------------------------------------- Datenschutz
page("datenschutz.html", "Datenschutz", f"Datenschutzerklärung von {FIRMA}.",
     f"""{page_hero("Datenschutzerklärung", "Informationen zur Verarbeitung Ihrer personenbezogenen Daten", [("Startseite", "index.html"), ("Datenschutz", None)])}
<section class="section">
  <div class="container prose">
    <p><strong>Hinweis:</strong> Platzhaltertext – bitte durch eine rechtlich geprüfte Datenschutzerklärung ersetzen (z. B. über einen Datenschutz-Generator).</p>
    <h2>1. Verantwortlicher</h2>
    <p>{FIRMA}, {INHABER}, {STRASSE}, {ORT}, E-Mail: {MAIL}</p>
    <h2>2. Hosting</h2>
    <p>[Angaben zum Hosting-Anbieter und zu Server-Logfiles]</p>
    <h2>3. Kontaktformular und E-Mail</h2>
    <p>[Angaben zur Verarbeitung von Anfragen, Rechtsgrundlage Art. 6 Abs. 1 lit. b DSGVO, Speicherdauer]</p>
    <h2>4. Kartendienste</h2>
    <p>[Angaben zu eingebundenen Karten, z. B. Google Maps oder OpenStreetMap]</p>
    <h2>5. Ihre Rechte</h2>
    <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht auf Beschwerde bei einer Aufsichtsbehörde.</p>
  </div>
</section>""")

# ---------------------------------------------------------------- 404
page("404.html", "Seite nicht gefunden", "Die angeforderte Seite wurde nicht gefunden.",
     """<section class="section text-center">
  <div class="container">
    <h1>404 – Seite nicht gefunden</h1>
    <p class="lead">Die gesuchte Seite existiert leider nicht (mehr).</p>
    <a class="btn btn--primary" href="{root}index.html">Zur Startseite</a>
  </div>
</section>""")

# ---------------------------------------------------------------- sitemap
urls = ["index.html", "leistungen.html"] + [f"leistungen/{l['slug']}.html" for l in LEISTUNGEN] + [
    "ueber-uns.html", "referenzen.html", "karriere.html", "kontakt.html", "impressum.html", "datenschutz.html"]
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{DOMAIN}/{u}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
print("ok")
