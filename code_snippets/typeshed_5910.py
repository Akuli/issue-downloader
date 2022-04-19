JsonObject = dict[str, Any]  # Any is Json
JsonArray = list[Any]  # Any is Json
Json = JsonObject | JsonArray | str | float | int | bool | None
