import threading
_parameter_values = threading.local()
_parameter_values.data: Dict[int, str] = {}
_parameter_values.data[3] = "hello"
