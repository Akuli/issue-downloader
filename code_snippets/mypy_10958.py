class MyError(Exception): pass
class RuntimeError(RuntimeError, MyError): pass
