class MessageIdStore:
    def __init__(self):
        self.__msgid_to_symbol: Dict[str, str] = {}
        self.__symbol_to_msgid: Dict[str, str] = {}

    def check_msgid_and_symbol(self, msgid: str, symbol: str) -> None:
        existing_msgid: Optional[str] = self.__symbol_to_msgid.get(symbol)
        existing_symbol: Optional[str] = self.__msgid_to_symbol.get(msgid)
        if existing_symbol is None and existing_msgid is None:
            return  # both symbol and msgid are usable
        if existing_msgid is not None:
            if existing_msgid != msgid:
                self._raise_duplicate_msgid(symbol, msgid, existing_msgid) 
        if existing_symbol != symbol:
            # This will emit: 'Argument 3 to "_raise_duplicate_symbol" of "MessageIdStore" 
            # has incompatible type "Optional[str]"; expected "str"'
            self._raise_duplicate_symbol(msgid, symbol, existing_symbol) 

    @staticmethod
    def _raise_duplicate_symbol(msgid: str, symbol: str, other_symbol: str) -> None:
        ...

    @staticmethod
    def _raise_duplicate_msgid(symbol: str, msgid: str, other_msgid: str) -> None:
        ...   
