# <img src="https://www.openbrewerydb.org/favicon.png" width="40" style="vertical-align:middle;" /> open_brewery_db.py
> Web-API for [Open Brewery DB](https://www.openbrewerydb.org) a free public API for brewery data including locations, types, and search across the US and beyond.

## Quick Start
```python
from open_brewery_db import OpenBreweryDb
db = OpenBreweryDb()

# Get a specific brewery
print(db.get_single_brewery("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"))

# Search breweries by name
print(db.get_breweries_list(by_name="dog", per_page=5))

# Get a random brewery
print(db.get_random_brewery())
```

---

## Breweries

| Method | Description |
|--------|-------------|
| `get_single_brewery(brewery_id)` | Get a single brewery by ID |
| `get_breweries_list(...)` | List breweries with optional filters |
| `get_random_brewery(size)` | Get one or more random breweries |
| `search_breweries(query, ...)` | Full-text search across breweries |
| `get_breweries_autocomplete(query)` | Autocomplete suggestions by name |
| `get_breweries_meta(...)` | Get total count for a filtered query |

---

## Filters (`get_breweries_list`)

| Parameter | Description |
|-----------|-------------|
| `by_city` | Filter by city name |
| `by_country` | Filter by country |
| `by_dist` | Filter by distance — `lat,lng` format |
| `by_ids` | Filter by comma-separated list of IDs |
| `by_name` | Filter by brewery name |
| `by_state` | Filter by state |
| `by_postal` | Filter by postal/zip code |
| `by_type` | Filter by brewery type (see below) |
| `sort` | Sort results — e.g. `type:asc` or `name:desc` |
| `page` | Page number (default: `1`) |
| `per_page` | Results per page (default: `50`, max: `200`) |

**Brewery types:**

| Value | Meaning |
|-------|---------|
| `micro` | Small independent brewery |
| `nano` | Extremely small brewery |
| `regional` | Regional location of a brewery |
| `brewpub` | Brewery with a pub or restaurant |
| `large` | Large brewery |
| `planning` | In planning phase |
| `bar` | Bar without brewing |
| `contract` | Contracted brewing |
| `proprietor` | Proprietary brewery |
| `closed` | Permanently closed |
