import threading
_parameter_values = threading.local()
_parameter_values.data = {}
_parameter_values.data[3] = "hello"
_parameter_values.data["hello"] = 3

import threading
_parameter_values = threading.local()
_parameter_values.data: Dict[int, str] = {}
_parameter_values.data[3] = "hello"
