import collections
from typing import Any, Dict, Text

class PlainOldData:

    def as_json_dict(self) -> Dict[Text, Any]:
        result = collections.OrderedDict()
        for k in self.__slots__:
            value = getattr(self, k)
            if value is not None:
                result[k] = value
        return result
