from requests import Session

class OpenBreweryDb:
	def __init__(self) -> None:
		self.api = "https://api.openbrewerydb.org"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
		}

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params or {}).json()

	def get_single_brewery(self, brewery_id: str) -> dict:
		return self._get(f"/breweries/{brewery_id}")

	def get_breweries_list(
			self,
			page: int,
			per_page: int) -> dict:
		params = {
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_breweries_by_city(
			self, city: str, page: int, per_page: int) -> dict:
		params = {
			"by_city": city,
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_breweries_by_dist(
			self, dist: str, page: int, per_page: int) -> dict:
		params = {
			"by_dist": dist,
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_breweries_by_name(
			self,
			name: str,
			page: int,
			per_page: int) -> dict:
		params = {
			"by_name": name,
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_breweries_by_state(
			self,
			state: str,
			page: int,
			per_page: int) -> dict:
		params = {
			"by_state": state,
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_breweries_by_postal(
			self,
			postal: int,
			page: int,
			per_page: int) -> dict:
		params = {
			"by_postal": postal,
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_breweries_by_type(
			self,
			type: str,
			page: int,
			limit: int) -> dict:
		params = {
			"by_type": type,
			"page": page,
			"per_page": per_page
		}
		return self._get("/breweries", params)

	def get_random_brewery(self) -> dict:
		return self._get("/breweries/random")

	def search_breweries(self, query: str) -> dict:
		params = {"query": query}
		return self._get("/breweries/search", params)
