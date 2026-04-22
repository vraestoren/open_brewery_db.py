from requests import Session

class OpenBreweryDb:
	def __init__(self) -> None:
		self.api = "https://api.openbrewerydb.org/v1"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
		}

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params or {}).json()

	def _build_params(self, **kwargs) -> dict:
		return {key: value for key, value in kwargs.items() if value is not None}

	def get_single_brewery(
			self,
			brewery_id: str) -> dict:
		return self._get(f"/breweries/{brewery_id}")

	def get_breweries_list(
			self,
			page: int = 1,
			per_page: int = 50,
			by_city: str = None,
			by_country: str = None,
			by_dist: str = None,
			by_ids: str = None,
			by_name: str = None,
			by_state: str = None,
			by_postal: str = None,
			by_type: str = None,
			sort: str = None) -> dict:
		params = self._build_params(
			page=page,
			per_page=per_page,
			by_city=by_city,
			by_country=by_country,
			by_dist=by_dist,
			by_ids=by_ids,
			by_name=by_name,
			by_state=by_state,
			by_postal=by_postal,
			by_type=by_type,
			sort=sort
		)
		return self._get("/breweries", params)

	def get_random_brewery(
			self,
			size: int = None) -> dict:
		params = self._build_params(size=size)
		return self._get("/breweries/random", params)

	def search_breweries(
			self,
			query: str,
			page: int = None,
			per_page: int = None) -> dict:
		params = self._build_params(
			query=query,
			page=page,
			per_page=per_page
		)
		return self._get("/breweries/search", params)

	def get_breweries_autocomplete(
			self,
			query: str) -> dict:
		params = self._build_params(query=query)
		return self._get("/breweries/autocomplete", params)

	def get_breweries_meta(
			self,
			by_city: str = None,
			by_country: str = None,
			by_dist: str = None,
			by_ids: str = None,
			by_name: str = None,
			by_state: str = None,
			by_postal: str = None,
			by_type: str = None) -> dict:
		params = self._build_params(
			by_city=by_city,
			by_country=by_country,
			by_dist=by_dist,
			by_ids=by_ids,
			by_name=by_name,
			by_state=by_state,
			by_postal=by_postal,
			by_type=by_type
		)
		return self._get("/breweries/meta", params)
