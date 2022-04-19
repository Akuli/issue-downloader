@lru_cache(maxsize=1)
def get_response_from_api() -> List[ApiObject]:
    url = _get_api_url()
    response = requests.get(url).text
    return json.loads(response, object_hook=_create_api_obj)
