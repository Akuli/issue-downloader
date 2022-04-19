class Foo:
    def factory(self) -> str:
        return 'Hello'

class Bar(Foo):
    def factory(self) -> int:
        return 10

class QPixmap(QPaintDevice):
    def swap(self, other: 'QPixmap') -> None: ...

class QBitmap(QPixmap):
    def swap(self, other: 'QBitmap') -> None: ...

class QBitmap(QPixmap):
    @covariant_args
    def swap(self, other: 'QBitmap') -> None: ...

class QBitmap(Implementation[QPixmap]):
    def swap(self, other: 'QBitmap') -> None: ...
