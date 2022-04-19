class Application(MutableMapping[Union[str, AppKey[Any]], Any]):
    @overload
    def __getitem__(self, key: AppKey[_T]) -> _T: ...
    @overload
    def __getitem__(self, key: str) -> Any: ...
    def __getitem__(self, key: Union[str, AppKey[_T]]) -> Any:
        return self._state[key]
