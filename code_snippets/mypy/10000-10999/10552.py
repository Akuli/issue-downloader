class Tst:
    def __init__(self) -> None:
        ...

    def create_field(self) -> None:
        self.abc = 1  # Please, generate error here

    def print_field(self) -> None:
        print(self.abc)  # And, optionally here...


def main() -> None:
    tst = Tst()
    tst.print_field()


if __name__ == '__main__':
    main()

