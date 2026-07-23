# India Paper Leaks — Public Transparency Map

An interactive choropleth of every documented question-paper leak in India, 2014–2024.

**Live site:** https://royronit.github.io/india-paper-leaks-map/

## What's here

- `index.html` — the single-page app (vanilla JS + D3 v7 from CDN)
- `app_bundle.json` — cleaned, structured incident data (66 records)
- `india_states.geojson` — simplified India state boundaries (190 KB)

## Data source

Compiled from public news reports by [Mauryan Shivam](https://www.kaggle.com/datasets/mauryansshivam/india-question-paper-leaks-incidents-details) on Kaggle, licensed CC BY-NC-SA 4.0. Original news references are linked from every incident card.

## Local dev

```
cd site
python3 -m http.server 8765
open http://localhost:8765
```

## Highlights from the data

- 66 documented incidents across 23 states, 10-year span
- 73% of alleged leaks were officially confirmed
- ~4× rise in the last 5 years vs the prior 5
- Only 3 of 66 cases resulted in a chargesheet
- UP (11), Maharashtra (6), Bihar (5) most affected
