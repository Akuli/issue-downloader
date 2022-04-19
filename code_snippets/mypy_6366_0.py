def assert_never(x: Any) -> NoReturn:
    assert False, "Unhandled type: {}".format(type(x).__name__)

PetLiteral = Literal['dog', 'cat', 'iguana']

def make_sound_literal(pet: PetLiteral) -> str:
    if pet == 'dog':
        return 'woof'
    elif pet == 'cat':
        return 'meow'
    # elif pet == 'iguana':
    #     return 'confused silence'
    else:
        assert_never(pet)
