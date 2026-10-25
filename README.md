# geoset.pl

Minimalna strona startowa dla **geoset.pl**, publikowana przez GitHub Pages.

Bez build stepu, bez zależności, bez JS-a: dwa pliki HTML, jeden arkusz stylów i logo.
Strona dostosowuje się do trybu jasnego/ciemnego (`prefers-color-scheme`).

## Pliki

| Plik | Rola |
|---|---|
| `index.html` | strona główna — samo logo (nazwa jest częścią znaku) |
| `404.html` | strona błędu 404 |
| `styles.css` | cała stylistyka |
| `logo.png` | oficjalny znak firmowy, 960×361, przycięty z mastera |
| `icon.png` | favicon / apple-touch-icon, 180×180 (fragment globusa) |
| `logo-source.png` | master 1458×1458 — źródło do ponownego eksportu |
| `CNAME` | domena dla GitHub Pages (`geoset.pl`) |
| `.nojekyll` | wyłącza przetwarzanie przez Jekyll |

`index.html` używa ścieżek relatywnych, `404.html` — bezwzględnych, bo GitHub Pages
serwuje 404 pod dowolną głębokością ścieżki.

Podglądu pod `budziam.github.io/geoset-site/` nie ma: obecność `CNAME` powoduje, że
GitHub przekierowuje ten adres na `geoset.pl`. Żeby zobaczyć stronę przed zmianą DNS,
usuń na chwilę `CNAME`, albo testuj lokalnie (`python3 -m http.server`).

Logo: `logo-source.png` to oryginał z profilu FB firmy (biały blok 1458×1458).
`logo.png` powstał przez przycięcie marginesów, sprowadzenie tła do czystej bieli
i eksport w 960 px (2× szerokości wyświetlania). Podmieniając logo, zachowaj proporcje
i zostaw białe tło — w trybie ciemnym strona kładzie je na białej płytce.

Podmiana nazwy/opisu: `<title>`, `meta description` i tagi `og:` w `index.html`.

## Publikacja

```bash
gh repo create geoset-site --public --source=. --remote=origin --push
```

Następnie w repozytorium: **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`**,
potem **Custom domain: `geoset.pl`** i po propagacji DNS **Enforce HTTPS**.

## DNS (Cloudflare)

Rekordy dla GitHub Pages muszą być **bez proxy** (szara chmurka / DNS only).
Pomarańczowa chmurka przed GitHub Pages kończy się błędem TLS.

| Typ | Nazwa | Wartość |
|---|---|---|
| A | `@` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| CNAME | `www` | `budziam.github.io` |
| TXT | `_github-pages-challenge-budziam` | wartość z Settings → Pages (weryfikacja domeny) |

## ⚠️ Zanim przełączysz apex

**`geoset.pl` ma dziś `MX 10 geoset.pl`** — czyli poczta wskazuje na goły apex, który
rozwiązuje się na NAS (`46.149.216.20`). Po przełączeniu rekordów A na GitHub Pages
**poczta przestanie działać**, bo MX nadal będzie wskazywał na GitHub.

Kolejność:

1. Dodaj `mail.geoset.pl` (A → `46.149.216.20`, bez proxy).
2. Zmień MX na `10 mail.geoset.pl`.
3. Sprawdź dostarczanie poczty.
4. Dopiero potem przełącz apex na GitHub Pages.

Efekt uboczny (dobry): apex przestaje ujawniać publiczny adres IP originu.
Poddomeny `czaspracy`, `panel`, `poczta` nadal tam siedzą — jeśli mają zostać za
Cloudflare, upewnij się, że nie mają własnych rekordów DNS-only.
