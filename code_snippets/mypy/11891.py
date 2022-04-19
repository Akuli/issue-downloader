class Bar(object):
    ...

reveal_type(Bar.__slots__)
reveal_type(Bar().__slots__)
