# geoset.pl

Minimalna strona startowa dla **geoset.pl**, publikowana przez GitHub Pages.

Bez build stepu, bez zależności, bez JS-a: dwa pliki HTML, jeden arkusz stylów i logo SVG.
Strona dostosowuje się do trybu jasnego/ciemnego (`prefers-color-scheme`).

## Pliki

| Plik | Rola |
|---|---|
| `index.html` | strona główna — logo + tytuł |
| `404.html` | strona błędu 404 |
| `styles.css` | cała stylistyka |
| `logo.svg` | znak firmowy (favicon + logo na stronie) |
| `CNAME` | domena dla GitHub Pages (`geoset.pl`) |
| `.nojekyll` | wyłącza przetwarzanie przez Jekyll |

`index.html` używa ścieżek relatywnych (działa też pod `budziam.github.io/geoset-site/`),
`404.html` — bezwzględnych, bo GitHub Pages serwuje 404 pod dowolną głębokością ścieżki.

Podmiana logo: nadpisz `logo.svg` (najlepiej `viewBox="0 0 64 64"`).
Podmiana nazwy: `<h1 class="title">` w `index.html` oraz `<title>` i tagi `og:`.

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
