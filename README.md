# open_brewery_db.py
Web-API for [openbrewerydb.org](https://www.openbrewerydb.org) website which is free dataset with public information on breweries, cideries, brewpubs, and bottleshops

## Example
```python
from open_brewery_db import OpenBreweryDb

obdb = OpenBreweryDb()
random_brewery = obdb.get_random_brewery()
print(random_brewery)
```
