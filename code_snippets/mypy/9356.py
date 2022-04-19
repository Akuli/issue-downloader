def get_mock_module(v: Literal["mock"] | Literal["unittest.mock"]) -> ...:
     return pkgutils.resolve_name(v)
