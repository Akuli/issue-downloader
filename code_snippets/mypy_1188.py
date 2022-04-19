if True:
    from pycurl import Curl, version_info
else:
    from mock import Mock
    Curl = Mock()
    version_info = Mock()
